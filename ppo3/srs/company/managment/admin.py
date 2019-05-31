from django.contrib import admin
from django.contrib.auth.models import User, Group
from . import models as m
from django.forms import ModelForm, ValidationError
from django import forms
from django.db import connection
from managment.utils import make_date, MONTH


admin.site.site_header = 'Компания'

admin.site.unregister(Group)


@admin.register(m.Unit)
class UnitAdmin(admin.ModelAdmin):
    fields = ('id', 'name')
    readonly_fields = ('id',)
    list_display = fields
    list_display_links = list_display



@admin.register(m.Material)
class MaterialAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'unit', 'summ', 'quantity')
    readonly_fields = ('id',)
    list_display = fields
    list_display_links = list_display


@admin.register(m.Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'unit', 'summ', 'quantity')
    readonly_fields = ('id',)
    list_display = fields
    list_display_links = list_display


@admin.register(m.Position)
class PositionAdmin(admin.ModelAdmin):
    fields = ('id', 'name',)
    readonly_fields = ('id',)
    list_display = fields
    list_display_links = list_display


@admin.register(m.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    #fields = ('id', 'name', 'position', 'salary', 'address', 'phone')
    list_display = ('name', 'position', 'salary', 'address')
    list_display_links = list_display


@admin.register(m.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = ('id', 'product', 'material', 'quantity')
    readonly_fields = ('id',)
    list_display = fields
    list_display_links = list_display


@admin.register(m.Budget)
class BudgetAdmin(admin.ModelAdmin):
    fields = ('id', 'summ', )
    readonly_fields = ('id',)
    list_display = fields
    list_display_links = list_display


class PurchaseForm(ModelForm):
    class Meta:
        model = m.Purchase
        fields = ('material', 'quantity', 'summ', 'time', 'employee')

    def clean(self):
        cleaned_data = super().clean()
        budget = m.Budget.objects.first()
        if budget.summ < cleaned_data['summ']:
            raise ValidationError('budget is not enough')
        return cleaned_data


@admin.register(m.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    form = PurchaseForm
    # fields = ('id', 'material', 'quantity', 'summ', 'time', 'employee')
    list_display = ('material', 'quantity', 'summ', 'time', 'employee')
    list_display_links = list_display


class SaleForm(ModelForm):
    class Meta:
        model = m.Sale
        fields = ('product', 'quantity', 'summ', 'time', 'employee')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['product'].quantity < cleaned_data['quantity']:
            raise ValidationError('not enough products')
        return cleaned_data


@admin.register(m.Sale)
class SaleAdmin(admin.ModelAdmin):
    form = SaleForm
    fields = ('id', 'product', 'quantity', 'summ', 'time', 'employee')
    readonly_fields = ('id',)
    list_display = fields
    list_display_links = list_display


class ProductionForm(ModelForm):
    class Meta:
        model = m.Production
        fields = ('id', 'product', 'quantity', 'time', 'employee')

    def clean(self):
        cleaned_data = super().clean()
        cursor = connection.cursor()
        cursor.execute(f'''
        DECLARE @r int;
        EXEC materials_enough @product_id={cleaned_data['product'].id}, @quantity={cleaned_data['quantity']}, @result = @r OUTPUT;
        SELECT @r;
        ''')
        result, = cursor.fetchone()

        cursor.close()

        if result == 0:
            raise ValidationError('materials not enough', 'invalid', {'quantity': 'too big'})
        return cleaned_data


@admin.register(m.Production)
class ProductionAdmin(admin.ModelAdmin):
    form = ProductionForm
    fields = ('id', 'product', 'quantity', 'time', 'employee')
    readonly_fields = ('id',)
    list_display = fields
    list_display_links = list_display


class Payroll(ModelForm):
    class Meta:
        model = m.Payroll
        fields = ('id', 'employee', 'date', 'year', 'salary', 'prize')
    date = forms.ChoiceField(choices=((1, "Январь"),
                                      (2, "Февраль"),
                                      (3, "Март"),
                                      (4, "Апрель"),
                                      (5, "Май"),
                                      (6, "Июнь"),
                                      (7, "Июль"),
                                      (8, "Август"),
                                      (9, "Сентябрь"),
                                      (10, "Октябрь"),
                                      (11, "Ноябрь"),
                                      (12, "Декабрь"))
                             )
    year = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['date'] = make_date(cleaned_data['year'], cleaned_data['date'])
        cursor = connection.cursor()
        sql = f'''
        DECLARE @r int;
        EXEC payroll_check 
        @employee_id={cleaned_data['employee'].id}, 
        @date_="{cleaned_data['date']}", 
        @final_salary={cleaned_data['salary'] + cleaned_data['prize']},
        @result = @r OUTPUT;
        SELECT @r;
        '''
        cursor.execute(sql)
        result, = cursor.fetchone()

        cursor.close()
        if result == 1:
            raise ValidationError('Недостаточно средств в бюджете')

        if result == 2:
            raise ValidationError('Уже выдали за этот месяц')

        return cleaned_data



@admin.register(m.Payroll)
class PayrollAdmin(admin.ModelAdmin):
    form = Payroll
    # change_form_template = 'payroll.html'
    list_display = ('id', 'year', 'monthh', 'employee', 'salary', 'prize')

    def monthh(self, obj):
        return MONTH[obj.month]
    list_display_links = list_display
    add_form_template = 'payroll.html'


@admin.register(m.Credit)
class CreditAdmin(admin.ModelAdmin):
    ...


class RepaymentForm(ModelForm):
    class Meta:
        model = m.Repayment
        fields = ('bank', 'payment_date')

    def clean(self):
        cleaned_data = super().clean()
        cursor = connection.cursor()
        cursor.execute(f'''
        DECLARE @r int;
        EXEC new_repayment @credit={cleaned_data['bank'].id}, @payment_date="{cleaned_data['payment_date']}", @result = @r OUTPUT;
        SELECT @r;
        ''')
        result, = cursor.fetchone()
        print(result)

        cursor.close()


        if result == 1:
            raise ValidationError('не хватает денег')
        if result == 2:
            raise ValidationError('уже заплатили')
        return cleaned_data


@admin.register(m.Repayment)
class RepaymentAdmin(admin.ModelAdmin):
    form = RepaymentForm
    list_display = ('bank', 'payment_date', 'sum_all', 'payment_sum', 'percents', 'fine')

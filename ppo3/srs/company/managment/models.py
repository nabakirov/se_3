from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User, PermissionsMixin
from django.utils.translation import gettext as _
from managment.config import DBTable
from managment.permissions import Role


class Unit(models.Model):
    class Meta:
        db_table = DBTable.UNIT
        verbose_name = _('unit')
        verbose_name_plural = _('units')

    name = models.CharField(_('name'), max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    class Meta:
        db_table = DBTable.MATERIAL
        verbose_name = _('material')
        verbose_name_plural = _('materials')

    name = models.CharField(_('name'), max_length=50, null=False, unique=True)
    unit = models.ForeignKey('Unit', on_delete=models.PROTECT, null=False, verbose_name=_('unit'))
    summ = models.FloatField(_('sum'), null=False)
    quantity = models.FloatField(_('quantity'), null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        db_table = DBTable.PRODUCT
        verbose_name = _('product')
        verbose_name_plural = _('products')

    name = models.CharField(_('name'), max_length=50, null=False, unique=True)
    unit = models.ForeignKey('Unit', on_delete=models.PROTECT, null=False, verbose_name=_('unit'))
    summ = models.FloatField(_('sum'), null=False)
    quantity = models.FloatField(_('quantity'), null=False)

    def __str__(self):
        return self.name


class Position(models.Model):
    class Meta:
        db_table = DBTable.POSITION
        verbose_name = _('position')
        verbose_name_plural = _('positions')

    name = models.CharField(_('name'), max_length=100, null=False)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone:
            raise ValueError('The given phone must be set')

        user = self.model(phone=phone,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'director')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class Employee(AbstractBaseUser):
    class Meta:
        db_table = DBTable.EMPLOYEE
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
    # user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='employee')
    name = models.CharField(_('name'), max_length=50, null=False, unique=False)
    position = models.ForeignKey('Position', on_delete=models.PROTECT, null=True, blank=True)
    salary = models.FloatField(_('salary'), null=False)
    address = models.CharField(_('address'), max_length=200, null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=100, null=False, unique=True)
    is_staff = models.BooleanField(_('is staff'), default=False)
    is_superuser = models.BooleanField(_('is superuser'), default=False)
    role = models.CharField(max_length=30, choices=(('director', _('director')),
                                                    ('manager', _('manager')),
                                                    ('technologist', _('technologist')),
                                                    ('accountant', _('accountant')),
                                                    ('hr', _('hr'))
                                                    ),
                            null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def has_module_perms(self, *args, **kwargs):
        if self.is_active:
            return True

    def has_perm(self, perm, obj=None):
        if perm in Role.permission_list(self.role):
            return True
        return False

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    class Meta:
        db_table = DBTable.INGREDIENT
        verbose_name = _('ingredient')
        verbose_name_plural = _('ingredients')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=False)
    material = models.ForeignKey('Material', on_delete=models.CASCADE, null=False)
    quantity = models.FloatField(_('quantity'), null=False)


class Budget(models.Model):
    class Meta:
        db_table = DBTable.BUDGET
        verbose_name = _('budget')
        verbose_name_plural = _('budget')

    summ = models.FloatField(_('sum'), null=False)

    def __str__(self):
        return str(self.summ)


class Purchase(models.Model):
    class Meta:
        db_table = DBTable.PURCHASE
        verbose_name = _('purchase')
        verbose_name_plural = _('purchases')
    material = models.ForeignKey('Material', on_delete=models.PROTECT, null=False)
    quantity = models.FloatField(_('quantity'), null=False)
    summ = models.FloatField(_('sum'), null=False)
    time = models.DateTimeField(_('time'), null=False)
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, null=False)


class Sale(models.Model):
    class Meta:
        db_table = DBTable.SALE
        verbose_name = _('sale')
        verbose_name_plural = _('sale')
    product = models.ForeignKey('Product', on_delete=models.PROTECT, null=False)
    quantity = models.FloatField(_('quantity'), null=False)
    summ = models.FloatField(_('sum'), null=False)
    time = models.DateTimeField(_('time'), null=False)
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, null=False)


class Production(models.Model):
    class Meta:
        db_table = DBTable.PRODUCTION
        verbose_name = _('production')
        verbose_name_plural = _('production')

    product = models.ForeignKey('Product', on_delete=models.PROTECT, null=False)
    quantity = models.FloatField(_('quantity'), null=False)
    time = models.DateTimeField(_('time'), null=False)
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, null=False)


class Payroll(models.Model):
    class Meta:
        db_table = DBTable.PAYROLL
        verbose_name = _('payroll')
        verbose_name_plural = _('payroll')

    employee = models.ForeignKey('Employee', on_delete=models.PROTECT)
    year = models.IntegerField(_('year'), null=False)
    month = models.IntegerField(_('month'), null=False)
    date = models.DateField(_('date'), null=False)
    salary = models.FloatField(_('salary'), null=False)
    prize = models.FloatField(_('prize'), null=False)

    @property
    def summ(self):
        return self.salary + self.prize


class Credit(models.Model):
    class Meta:
        db_table = DBTable.CREDIT
    bank = models.CharField(_('bank'), max_length=50, null=False)
    date_of_issue = models.DateField()
    fine = models.FloatField()
    percent = models.FloatField()
    sum = models.FloatField()
    year = models.FloatField()
    redeemed = models.FloatField()

    def __str__(self):
        return self.bank


class Repayment(models.Model):
    class Meta:
        db_table = DBTable.REPAYMENT
    bank = models.ForeignKey('Credit', on_delete=models.PROTECT, related_name='repayments')
    payment_date = models.DateField(_('date'))
    sum_all = models.FloatField(null=True, blank=True)
    payment_sum = models.FloatField(_('sum'), null=True, blank=True)
    percents = models.FloatField(null=True, blank=True)
    fine = models.FloatField(null=True, blank=True)


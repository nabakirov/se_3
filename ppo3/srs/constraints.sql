use company 
go

create trigger new_purchase on purchase INSTEAD OF INSERT as 
    declare @summ float
    declare @material_id int
    declare @quantity float
    declare @time datetime
    declare @employee_id int

    select @summ = summ from inserted
    select @material_id = material_id from inserted
    select @quantity = quantity from inserted
    select @time = [time] from inserted
    select @employee_id = employee_id from inserted


    if @summ > (select summ from budget where id = 0)
		raiserror('there is not enought sum in budget', 16, 9);
	else
        insert into purchase(material_id, quantity, summ, [time], employee_id) 
			values(@material_id, @quantity, @summ, @time, @employee_id)

        update material 
        set material.summ += @summ,
            material.quantity += @quantity
        where material.id = @material_id

		update budget set summ -= @summ where budget.id = 0;
        
go


create trigger new_sale on sale instead of insert as
    declare @product_id int
    declare @quantity float
    declare @summ float
    declare @time datetime
    declare @employee_id int
	declare @sale_summ float
	declare @total_summ float

    select @product_id = product_id from inserted
    select @quantity = quantity from inserted
    select @summ = (select (p.summ / p.quantity) * @quantity from product p where id = @product_id )
	select @sale_summ = (select @summ * (select sale_percent from budget where id = 0) / 100)
    select @time = [time] from inserted
    select @employee_id = employee_id from inserted
	set @total_summ = @summ + @sale_summ

    if @quantity > (select quantity from product where id = @product_id)
		raiserror('there is not enought products', 16, 9);
	else
        insert into sale(product_id, quantity, summ, [time], employee_id)
            values(@product_id, @quantity, @total_summ, @time, @employee_id);

        update product set
            product.summ -= @summ,
            product.quantity -= @quantity
        where product.id = @product_id;

        update budget set budget.summ += @total_summ where budget.id = 0;
        
go

create trigger new_production on production instead of insert as
    declare @product_id int
    declare @quantity float
    declare @time datetime
    declare @employee_id int


    select @product_id = product_id from inserted
    select @quantity = quantity from inserted
    select @time = [time] from inserted
    select @employee_id = employee_id from inserted

    

    declare @material_exist int
    declare @material_need int
    declare @summ float = 0

    select @material_exist = (
        select count(i.material_id)
        from ingredient as i
        inner join material as m
        on i.material_id = m.id
        where i.product_id = @product_id and m.quantity >= i.quantity * @quantity)
    
    select @material_need = (
        select count(i.material_id)
        from ingredient as i
        where i.product_id = @product_id
    )
    
    select @summ = (
        select sum(i.quantity * @quantity * (m.summ / m.quantity))
        from ingredient i
        join material m
        on i.material_id = m.id
        where i.product_id = @product_id and m.quantity >= i.quantity * @quantity
    )


    if @material_exist < @material_need
        raiserror('not enought materials', 16, 9);
    else
        update material
        set 
            quantity = (m.quantity - i.quantity * @quantity),
            summ = (m.summ - (i.quantity * @quantity * (m.summ / m.quantity)))
        from 
            material m
            join ingredient i on i.material_id = m.id
        
        update
            product 
        set 
            quantity = (p.quantity + @quantity),
            summ = p.summ + @summ
        from 
            product p
        where id = @product_id
		
		insert into production(product_id, quantity, [time], employee_id)
		values (@product_id, @quantity, @time, @employee_id)

CREATE TRIGGER [dbo].[payroll_insert]
ON [dbo].[payroll]
instead of insert
AS
Begin
 declare @employee_id int
 declare @year int
 declare @month int
 declare @salary float
 declare @prize float
 declare @action_count int =0
 declare @prize_percent float
 declare @budget_sum float
 declare @date_ date

 set @date_ = (select date from inserted)
 set @year = year(@date_)
 set @month = month(@date_)
 set @employee_id = (select employee_id from inserted)
 set @salary = (select salary from employee where id=@employee_id)
 set @prize_percent = (select prize_percent from budget where id = 0)
 set @action_count += (select count(employee_id) from production where employee_id=@employee_id and year([time])=@year and month([time])=@month)
 set @action_count += (select count(employee_id) from purchase where employee_id=@employee_id and year([time])=@year and month([time])=@month)
 set @action_count += (select count(employee_id) from sale where employee_id=@employee_id and year([time])=@year and month([time])=@month)
 set @prize = @action_count * ((@salary*@prize_percent)/100)
 set @budget_sum = (select summ from budget where id = 0)

 if (@salary + @prize <= @budget_sum) begin
 	insert into payroll (employee_id, year, month, [date], salary, prize) values (@employee_id, @year, @month, @date_, @salary, @prize)
 	update budget set summ -= (@salary + @prize)
 	end
 else begin
  raiserror ('Budget is not enough',16,1)
  rollback
 end
end
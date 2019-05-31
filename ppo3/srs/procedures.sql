use company
go

create procedure get_budget as
	select summ as budget_summ from budget where id = 0;

create procedure material_by_product @material_id DEC(5,3) as 
	select m.id as material_id, m.name as material_name, i.quantity as quantity_need, m.quantity as quantity_exist, m.summ as product_summ as
	from material as m
	inner join ingredient as i on i.material_id = m.id
	where i.product_id = @material_id;


create procedure get_data @product_id DEC(5,3) as 
	select 
		m.id as material_id, 
		m.name as material_name, 
		i.quantity as quantity_need, 
		m.quantity as quantity_exist, 
		m.summ as material_summ, 
		b.summ as budget_summ,
		p.summ as product_summ,
		p.quantity as product_quantity
	from material as m
	inner join ingredient as i on i.material_id = m.id
	inner join budget as b on b.id = 0
	inner join product as p on p.id = @product_id
	where i.product_id = @product_id;


create procedure make_product @product_id DEC(5,3), @quantity DEC(5,3), @employee_id DEC(5,3) as
	insert into production (product_id, quantity, employee_id, time)
		values (@product_id, @quantity, @employee_id, getdate())

create procedure sale_product @product_id DEC(5,3), @quantity DEC(5,3), @employee_id DEC(5,3) as
	insert into sale (product_id, quantity, employee_id, time)
		values (@product_id, @quantity, @employee_id, getdate())

create procedure make_purchase @material_id DEC(5,3), @quantity DEC(5,3), @employee_id DEC(5,3), @summ DEC(5,3) as
	insert into purchase (material_id, quantity, employee_id, time, summ)
		values (@material_id, @quantity, @employee_id, getdate(), @summ)

create procedure materials_enough @product_id int, @quantity float, 
@result int OUTPUT as
	declare @material_exist int
	declare @material_need int
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
	if (@material_exist < @material_need) 
		begin
			set @result = 0
			return
		end
	else 
		begin
			set @result = 1
			return
		end

create procedure payroll_check @employee_id int, @date_ date, @result int output as
 declare @year int
 declare @month int
 declare @salary float
 declare @prize float
 declare @action_count int =0
 declare @prize_percent float
 declare @budget_sum float

 set @year = year(@date_)
 set @month = month(@date_)
 set @salary = (select salary from employee where id=@employee_id)
 set @prize_percent = (select prize_percent from budget where id = 0)
 set @action_count += (select count(employee_id) from production where employee_id=@employee_id and year([time])=@year and month([time])=@month)
 set @action_count += (select count(employee_id) from purchase where employee_id=@employee_id and year([time])=@year and month([time])=@month)
 set @action_count += (select count(employee_id) from sale where employee_id=@employee_id and year([time])=@year and month([time])=@month)
 set @prize = @action_count * ((@salary*@prize_percent)/100)
 set @budget_sum = (select summ from budget where id = 0)
 set @salary += @prize
 
 if (@budget_sum < @salary) begin
	set @result = 1
	return
 end

 if @employee_id in (select employee_id from payroll where employee_id=@employee_id and year = @year and month = @month) begin
	set @result = 2
	return
 end

 set @result = 0
 return





create procedure payroll_data @employee_id int, @date_ date as
	select 
		e.salary as salary, 
		(select count(employee_id) from production where employee_id=@employee_id and year([time])=year(@date_) and month([time])=month(@date_)) as production_action_count,
		(select count(employee_id) from sale where employee_id=@employee_id and year([time])=year(@date_) and month([time])=month(@date_)) as sale_action_count,
		(select count(employee_id) from purchase where employee_id=@employee_id and year([time])=year(@date_) and month([time])=month(@date_)) as purchase_action_count,
		(select prize_percent from budget where id = 0) as prize_percent
		
	from employee as e 
	where e.id = @employee_id
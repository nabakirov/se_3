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

    select @product_id = product_id from inserted
    select @quantity = quantity from inserted
    select @summ = summ from inserted
    select @time = [time] from inserted
    select @employee_id = employee_id from inserted

    if @quantity > (select quantity from product where id = @product_id)
		raiserror('there is not enought products', 16, 9);
	else
        insert into sale(product_id, quantity, summ, [time], employee_id)
            values(@product_id, @quantity, @summ, @time, @employee_id);

        update product set
            product.summ -= @summ,
            product.quantity -= @quantity
        where product.id = @product_id;

        update budget set budget.summ += @summ where budget.id = 0;
        
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
        select sum(i.quantity * 1 * (m.summ / m.quantity))
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




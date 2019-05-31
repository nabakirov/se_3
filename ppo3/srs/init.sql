create database company
go

use company
go

create table unit(
    id int identity(0,1) not null primary key,
    [name] varchar(50) not null unique
);

create table material(
    id int identity(0,1) not null primary key,
    [name] varchar(50) not null unique,
    unit_id int not null,
    summ float not null,
    quantity float not null,

    CONSTRAINT fk_material_unit_id
		FOREIGN KEY(unit_id) 
		REFERENCES unit(id)
);

create table product(
    id int identity(0,1) not null primary key,
    [name] varchar(50) not null unique,
    unit_id int not null,
    summ float not null,
    quantity float not null,

    CONSTRAINT fk_product_unit_id
		FOREIGN KEY(unit_id) 
		REFERENCES unit(id)
);

create table position(
    id int identity(0,1) not null primary key,
    [name] varchar(50) not null unique
);

create table employee(
    id int identity(0, 1) not null primary key,
    [name] varchar(100) not null,
    position_id int not null,
    salary float null,
    [address] varchar(200) null,
    phone varchar(100) null,

    CONSTRAINT fk_employee_position_id
		FOREIGN KEY(position_id) 
		REFERENCES position(id)
);


create table ingredient(
    id int identity(0, 1) not null primary key,
    product_id int not null,
    material_id int not null,
    quantity float not null,

    CONSTRAINT fk_ingredient_product_id
		FOREIGN KEY(product_id) 
		REFERENCES product(id)
		ON DELETE CASCADE,
    CONSTRAINT fk_ingredient_material_id
		FOREIGN KEY(material_id) 
		REFERENCES material(id)
		ON DELETE CASCADE
);

create table budget(
    id int identity(0,1) not null primary key,
    summ float not null
);

create table purchase(
    id int identity(0,1) not null primary key,
    material_id int null,
    quantity float not null,
    summ float not null,
    [time] datetime not null,
    employee_id int not null,

    CONSTRAINT fk_purchase_material_id
		FOREIGN KEY(material_id) 
		REFERENCES material(id),
    constraint fk_purchase_employee_id
        foreign key(employee_id)
        references employee(id)
);

create table sale(
    id int identity(0,1) not null primary key,
    product_id int not null,
    quantity float not null,
    summ float null,
    [time] datetime not null,
    employee_id int not null,

    CONSTRAINT fk_sale_product_id
		FOREIGN KEY(product_id) 
		REFERENCES product(id),
    constraint fk_sale_employee_id
        foreign key(employee_id)
        references employee(id)
);

create table production(
    id int identity(0,1) not null primary key,
    product_id int not null,
    quantity float not null,
    [time] datetime not null,
    employee_id int not null,

    CONSTRAINT fk_production_product_id
		FOREIGN KEY(product_id) 
		REFERENCES product(id),
    constraint fk_production_employee_id
        foreign key(employee_id)
        references employee(id)
);


create table credit (
	id int identity(1,1) not null primary key,
	bank nvarchar(50) not null,
	date_of_issue date null,
	fine real null,
	[percent] real null,
	[sum] real null,
	[year] int null,
	redeemed real null
);


create table repayment (
	id int identity(1,1) not null primary key,
	bank int not null,
	payment_date date,
	sum_all real,
	payment_sum real,
	[percents] real,
	fine real,
	CONSTRAINT fk_bank_credit
		FOREIGN KEY(bank) 
		REFERENCES credit(id)
);
	


go
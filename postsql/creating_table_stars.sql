-- Create schema
CREATE SCHEMA IF NOT EXISTS mydb;
SET search_path TO mydb;

-- Table: customer
drop table if exists mydb.customer;
CREATE TABLE IF NOT EXISTS mydb.customer (
  idcustomer Varchar(30) primary key,
  cust_name VARCHAR(30),
  segment varchar(30),
  country varchar(30),
  Region varchar(30)
);

-- Table: products
CREATE TABLE IF NOT EXISTS products (
  product_id VARCHAR(30) primary key,
  category varchar(30),
  sub_category varchar(30),
  product_name varchar(255)
);

drop table if exists mydb.date;
CREATE TABLE IF NOT EXISTS mydb.date (
	date_id varchar(30) primary key,
	Order_date date,
	Ship_date date
);


drop table if exists mydb.location;
CREATE TABLE mydb.location (
	location_id varchar(30) primary key,
	city varchar(30),
	state varchar(30),
	postal_code int
);

drop table if exists mydb.orders;
create table mydb.orders(
	order_id varchar(30) primary key,
	ship_mode varchar(30)
	
);

drop table if exists mydb.transaction_sale;
create table mydb.transaction_sale (
	Row_id int primary key,
	Order_id varchar(30),
	date_id varchar(30),
	cust_id varchar(30),
	location_id varchar(30),
	product_id varchar(20),
	sales float,
	quantity int,
	discount float,
	profit float,
	foreign key (Order_id) references mydb.orders(order_id) on delete no action on update no action,
	foreign key (date_id) references mydb.date(date_id) on delete no action on update no action,
	foreign key (cust_id) references mydb.customer(idcustomer) on delete no action on update no action,
	foreign key (location_id) references mydb.location(location_id) on delete no action on update no action,
	foreign key (product_id) references mydb.products(product_id) on delete no action on update no action
	
);

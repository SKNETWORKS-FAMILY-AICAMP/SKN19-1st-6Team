drop table car_tmp;
create table car_tmp
(	
	vehicle_id int auto_increment primary key,
    fuel_id varchar(300),
    vehicle_model_id varchar(300),
    model varchar(300),
	vehicle_brand varchar(300),
    vehicle_image varchar (1000),
    vehicle_capacity varchar(300),
    max_speed varchar(300),
    driving_range varchar(300),
    vehicle_subsidy varchar(300),
    battery_type varchar(100),
    dealer_contact varchar(100),
    manufacturer varchar(300),
    manufacturing_country varchar(300),
    car_type varchar(300)
) engine=innodb;

select * from car_tmp;
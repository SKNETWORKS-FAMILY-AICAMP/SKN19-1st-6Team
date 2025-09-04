create table IF NOT EXISTS tmp_registration
(
    registration_code int auto_increment primary key comment '등록코드',
    year_month_code varchar(100) comment '연월정보',
    fuel_type varchar(30) NOT NULL comment '연료종류',
    car_type varchar(50) comment '차종',
    region varchar(10) comment '지역명',
    registration_count int comment '등록대수',
    fuel_group VARCHAR(20) NOT NULL comment '연료구분(상위)'


) engine=innodb;

use totaldb;
select * from tmp_registration;
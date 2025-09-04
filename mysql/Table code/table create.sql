use totaldb;
drop table vehicle_type;
drop table car;
-- 연료 테이블
CREATE TABLE fuel_type (
    fuel_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '연료 식별자',
    fuel_category_name VARCHAR(100) NOT NULL COMMENT '연료 카테고리명',
    parent_fuel_id INT DEFAULT NULL COMMENT '상위 연료 식별자',
    CONSTRAINT fk_fuel_parent FOREIGN KEY (parent_fuel_id) REFERENCES fuel_type(fuel_id)
) ENGINE=InnoDB COMMENT='연료 유형';

-- 차량 유형 테이블
CREATE TABLE vehicle_type (
    vehicle_model_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '차량 유형 식별자',
    vehicle_model VARCHAR(100) NOT NULL UNIQUE COMMENT '차량 모델명 (전기승용, 전기화물 등)',
    vehicle_model_detail VARCHAR(100) NOT NULL UNIQUE COMMENT '세부 구분자 (SUV, 세단, 경차 등)'
) ENGINE=InnoDB COMMENT='차량 유형';

CREATE TABLE car (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY COMMENT '차량 식별자',
    fuel_id INT NOT NULL COMMENT '연료 참조키',
    vehicle_model_id INT NOT NULL COMMENT '차량 모델 참조키',
    model VARCHAR(300),
    vehicle_brand VARCHAR(300),
    vehicle_image VARCHAR (1000),
    vehicle_capacity VARCHAR(300),
    max_speed VARCHAR(300),
    driving_range VARCHAR(300),
    vehicle_subsidy VARCHAR(300),
    battery_type VARCHAR(100),
    dealer_contact VARCHAR(100),
    manufacturer VARCHAR(300),
    manufacturing_country VARCHAR(300),
    CONSTRAINT fk_car_fuel FOREIGN KEY (fuel_id) REFERENCES fuel_type(fuel_id),
    CONSTRAINT fk_car_vehicle FOREIGN KEY (vehicle_model_id) REFERENCES vehicle_type(vehicle_model_id)
) ENGINE=InnoDB COMMENT='차량 정보';

create table car_registration
(
    registration_id int auto_increment primary key comment '등록코드',
	fuel_id INT NOT NULL COMMENT '연료 참조키',
    vehicle_model_id INT NOT NULL COMMENT '차량 모델 참조키',
    base_ym varchar(100) comment '연월정보',
    region_name varchar(10) comment '지역명',
    registered_count int comment '등록대수',
	CONSTRAINT fk_car_registration_fuel FOREIGN KEY (fuel_id) REFERENCES fuel_type(fuel_id),
    CONSTRAINT fk_car_registration_vehicle FOREIGN KEY (vehicle_model_id) REFERENCES vehicle_type(vehicle_model_id)
) engine=innodb;
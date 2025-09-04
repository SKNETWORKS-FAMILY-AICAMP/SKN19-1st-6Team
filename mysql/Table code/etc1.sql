
-- 중복 제거 후 vehicle_type 테이블에 삽입
INSERT INTO vehicle_type (vehicle_model, vehicle_model_detail)
SELECT DISTINCT vehicle_model_id, car_type
FROM car_tmp
WHERE vehicle_model_id IS NOT NULL AND car_type IS NOT NULL;

-- MySQL 8.0 이상
INSERT INTO car (
    fuel_id,
    vehicle_model_id,
    model,
    vehicle_brand,
    vehicle_image,
    vehicle_capacity,
    max_speed,
    driving_range,
    vehicle_subsidy,
    battery_type,
    dealer_contact,
    manufacturer,
    manufacturing_country
)
SELECT 
    ft.fuel_id,
    vt.vehicle_model_id,
    ct.model,
    ct.vehicle_brand,
    ct.vehicle_image,
    ct.vehicle_capacity,
    ct.max_speed,
    ct.driving_range,
    ct.vehicle_subsidy,
    ct.battery_type,
    ct.dealer_contact,
    ct.manufacturer,
    ct.manufacturing_country
FROM car_tmp ct
JOIN (
    SELECT DISTINCT vehicle_model_id, car_type FROM car_tmp
) tmp ON ct.vehicle_model_id = tmp.vehicle_model_id AND ct.car_type = tmp.car_type
JOIN vehicle_type vt ON vt.vehicle_model = tmp.vehicle_model_id AND vt.vehicle_model_detail = tmp.car_type
JOIN (
    SELECT 
        fuel_id,
        fuel_category_name
    FROM fuel_type
) ft ON SUBSTRING(ct.vehicle_model_id, 1, 2) = SUBSTRING(ft.fuel_category_name, 1, 2);


use totaldb;
select * from fuel_type;
select * from vehicle_type;
select * from car;

update car_tmp
set car_type = 'NULL'
where vehicle_id in (174,175,176,177);
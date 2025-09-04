SELECT DISTINCT fuel_type FROM tmp_registration;
SELECT DISTINCT car_type FROM tmp_registration;
SELECT * FROM fuel_type;

SELECT DISTINCT tr.fuel_type
FROM tmp_registration tr
LEFT JOIN fuel_type ft
  ON tr.fuel_type = ft.fuel_category_name
    OR (tr.fuel_type = '엘피지' AND ft.fuel_category_name = 'LPG')
WHERE ft.fuel_id IS NULL;

SELECT DISTINCT tr.car_type
FROM tmp_registration tr
LEFT JOIN vehicle_type vt
  ON tr.car_type = vt.vehicle_model
WHERE vt.vehicle_model_id IS NULL;

SELECT COUNT(*) FROM tmp_registration;

SELECT COUNT(*)
FROM tmp_registration tr
JOIN fuel_type ft ON (tr.fuel_type = ft.fuel_category_name OR (tr.fuel_type = '엘피지' AND ft.fuel_category_name = 'LPG'))
JOIN vehicle_type vt ON tr.car_type = vt.vehicle_model AND (vt.vehicle_model_detail IS NULL OR vt.vehicle_model_detail = '');
SELECT COUNT(*)
FROM tmp_registration tr
JOIN fuel_type ft ON (tr.fuel_type = ft.fuel_category_name OR (tr.fuel_type = '엘피지' AND ft.fuel_category_name = 'LPG'))
JOIN vehicle_type vt ON tr.car_type = vt.vehicle_model;

SELECT DISTINCT tr.fuel_type
FROM tmp_registration tr
LEFT JOIN fuel_type ft ON tr.fuel_type = ft.fuel_category_name
WHERE ft.fuel_id IS NULL;

UPDATE tmp_registration
SET fuel_type = 'LPG'
WHERE fuel_type = '엘피지'
and registration_code > 0;



SELECT COUNT(*)
FROM tmp_registration tr
JOIN fuel_type ft ON (tr.fuel_type = ft.fuel_category_name OR (tr.fuel_type = '엘피지' AND ft.fuel_category_name = 'LPG'))
JOIN vehicle_type vt ON tr.car_type = vt.vehicle_model;


INSERT INTO car_registration (
    fuel_id,
    vehicle_model_id,
    base_ym,
    region_name,
    registered_count
)
SELECT
    ft.fuel_id,
    vt.vehicle_model_id,
    tr.year_month_code,
    tr.region,
    tr.registration_count
FROM tmp_registration tr
JOIN fuel_type ft ON tr.fuel_type = ft.fuel_category_name
JOIN vehicle_type vt ON tr.car_type = vt.vehicle_model;

drop table tmp_registration;
drop table car_registration;


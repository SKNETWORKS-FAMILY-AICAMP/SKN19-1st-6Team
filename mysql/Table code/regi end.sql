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
JOIN vehicle_type vt ON tr.car_type = vt.vehicle_model
    AND vt.vehicle_model_detail = 'NULL';

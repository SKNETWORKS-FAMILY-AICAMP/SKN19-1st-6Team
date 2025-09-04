INSERT INTO fuel_type (fuel_category_name, parent_fuel_id)
VALUES 
('전기',NULL),
('수소',NULL),
('하이브리드', NULL),
('화석연료', NULL),
('기타연료', NULL);

-- 화석연료의 하위 연료
INSERT INTO fuel_type (fuel_category_name, parent_fuel_id)
VALUES 
('휘발유', 4),
('경유', 4),
('등유', 4),
('LNG', 4),
('CNG', 4),
('LPG', 4);

-- 수소의 하위 연료
INSERT INTO fuel_type (fuel_category_name, parent_fuel_id)
VALUES 
('수소전기', 2);

-- 하이브리드의 하위 연료
INSERT INTO fuel_type (fuel_category_name, parent_fuel_id)
VALUES 
('하이브리드(휘발유+전기)', 3),
('하이브리드(경유+전기)', 3),
('하이브리드(LPG+전기)', 3),
('하이브리드(LNG+전기)', 3),
('하이브리드(CNG+전기)', 3);

-- 기타연료의 하위 연료
INSERT INTO fuel_type (fuel_category_name, parent_fuel_id)
VALUES 
('태양열', 5),
('알코올', 5);

SELECT 
    SUBSTRING(vehicle_model, 3) AS trimmed_model,
    IFNULL(vehicle_model_detail, '') AS detail,
    COUNT(*) AS cnt,
    GROUP_CONCAT(vehicle_model_id) AS ids
FROM vehicle_type
GROUP BY trimmed_model, detail
HAVING cnt > 1;


UPDATE vehicle_type
SET vehicle_model = SUBSTRING(vehicle_model, 3)
WHERE vehicle_model LIKE '전기%' OR vehicle_model LIKE '수소%';


UPDATE car
SET vehicle_model_id = 2
WHERE vehicle_model_id = 8;
DELETE FROM vehicle_type
WHERE vehicle_model_id = 8;



-- 먼저 기존 제약 조건 삭제
ALTER TABLE vehicle_type DROP INDEX vehicle_model;
ALTER TABLE vehicle_type DROP INDEX vehicle_model_detail;

-- 복합 유니크 키로 설정
ALTER TABLE vehicle_type ADD UNIQUE KEY uniq_vehicle_model_combination (vehicle_model, vehicle_model_detail);


UPDATE vehicle_type
SET vehicle_model_detail = ''
WHERE vehicle_model_detail IS NULL;

SELECT
    SUBSTRING(vehicle_model, 3) AS trimmed_model,
    vehicle_model_detail,
    GROUP_CONCAT(vehicle_model_id) AS ids,
    COUNT(*) AS cnt
FROM vehicle_type
GROUP BY trimmed_model, vehicle_model_detail
HAVING cnt > 1;

UPDATE car
SET vehicle_model_id = 5
WHERE vehicle_model_id = 9;

DELETE FROM vehicle_type
WHERE vehicle_model_id = 9;

UPDATE vehicle_type
SET vehicle_model = SUBSTRING(vehicle_model, 3)
WHERE vehicle_model LIKE '전기%' OR vehicle_model LIKE '수소%';


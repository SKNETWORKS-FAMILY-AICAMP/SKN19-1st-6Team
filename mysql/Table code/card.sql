DROP TABLE IF EXISTS CARD_INFO CASCADE;
DROP TABLE IF EXISTS CARD_CODE CASCADE;
DROP TABLE IF EXISTS CARD_CATEGORY_CODE CASCADE;

CREATE TABLE IF NOT EXISTS CARD_CODE
(
    card_company_id INT AUTO_INCREMENT NOT NULL COMMENT '카드사코드',    
    card_company_name VARCHAR(30) NOT NULL COMMENT '카드사명',
    CONSTRAINT pk_card_company_id PRIMARY KEY (card_company_id)
) ENGINE=INNODB COMMENT '카드사 코드 관리';

-- CREATE TABLE IF NOT EXISTS CARD_CATEGORY_CODE
-- (
--     card_category_id INT AUTO_INCREMENT COMMENT '카테고리코드',    
--     card_category_name VARCHAR(30) NOT NULL COMMENT '카테고리명',
--     card_parent_category_id INT COMMENT '상위카테고리코드',
--     CONSTRAINT pk_card_category_id PRIMARY KEY (card_category_id),
--     CONSTRAINT fk_card_parent_category_id FOREIGN KEY (card_parent_category_id) REFERENCES CARD_CATEGORY_CODE (card_category_id)
-- ) ENGINE=INNODB COMMENT '카드 혜택 카테고리 관리';

CREATE TABLE IF NOT EXISTS CARD_INFO
(
    card_id    				INT AUTO_INCREMENT NOT NULL COMMENT '카드코드',
    card_name    			VARCHAR(100) NOT NULL COMMENT '카드이름',
    card_image   			VARCHAR(100) COMMENT '카드이미지경로',
    card_type  				VARCHAR(10) COMMENT '카드타입',
    card_category_name		VARCHAR(100) COMMENT '카테고리명', 
	card_detail				VARCHAR(500) COMMENT '혜택내용',
    card_detail_url 		VARCHAR(100) COMMENT '카드내용URL',
    card_company_id 		INT NOT NULL COMMENT '카드사코드',    
    CONSTRAINT pk_card_id 	PRIMARY KEY (card_id),
    CONSTRAINT fk_card_company_id FOREIGN KEY (card_company_id) REFERENCES CARD_CODE (card_company_id)
) ENGINE=INNODB COMMENT '친환경 카드 정보';

-- CREATE TABLE IF NOT EXISTS CARD_INFO
-- (
--     card_id    		INT AUTO_INCREMENT NOT NULL COMMENT '카드코드',
--     card_name    	VARCHAR(100) NOT NULL COMMENT '카드이름',
--     card_image   	VARCHAR(100) COMMENT '카드이미지경로',
--     card_type  		VARCHAR(10) COMMENT '카드타입',
--     vehicle_model   VARCHAR(30) COMMENT '차종',
-- 	card_detail		VARCHAR(500) COMMENT '혜택내용',
--     card_detail_url VARCHAR(100) COMMENT '카드내용URL',
--     card_company_id 	INT NOT NULL COMMENT '카드사코드',    
--     card_category_id	INT NOT NULL COMMENT '카테고리코드',    
--     CONSTRAINT pk_card_id PRIMARY KEY (card_id),
--     CONSTRAINT fk_card_company_id FOREIGN KEY (card_company_id) REFERENCES CARD_CODE (card_company_id),
--     CONSTRAINT fk_card_category_id FOREIGN KEY (card_category_id) REFERENCES CARD_CATEGORY_CODE (card_category_id)
-- ) ENGINE=INNODB COMMENT '친환경 카드 정보';

CREATE TABLE IF NOT EXISTS eco_card_summary
(
    card_id    				INT AUTO_INCREMENT NOT NULL COMMENT '카드코드',
    card_company_name		VARCHAR(30) NOT NULL COMMENT '카드사명',
    card_name    			VARCHAR(100) NOT NULL COMMENT '카드이름',
    card_image   			VARCHAR(100) COMMENT '카드이미지경로',
    card_type  				VARCHAR(10) COMMENT '카드타입',
	charging_discount_yn	VARCHAR(2) COMMENT '충전요금할인', 
    transport_discount_yn  	VARCHAR(2) COMMENT '교통할인', 
    maintenance_service_yn	VARCHAR(2) COMMENT '정비서비스', 
    auto_insurance_yn		VARCHAR(2) COMMENT '자동차보험', 
    vehicle_etc_yn			VARCHAR(2) COMMENT '차량기타', 
    card_type_elec_yn		VARCHAR(2) COMMENT '전기차', 
    card_type_suso_yn		VARCHAR(2) COMMENT '수소차',     
	card_detail				VARCHAR(500) COMMENT '혜택내용',
    card_detail_url 		VARCHAR(100) COMMENT '카드내용URL',
    CONSTRAINT pk_card_id 	PRIMARY KEY (card_id)
) ENGINE=INNODB COMMENT '친환경 카드 집계 정보';

select * from card_code;
select * from card_info;
select * from eco_card_summary;
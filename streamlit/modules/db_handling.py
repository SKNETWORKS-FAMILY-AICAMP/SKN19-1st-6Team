import mysql.connector
from modules.environment import env
import pandas as pd

def get_conn():
    connection = mysql.connector.connect(
        host = env.get("MYSQL_HOST"),         
        user = env.get("MYSQL_USER"),      
        password = env.get("MYSQL_PASSWORD"),      
        database = env.get("MYSQL_DB"),    
    )
    return connection

def get_data(data, values=None):
    
    # faq 화면
    faq_sql = """
    select * from faq
    """
    # 자동차 화면
    car_sql = """
        SELECT 
        c.registration_id as registration_code, 
        c.base_ym as year_month_code,
        f.child_name AS fuel_type,  -- 소분류 (항상 자식)
        COALESCE(f.parent_name, f.child_name) AS fuel_group,  -- 대분류
        v.vehicle_model as car_type,
        c.region_name as region,
        c.registered_count as registration_count
    FROM 
        car_registration AS c

    -- fuel_type self join
    JOIN (
        SELECT 
            child.fuel_id,
            child.fuel_category_name AS child_name,
            child.parent_fuel_id,
            parent.fuel_category_name AS parent_name
        FROM 
            fuel_type AS child
        LEFT JOIN 
            fuel_type AS parent
        ON 
            child.parent_fuel_id = parent.fuel_id
    ) AS f
    ON c.fuel_id = f.fuel_id

    -- 차량 모델 정보 조인
    JOIN vehicle_type AS v 
    ON c.vehicle_model_id = v.vehicle_model_id;
    """
    # 보조금 화면
    benefit_sql = """
    SELECT c.vehicle_id, c.model, c.vehicle_brand, f.fuel_category_name, v.vehicle_model, v.vehicle_model_detail, c.vehicle_image, c.vehicle_capacity, c.max_speed, c.driving_range, c.vehicle_subsidy, c.battery_type, c.dealer_contact, c.manufacturer, c.manufacturing_country
    FROM car as c
    JOIN fuel_type as F ON c.fuel_id = f.fuel_id
    JOIN vehicle_type as V ON c.vehicle_model_id = v.vehicle_model_id
    WHERE c.vehicle_subsidy !='NULL';
    """
    # 카드 화면
    card_sql = """
    SELECT * FROM eco_card_summary
    """

    if data=='faq' : query=faq_sql
    if data=='car' : query=car_sql
    if data=='benefit' : query=benefit_sql
    if data=='card' : query=card_sql

    with get_conn() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(query, values)
                rows = cur.fetchall()
                columns = [col[0] for col in cur.description]
                df = pd.DataFrame(rows, columns=columns)
                return df
            except:
                return pd.DataFrame({0:['쿼리 오류가 있습니다.']})
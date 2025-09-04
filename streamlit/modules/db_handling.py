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
    /*조회할 테이블 쿼리*/
    """
    # 자동차 화면
    car_sql = """
    /*조회할 테이블 쿼리*/
    """
    # 보조금 화면
    benefit_sql = """
    /*조회할 테이블 쿼리*/
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
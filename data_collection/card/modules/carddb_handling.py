import mysql.connector
from modules.environment import env

def get_conn():
    connection = mysql.connector.connect(
        host = env.get("MYSQL_HOST"),         
        user = env.get("MYSQL_USER"),      
        password = env.get("MYSQL_PASSWORD"),      
        database = env.get("MYSQL_DB"),    
    )
    return connection

def mydb_read(query, values=None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, values)
            return cur.fetchall()

def mydb_edit(query, values=None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, values)
            conn.commit()

# query = """
# SELECT * FROM card_code
# """

# print(mydb_read(query))
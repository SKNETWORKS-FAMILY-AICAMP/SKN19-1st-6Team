import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / "mysql.env"
load_dotenv(dotenv_path=env_path)
  
env = {
    "MYSQL_HOST": os.getenv("MYSQL_HOST"),    
    "MYSQL_USER": os.getenv("MYSQL_USER"),
    "MYSQL_PASSWORD": os.getenv("MYSQL_PASSWORD"),  
    "MYSQL_DB": os.getenv("MYSQL_DB"),
    "NAVER_CLIENT_ID": os.getenv("NAVER_CLIENT_ID"),
    "NAVER_CLIENT_PW": os.getenv("NAVER_CLIENT_PW"),
}



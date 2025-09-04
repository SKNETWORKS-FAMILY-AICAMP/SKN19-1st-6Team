import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlretrieve

import mysql.connector

connection = mysql.connector.connect(
host="localhost",
user="ohgiraffers",
password="ohgiraffers",
database="faqdb"
)

if connection.is_connected():
    print("MySQL에 성공적으로 연결되었습니다!")

# SQL 수행을 위한 커서 생성
cursor = connection.cursor()


# 1. request -> url 요청
keyword = ['전기', '전기차', '충전', '보조', '카드', '혜택', '정비', '수리', '배터리', '방전', '고전압', '인프라']
cp = ['hyundai', 'kia']
for c in cp:
    for key in keyword:
        file_path = f"C:/Users/Playdata/Documents/GitHub/SKN_19/00_project/01/{c}_{key}.html"
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()
            
        # 2. BeautifulSoup 객체 생성
        bs = BeautifulSoup(html, 'html.parser')

        # 3. 요소
        elec_list = bs.select('.cmp-accordion__item')

        title_list = []
        for elec in elec_list:
            title = elec.select_one(".cmp-accordion__title").text
            answer = elec.select(".cmp-accordion__panel p")
            tmp = ''
            for i in answer:
                tmp += i.text
            title_list.append((title, tmp))
            
        for q in title_list:
            sql = "INSERT INTO faq_id_tb (question, answer, keyword, company) VALUES (%s, %s, %s, %s)"
            values = (q[0], q[1], key, c)
            cursor.execute(sql, values)
            connection.commit()


cursor.close()
connection.close()
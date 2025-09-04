import mysql.connector
import csv

connection = mysql.connector.connect(
    host = 'localhost',  
    user = 'ohgiraffers',
    password = 'ohgiraffers',
    database = 'car_registration'
)

cursor = connection.cursor()

sql = "insert into tbl_registration(year_month_code, fuel_type, car_type, region, registration_count, fuel_group) " \
"values (%s, %s, %s, %s, %s, %s)"  

for year in range(2020, 2025 + 1):
    for month in range(1,8,6):
        if year == 2025 and month > 7:
            break
        if month <= 9:
            month = '0' + str(month)
        
        file_name = f"{year}{month}.csv"
        f = open(file_name, 'r')
        reader = csv.reader(f)
        next(reader)

        fuel_group = ''
        values = ''

        # values 지정
        for line in reader:
            if line[0] in ['휘발유', '경유', '엘피지'] :
                fuel_group = '내연기관'
            elif line[0] in ['CNG', 'LNG']:
                fuel_group = '천연가스'
            elif '하이브리드' in line[0]:
                fuel_group = '하이브리드'
            elif '수소' in line[0]:
                fuel_group = '수소'
            elif line[0] == '전기':
                fuel_group = '전기'
            else :
                fuel_group = '기타연료'
            
            values = (f"{year}{month}", line[0], line[1], line[2], line[3], fuel_group)
            cursor.execute(sql, values)

        f.close() 




print(f"{cursor.rowcount}개의 행을 삽입했습니다.") 

connection.commit()

cursor.close()
connection.close()
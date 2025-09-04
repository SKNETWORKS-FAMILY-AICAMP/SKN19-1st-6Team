from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import mysql.connector
from urllib.request import urlretrieve
from datetime import datetime
import os

def ErrorHandle(lst):
    length = len(lst)
    car_people = 'NULL'
    car_maxspeed = 'NULL'
    car_range = 'NULL'
    car_battery = 'NULL'
    money = 'NULL'
    phone = 'NULL'
    made = 'NULL'
    made_nation = 'NULL'
    for l in lst:
        i = l.text.split(':')[0]
        i = i.replace('-','')
        i = i.replace(' ','')
        if i == '승차인원':
            car_people = l.text.split(':')[1]
        if i == '최고속도출력':
            car_maxspeed = l.text.split(':')[1]
        if i == '1회충전주행거리':
            car_range = l.text.split(':')[1]
        if i == '배터리':
            car_battery = l.text.split(':')[1]
        if i == '국고보조금':
            money = l.text.split(':')[1]
            money = money.replace("만원", "")
            money = money.replace(",", "")
        if i == '판매사연락처':
            phone = l.text.split(':')[1]
        if i == '제조사':
            made = l.text.split(':')[1]
        if i == '제조국가':
            made_nation = l.text.split(':')[1]
    if length<8:
        return car_people, car_maxspeed, car_range, car_battery, money, phone, made, made_nation
    else:
        return car_people, car_maxspeed, car_range, car_battery, money, phone, made, made_nation

connection = mysql.connector.connect(
    host="localhost", user="ohgiraffers", password="ohgiraffers", database="cardb"
)
cursor = connection.cursor()
sql = "INSERT INTO ev_car (car_fuel, car_detail, car_name, car_company, car_img, car_people, car_maxspeed, car_range, car_battery, money, phone, made, made_nation) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

path = "chromedriver.exe"
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

driver.get("https://ev.or.kr/nportal/buySupprt/initSubsidyTargetVehicleAction.do")
driver.execute_script("""
var header = document.querySelector('#header');
if (header) {
    header.style.display = 'none';
}
""")
idx=0
time.sleep(2)
car_sel_1=['vt01','vt02','vt03']
car_selection = ['ev','h2','ce']
car_detail_dict={'ev':['ev01','ev02','ev03','ev04'],'h2':['h201','h202','h203','h204'],'ce':['ce01','ce02']}
detail_dict={'ev01':'전기승용','ev02':'전기화물','ev03':'전기승합','ev04':'전기이륜','h201':'수소승용','h202':'수소화물','h203':'수소승합','h204':'수소특수','ce01':'전기굴착기','ce02':'수소지게차'}
for sel1, selec in zip(car_sel_1,car_selection):
    label = driver.find_element(By.CSS_SELECTOR, f'label[for="{sel1}"]')
    label.click()
    time.sleep(1)
    for de in car_detail_dict[selec]:
        detail=driver.find_element(By.CSS_SELECTOR,f'label[for="{de}"]')
        detail.click()
        time.sleep(1)
        selections = driver.find_element(By.XPATH, '//*[@id="schCompany"]')
        options = selections.find_elements(By.CSS_SELECTOR, "option")
        for op in options:
            selections = driver.find_element(By.XPATH, '//*[@id="schCompany"]')
            select = Select(selections)
            select.select_by_visible_text(op.text)
            time.sleep(1)
            sel_button = driver.find_element(
                By.XPATH, '//*[@id="searchForm"]/div/table/tbody/tr[5]/td/button'
            )
            driver.execute_script("arguments[0].click();", sel_button)
            time.sleep(1)
            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.END)
            end_button = driver.find_element(By.CSS_SELECTOR, ".last.arrow")
            driver.execute_script("arguments[0].click();", end_button)
            time.sleep(1)
            end_page = driver.find_element(By.CSS_SELECTOR, "a.current").text
            print(f"{op.text}:{end_page}")
            for page in range(int(end_page), 0, -1):
                info_boxs = driver.find_elements(By.CLASS_NAME, "infoBox")
                for car in info_boxs:
                    car_company = car.find_element(By.CSS_SELECTOR, "span").text
                    car_name = car.find_element(By.CSS_SELECTOR, "p").text
                    car_img = car.find_element(By.CSS_SELECTOR,'img')
                    img_dir = "car_images"
                    os.makedirs(img_dir, exist_ok=True)
                    file_name = datetime.now().strftime('%y%m%d_%H%M%S')+str(idx)+'.png'
                    idx+=1
                    img_path=f"{img_dir}/{file_name}"
                    driver.execute_script("arguments[0].scrollIntoView();", car_img)
                    time.sleep(0.5)
                    car_img.screenshot(img_path)
                    car_elem = car.find_elements(By.CSS_SELECTOR,'dd')
                    eh=ErrorHandle(car_elem)
                    values = (selec,detail_dict[de],car_name, car_company, img_path, eh[0], eh[1], eh[2], eh[3], eh[4], eh[5], eh[6], eh[7])
                    cursor.execute(sql, values)
                    connection.commit()
                prev_arrow = driver.find_element(By.CSS_SELECTOR, ".prev.arrow")
                driver.execute_script("arguments[0].click();", prev_arrow)
                time.sleep(1)
            time.sleep(2)

driver.quit()
cursor.close()
connection.close()

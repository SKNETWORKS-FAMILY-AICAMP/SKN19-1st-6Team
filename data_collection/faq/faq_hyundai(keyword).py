from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# 충전1, 카드6, 혜택1, 정비2, 수리2, 

# 1. chrome 실행
path = 'chromedriver.exe'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)

# 2. 특정 url 접근
# driver.get('https://www.kia.com/kr/customer-service/center/faq')
# time.sleep(1)

# 3. 검색 처리
# - 검색어 입력 및 검색
keyword = ['전기', '전기차', '충전', '보조', '카드', '혜택', '정비', '수리', '배터리', '방전', '고전압', '인프라']
for key in keyword:
    driver.get('https://www.hyundai.com/kr/ko/e/customer/center/faq')
    time.sleep(1)

    search_box = driver.find_element(By.CSS_SELECTOR, '.search-wrap')
    search_box.send_keys(key)
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)

    html = driver.page_source
    # UTF-8 인코딩으로 파일 저장
    try:
        with open(f'hyundai_{key}.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("파일이 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {e}")
        
driver.quit()

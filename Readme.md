## 🌱 SK네트웍스 Family AI  캠프 19기 1차 프로젝트

### **1️⃣ 팀 소개**

- 팀명: 🍫 윌리6 🚗
- 팀원 & GitHub

    | 이름  | 한줄소개             | GitHub                                  |
    | --- | --------------- | --------------------------------------- |
    | 이인재 | 열심히하겠습니다😤 | [🔗 GitHub](https://github.com/distecter) |
    | 이승원 | 노력해볼게요🧐 | [🔗 GitHub](https://github.com/seungwon-sw)    |
    | 김소희 | 데이터 숲에서 길을 찾는 탐험가🤠      | [🔗 GitHub](https://github.com/sosodoit) |
    | 신지섭 | 항상 피곤한 개발자😪 | [🔗 GitHub](https://github.com/Melonmacaron) |

### **2️⃣ 프로젝트 개요**

#### 프로젝트 명

    👉 친환경차 혜택 정보 통합 플랫폼

#### 프로젝트 소개

    친환경 차량에 관한 등록 데이터, 국가 보조금, 카드사 혜택 등을 
    한 곳에서 볼 수 있는 웹사이트를 제공합니다.

    이를 통해 소비자가 데이터 기반의 정보와 구매 시 및 
    구매 이후 혜택을 쉽게 확인할 수 있도록 돕습니다.
    

#### 프로젝트 필요성(배경)
    
<img src="./etc/등록추이1.png" width="300"/>

- 최근 친환경차 등록 수 증가 & 정부·지자체의 다양한 보조금 정책
    
<img src="./etc/하이브리드.png" width="500"/>
<img src="./etc/전기.png" width="500"/>
<img src="./etc/수소.png" width="500"/>

- 친환경 차량 비중 증가 > 관련 혜택 수요 증가 (예상)   
→ 위 정보를 근거하여, 소비자의 정보 탐색 비용을 줄이고 구매를 촉진할 필요성이 존재
    
#### 프로젝트 목표

    친환경차 구매 잠재 고객의 정보 접근성 향상을 목표로, 데이터·시각화·혜택 정보 통합을 통해
    소비자 중심의 서비스를 제공하는 것을 목표로 합니다!

#### 주요 목표 기능

    📊 친환경차 중심의 연료별 차량 등록 현황 시각화

    💳 국가/지자체 보조금 및 신용카드 혜택 정보 안내

    ❓ 친환경차 FAQ 제공

#### 📂 프로젝트 구조
```
project/
│── data_collection/   # 데이터 수집/적재 코드
│── mysql/             # DB 관련 코드 및 쿼리
│── streamlit/         # 화면 구현 코드
│── etc/               # WBS, 요구사항 문서 등
```

#### 활용 데이터
- [친환경 자동차 등록 현황](https://stat.molit.go.kr/portal/cate/statMetaView.do?hRsId=58&hFormId=1244&hSelectId=1244&hPoint=00&hAppr=1&hDivEng=&oFileName=&rFileName=&midpath=&sFormId=1244&sStart=2024&sEnd=2024&sStyleNum=562&settingRadio=xlsx)
- [국가 보조금](https://ev.or.kr/nportal/monitor/evMap.do#)
- [카드 고릴라](https://www.card-gorilla.com/search/all?keyword=%EC%A0%84%EA%B8%B0%EC%B0%A8)
- [현대FAQ](https://www.hyundai.com/kr/ko/faq.html)
- [기아FAQ](https://www.kia.com/kr/customer-service/center/faq)

### **3️⃣ 기술 스택**

- 협업: <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/notion/notion-original.svg" alt='Notion' width='20' /> Notion, <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" alt='Git' width='20'/> Git, <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" alt='GitHub' width='20'/> GitHub
- 데이터: <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg" alt='MySQL' width='20'/> MySQL
- 언어 & 환경: <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt='Python' width='20'/> Python(version=3.12), <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" alt='VSCode' width='20' /> VSCode
- 크롤: <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" alt='Selenium' width='20'/> Selenium, <img src="https://img.shields.io/badge/-BeautifulSoup-green?logo=python&logoColor=white" height="20"/> BeautifulSoup
- 데이터 정제/처리: <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" alt='Pandas' width='20'/> Pandas
- 프론트엔드: <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original.svg" alt='Streamlit' width='20'/> Streamlit


### **4️⃣ WBS**

|분류|상세업무|산출물|시작일|종료일|
|---|---|---|---|---|
|기획|1. 데이터서치 및 주제선정||09.01|09.03|
|기획|2. 데이터 수집 가능성 검증||09.01|09.03|
|기획|2-1. 조사 URL별 수집 가능성 확인||09.01|09.03|
|기획|2-2. 데이터 구조 확인(샘플 데이터)||09.01|09.03|
|요구분석|3. 요구사항 분석|요구사항 명세서|09.03|09.03|
|요구분석|3-1. 요구사항별 기능 목록화||09.03|09.03|
|요구분석|3-2. 요구사항별 활용 데이터 식벽||09.03|09.03|
|화면설계|3. 화면 레이아웃 설계|페이지별 목업|09.03|09.03|
|DB설계|4. DB 설계|ERD|09.03|09.03|
|개발|5. 개발 환경 셋팅||09.03|09.03|
|개발|5-1. Streamlit-Mysql 연동||09.03|09.03|
|개발|5-2. 크롤링 코드 구현|크롤링 코드|09.03|09.03|
|개발|5-3. DB 적재 코드 구현|DB 적재 코드|09.03|09.04|
|개발|6. 화면 구현|화면 구현 코드|09.04|09.04|
|개발|6-1. 페이지 구현||09.04|09.04|
|개발|6-2. 페이지별 기능 구현||09.04|09.04|
|통합테스트|7. 코드 점검 및 리팩토링||09.04|09.04|

### **5️⃣ ERD** 
    
   <img src="./mysql/ERD1.png" alt="ERD1" width="800"/>

### **6️⃣ 요구사항 명세서**

#### 📝 페이지별 목업 및 담당자

| 페이지 | [CR] 친환경차 등록 알아보기 | [BE] 보조금 정보 알아보기 | [CD] 친환경 카드 알아보기 | [FA] FAQ |
|:------:|:----:|:----:|:----:|:----:|
| 목&nbsp;업 | <img src="./etc/목업_CR.jpg" width="200"/> | <img src="./etc/목업_BE.jpg" width="200"/> | <img src="./etc/목업_CD.png" width="200"/> | <img src="./etc/목업_FA.png" width="200"/> |
| 담&nbsp;당&nbsp;자 | 이승원 | 신지섭 | 김소희 | 이인재 |

<br/>

#### 📝 페이지별 요구사항 명세서

<details>
<summary><strong>[CR] 친환경차 등록 알아보기</strong></summary>
<br/>

|구분|기능명|내용|비고|구현여부|
|---|---|---|---|---|
|CR-GRAPH-01|월별 차량 추이|형태 = 꺾은 선 그래프||○|
|CR-FILTER-01|사용자 필터(그래프선택)|차종 / 지역 / 연료|선택한 번호의 그래프 노출|△(사용자 측면에서 차종별 추이는 활용 가능성이 낮아 구현 제외)|
|CR-FILTER-02|사용자 필터(지역선택)|서울, 충남, ...|TAB-01 = 지역 선택시|○|
|CR-FILTER-03|사용자 필터(연료선택)|전기, 수소, 하이브리드|TAB-01 = 연료 선택시|○|
</details>

<details>
<summary><strong>[BE] 보조금 정보 알아보기</strong></summary>
<br/>

|구분|기능명|내용|비고|구현여부|
|---|---|---|---|---|
|BE-FILTER-01|사용자 필터(차량회사선택)|||○|
|BE-FILTER-02|사용자 필터(차량종류선택)|경차, 세단,  SUV||○|
|BE-FILTER-03|사용자 필터(정렬기능)|조회 기준(보조금, 탑승인원)||○|
|BE-GRAPH-01|차량 이미지||페이지 중앙 왼쪽 구현|○|
|BE-GRAPH-02|차량 기본 설명|연료, 완충 주행거리, 회사, 차종, 차명, 제조사, 제조국가|페이지 중앙 오른쪽 구현|○|
</details>

<details>
<summary><strong>[CD] 친환경 카드 알아보기</strong></summary>
<br/>

|구분|기능명|내용|비고|구현여부|
|---|---|---|---|---|
|CD-TABLE-01|카드 상세 정보|카드이미지, 카드명, 주요 혜택, 카드링크(버튼) 노출|TABLE-02의 첫번째 카드 노출|○|
|CD-TABLE-02|FILTER 기준 관련 카드 목록|카드사, 카드명, 카드타입, 카드링크||X(TABLE-01 로도 정보 제공이 충분하여 제외)|
|CD-BTN-01|카드 보러 가기 버튼|카드 상세 페이지 이동||○|
|CD-GRAPH-01|카드사별 친환경 카드 통계|형태 = 파이 차트 / 필터 영향 없음||○|
|CD-GRAPH-02|전체 카드의 친환경 혜택 통계|형태 = 막대 그래프 / 필터 영향 없음||○|
|CD-FILTER-01|사용자 필터(카드사선택)|TABLE-01, TABLE-02 필터링||○|
|CD-FILTER-02|사용자 필터(카드타입선택)|TABLE-01, TABLE-02 필터링||○|
|CD-FILTER-03|사용자 필터(주요혜택선택)|TABLE-01, TABLE-02 필터링||○|
|CD-NAV-01|카드 목록 네비게이션 기능|카드 목록 (default = 10)||○|
</details>

<details>
<summary><strong>[FA] FAQ</strong></summary>
<br/>

|구분|기능명|내용|비고|구현여부|
|---|---|---|---|---|
|FA-FILTER-01|사용자 필터(회사선택)|회사별 FAQ 필터링||○|
|FA-FILTER-02|사용자 필터(키워드선택)|친환경 키워드별 FAQ 필터링||○|
|FA-GRAPTH-01|FAQ 등록 개수|FAQ 질문 총합 개수 시각화||○|
|FA-BTN-01|FAQ 펼침/닫침 기능|사용자 편의성을 위한 펼침/닫침 기능||○|
|FA-BTN-02|키워드 및 질문 등록 갱신|공식 홈페이지에 올라온 신규 질문과 키워드 추가||X|
|FA-NAV-01|FAQ 목록 네비게이션 기능|FAQ 목록 (default = 10)||○|
</details>

### **7️⃣ 수행결과(테스트/시연 페이지)**

1. 페이지명: 친환경차 등록 현황 알아보기
    - 목적: 차량 등록의 추이를 확인시킴으로서 친환경차의 관심도 증가 추세를 보여줌
<img src="./etc/등록페이지.png" width="1000"/>

2. 페이지명: 보조금 확인
    - 목적: 친환경 차량 구매시 모델별로 받을 수 있는 보조금 확인
<img src="./etc/보조금페이지.png" width="1000"/>

3. 페이지명: 친환경차 카드정보 
    - 목적: 사용자에게 친환경 차량 관련 혜택이 있는 카드 정보 제공
<img src="./etc/카드페이지.png" width="1000"/>

4. 페이지명:FAQ
    - 목적: 차량 회사 데이터 기반의 FAQ를 친환경 차량 키워드로 제공
<img src="./etc/FAQ페이지.png" width="1000"/>

---

### **⚡이슈 해결 과정**

1. 셀레니움 차단 문제

    셀리니움으로 검색어 입력 후 실행 시 결과가 정상적인 로드가 되지 않고, 페이지가 차단 이로 인해 원하는 데이터 수집이 불가 -> 동작 속도를 최대 10초 까지 조정하여 진행 하였음에도 불가능 -> 셀레니움으로 검색 결과까지는 되는 경우 받아온 데이터를 HTML로 저장하여 이를 DB에 저장하는 형식으로 진행

2. 문제상황 : 보조금 차량 데이터 수집과정에서 사이트에 있는 이미지 소스 링크가 직접적인 접근을 차단한 상태

    해결과정 : Selenium 브라우저의 스크린샷 메서드로 해결하려고 했지만 화면의 위쪽 레이어에 존재하는 여러 요소들이 사진을 가려졌지만 해당 요소를 비활성화 시키는 JS코드를 이용하여 해당요소를 화면에서 비활성화시킨후 Selenium 브라우저의 스크린샷 메서드를 이용하여 문제 해결
    
    결과 : 해당 사이트에 존재하는 모든 보조금 차량 이미지 크롤링 완료

### **🔎 아쉬운점 & 개선점**

- 섬세하게 다루지 못한 데이터가 있어 아쉬움 (차량 모델·카드 혜택 카테고리 세분화 필요)

- 기한 내 작업계획·범위가 명확하지 못했던 점 → 프로젝트 관리 개선 필요

- 향후 더 많은 외부 API 연동 고려 필요


### **한 줄 회고**

| 이름  | 한줄회고          |
| ------ | --------------- |
| 이&nbsp;인&nbsp;재 | 개인의 사정상 streamlit, web crawling의 수업을 듣지 못했지만 팀원들의 도움으로 동적, 정적 크롤링 코드의 작성법 및 반복문의 응용을 제대로 하며 기본 문법의 중요성을 다시금 깨닫게 되었고 db생성, 연결, 등록을 크롤링을 이용해 직접 하게되어 데이터가 어떻게 등록되어 구분하는지 명확하게 알게되어 의미가 있던 프로젝트였다. |
| 이&nbsp;승&nbsp;원 | 파일 정제 및 파이썬을 통한 DB 적재, DB를 활용한 streamlit 구현을 해볼 수 있었다.  | 
| 김&nbsp;소&nbsp;희 | 프로젝트 폴더 구조를 미리 설계하고 스트림릿 DB 연동을 모듈화하여 팀원들의 코드 통합을 원활하게 진행할 수 있었습니다. 앞으로 더 큰 규모의 프로젝트를 진행할 때에도 이러한 경험을 살려 초기 단계부터 통합과 확장을 고려한 구조를 제안하고 적용해 보고자 합니다. | 
| 신&nbsp;지&nbsp;섭 | 보조금확인 페이지 구현을 중점적으로 담당하였습니다. 동적인 웹 페이지의 데이터를 크롤링해야했기에 Selenium브라우저를 이용하여 크롤링을 진행하였고 공통된 컬럼을 갖는 등록데이터와의 정규화를 진행하였습니다. |

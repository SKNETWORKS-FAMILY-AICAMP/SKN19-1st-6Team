from modules.db_handling import get_data
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

text1 = "🌱 얼마나 많은 사람들이 "
highlight = "<span style='color:green;'>친환경차</span>"
text2 = "를 몰고 다닐까요? 한번 같이 확인해봐요😍"
st.markdown(f"<h1>{text1}{highlight}{text2}</h1>", unsafe_allow_html=True)


df = get_data('car')
# st.dataframe(df.reset_index(drop=True))


options = ['연료 별 차량 등록' , '지역 별 친환경 차량 등록']
graph = st.selectbox('어떤 그래프를 보고 싶으세요? (그래프 선택)', options)

df_line = (
        df.groupby(["year_month_code", "fuel_group"], as_index=False)["registration_count"]
        .sum()
    )

    # 2) x축을 날짜로(정렬 안정)
df_line["year_month"] = pd.to_datetime(df_line["year_month_code"].astype(str) + "01", format="%Y%m%d")
df_line = df_line.sort_values("year_month")

if graph == '연료 별 차량 등록':
    # 1) fuel_group 고유값 가져오기
    fuel_options = df_line["fuel_group"].unique().tolist()

    # 2) 멀티셀렉트 위젯 (기본값은 전부 선택된 상태)
    selected_fuels = st.multiselect(
        "어떤 연료가 궁금하세요? (연료 선택: 다중선택 가능)",
        fuel_options,
        default=fuel_options
    )

    # 3) 선택된 fuel_group만 필터링
    df_line_filtered = df_line[df_line["fuel_group"].isin(selected_fuels)]

    # 4) 라인 차트
    st.line_chart(
        data=df_line_filtered,
        x="year_month",
        y="registration_count",
        color="fuel_group",
        use_container_width=True,
    )

if graph == '지역 별 친환경 차량 등록':
    # 1) 지역 선택
    region_options = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', 
                      '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
    selected_region = st.selectbox('어떤 지역이 궁금하세요? (지역 선택)', region_options)

    # 2) 지역 × 연료 그룹핑
    df_region = (
        df.groupby(["year_month_code", "region", "fuel_group"], as_index=False)["registration_count"]
          .sum()
    )

    # 3) 날짜 변환 + 정렬
    df_region["year_month"] = pd.to_datetime(
        df_region["year_month_code"].astype(str) + "01", format="%Y%m%d"
    )
    df_region = df_region.sort_values("year_month")

    # 4) 선택한 지역만 필터링
    df_region_filtered = df_region[df_region["region"] == selected_region]

    # 5) 연료 그룹 중 하이브리드·전기·수소만 남기기
    target_fuels = ["하이브리드", "전기", "수소"]
    df_region_filtered = df_region_filtered[df_region_filtered["fuel_group"].isin(target_fuels)]

    # 6) 라인 차트 (연료별 색상 분리)
    st.line_chart(
        data=df_region_filtered,
        x="year_month",
        y="registration_count",
        color="fuel_group",
        use_container_width=True,
    )

from modules.db_handling import get_data
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title(
    "🌱 친환경차를 몰고계신가요? 몰고다닐계획이신가요? 관련된 카드 혜택을 확인해보세요😍"
)
df = get_data("card")

# 사이드바 필터링
st.sidebar.header("필터")
selected_fuel = st.sidebar.multiselect("친환경 차 종류 선택", ["전기차", "수소차"])
selected_benefit = st.sidebar.multiselect(
    "주요혜택 선택",
    ["충전요금할인", "교통할인", "정비서비스", "자동차보험", "차량기타"],
)
selected_company = st.sidebar.multiselect(
    "카드사 선택", df["card_company_name"].unique()
)
selected_type = st.sidebar.multiselect("카드타입 선택", df["card_type"].unique())

# ---------------------------------------------------------------------------------------
filtered_df = df.copy()

# 카드별 혜택이 여러 행으로 존재하므로 card_id 기준으로 통합
benefit_cols = {
    "충전요금할인": "charging_discount_yn",
    "교통할인": "transport_discount_yn",
    "정비서비스": "maintenance_service_yn",
    "자동차보험": "auto_insurance_yn",
    "차량기타": "vehicle_etc_yn",
}


def any_y(s):
    return "Y" if (s.astype(str).str.upper() == "Y").any() else "N"


df_unique = (
    df.groupby(["card_company_name", "card_name"], as_index=False)
    .agg(
        {
            "card_type": "first",
            "card_image": "first",
            "card_detail_url": "first",
            "card_type_elec_yn": any_y,  # 연료타입 카드 단위로 OR
            "card_type_suso_yn": any_y,  # 연료타입 카드 단위로 OR
            **{col: any_y for col in benefit_cols.values()},  # 혜택 OR 집계
            "card_detail": lambda s: " · ".join(
                sorted(set(map(str, s)))
            ),  # 대표 상세혜택(중복 제거 후 합치기)
        }
    )
    .rename(columns={"card_detail": "card_detail_agg"})
)

# 이후 모든 필터/시각화는 df 대신 df_unique 사용
filtered_df = df_unique.copy()

# ---------------------------------------------------------------------------------------

# ID: 필터0: 전기차, 수소차 선택
fuel_type_cols = {
    "전기차": "card_type_elec_yn",
    "수소차": "card_type_suso_yn",
}
if selected_fuel:
    cond = pd.Series(False, index=filtered_df.index)
    for fuel in selected_fuel:
        cond |= filtered_df[fuel_type_cols[fuel]] == "Y"
    filtered_df = filtered_df[cond]

# ID: 필터3: 주요혜택 선택
benefit_cols = {
    "충전요금할인": "charging_discount_yn",
    "교통할인": "transport_discount_yn",
    "정비서비스": "maintenance_service_yn",
    "자동차보험": "auto_insurance_yn",
    "차량기타": "vehicle_etc_yn",
}
if selected_benefit:
    cond = pd.Series(False, index=filtered_df.index)
    for benefit in selected_benefit:
        cond |= filtered_df[benefit_cols[benefit]] == "Y"
    filtered_df = filtered_df[cond]

# ID: 필터1: 카드사 선택
if selected_company:
    filtered_df = filtered_df[filtered_df["card_company_name"].isin(selected_company)]

# ID: 필터2: 카드타입 선택
if selected_type:
    filtered_df = filtered_df[filtered_df["card_type"].isin(selected_type)]
# ---------------------------------------------------------------------------------------

# ID: 시각화1 - 필터 영향 없음 (카드별 카운트 중복 제거 완료)
card_counts = (
    df_unique.groupby("card_company_name")["card_name"]
    .nunique()
    .reset_index(name="card_count")
)
fig = px.pie(
    card_counts,
    values="card_count",
    names="card_company_name",
    title="친환경 카드상품이 많은 카드사",
)
st.plotly_chart(fig, use_container_width=True)

# ID: 시각화2 - 필터 영향 없음 (혜택별 카드 카운트 중복 제거 완료)
benefit_counts = {
    name: (df_unique[col] == "Y").sum() for name, col in benefit_cols.items()
}
benefit_df = pd.DataFrame(
    sorted(benefit_counts.items(), key=lambda x: x[1], reverse=True),
    columns=["혜택", "카드 수"],
)
fig2 = px.bar(
    benefit_df,
    x="혜택",
    y="카드 수",
    title="친환경차와 관련된 주요 혜택 순위",
    text="카드 수",
)
st.plotly_chart(fig2, use_container_width=True)
# ---------------------------------------------------------------------------------------

# ID: 테이블1 - 카드 상세보기 (페이지네이션 적용, key로 중복 ID 에러 해결)
st.subheader("카드 상세보기")

# 페이지네이션 설정
items_per_page = 10
total_items = len(filtered_df)
total_pages = (total_items - 1) // items_per_page + 1

page = st.number_input(
    "페이지 선택",
    min_value=1,
    max_value=total_pages,
    value=1,
    step=1,
    key="card_pagination",
)

start_idx = (page - 1) * items_per_page
end_idx = start_idx + items_per_page

for i, row in filtered_df.iloc[start_idx:end_idx].iterrows():
    with st.expander(
        f"{row['card_company_name']} - {row['card_name']}", expanded=(i == start_idx)
    ):
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(f'img/card/{row["card_image"]}', caption=row["card_name"])
        with col2:
            st.write(f"**카드사**: {row['card_company_name']}")
            st.write(f"**타입**: {row['card_type']}")
            st.write(f"**상세혜택**: {row['card_detail_agg']}")
            st.markdown(f"[👉 상세 페이지로 이동]({row['card_detail_url']})")

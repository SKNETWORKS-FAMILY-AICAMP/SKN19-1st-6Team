from modules.db_handling import get_data
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os


def sort_df(df, sort_key):
    if sort_key == "driving_range_clean":
        return df.sort_values(by="driving_range_clean", ascending=False)
    elif sort_key == "vehicle_subsidy":
        return df.sort_values(by="vehicle_subsidy", ascending=False)
    else:
        return df


def extract_driving_range(val):
    if pd.isna(val):
        return np.nan
    val = str(val)

    import re

    match = re.search(r"\(상온\)(\d+)", val)
    if match:
        return int(match.group(1))

    match = re.search(r"(\d+)", val)
    if match:
        return int(match.group(1))
    return np.nan


st.title("🌱 어떤 차에 관심이 있으신가요? 보조금 한번 확인해보세요 ~ 🤑")
df = get_data("benefit")
df = df.replace("NULL", "정보없음")

df["vehicle_subsidy"] = (
    df["vehicle_subsidy"]
    .astype(str)
    .str.extract(r"(\d+)")[0]
    .astype(float)
    .astype("Int64")
)
df["driving_range_clean"] = df["driving_range"].apply(extract_driving_range)

c11, c12 = st.columns([7.5, 2.5])
with c11:
    r_options = {"승용차": "승용", "승합차": "승합", "화물차량": "화물"}

    v_type_display = st.radio(
        "차량 타입 선택", options=list(r_options.keys()), horizontal=True
    )

    v_type = r_options[v_type_display]
with c12:
    f_options = ["전기", "수소"]
    f_type = st.radio("", f_options, horizontal=True)

from collections import Counter

# 1. 각 vehicle_model 그룹별로 처리
brand_by_model = {}

for model, group in df.groupby("vehicle_model"):
    brands = group["vehicle_brand"]
    brand_counts = Counter(brands)
    sorted_brands = [brand for brand, _ in brand_counts.most_common()]
    brand_by_model[model] = sorted_brands

for model, brands in brand_by_model.items():
    print(f"{model}: {brands}")

if v_type == "승용":
    brands = brand_by_model["승용"]
elif v_type == "승합":
    brands = brand_by_model["승합"]
elif v_type == "화물":
    brands = brand_by_model["화물"]
elif v_type == "특수":
    brands = brand_by_model["특수"]

c21, c22 = st.columns(2)
with c21:
    brand = st.selectbox("브랜드", brands)
with c22:
    st.markdown("<br>", unsafe_allow_html=True)
    if v_type == "승용":
        cc21, cc22, cc23 = st.columns(3)
        with cc21:
            small = st.checkbox("경차")
        with cc22:
            mid = st.checkbox("세단")
        with cc23:
            suv = st.checkbox("SUV")
c31, c32 = st.columns([7, 3])
select_df = df[
    (df["vehicle_model"] == v_type)
    & (df["vehicle_brand"] == brand)
    & (df["fuel_category_name"] == f_type)
]

if v_type == "승용":
    selected_details = []
    if small:
        selected_details.append("경차")
    if mid:
        selected_details.append("세단")
    if suv:
        selected_details.append("SUV")

    if selected_details:
        select_df = select_df[select_df["vehicle_model_detail"].isin(selected_details)]
with c31:
    model_name = st.text_input("검색")

if model_name:
    select_df = select_df[
        select_df["model"].str.contains(model_name, case=False, na=False)
    ]
with c32:
    key_map = {
        "정렬순서": None,
        "1회충전거리순": "driving_range_clean",
        "보조금순": "vehicle_subsidy",
    }
    o_options = ["정렬순서", "보조금순", "1회충전거리순"]
    order = st.selectbox("", o_options)
container = st.container()
sorted_df = sort_df(select_df, key_map[order])

with container:
    img_folder = "img/"
    for idx, row in sorted_df.iterrows():
        col1, col2 = st.columns([1.5, 4])
        img_path = img_path = os.path.join(img_folder, row["vehicle_image"])
        # 왼쪽: 이미지 불러오기 (경로가 있다고 가정)
        try:
            img = Image.open(img_path)
            col1.image(img, use_container_width=True)
        except:
            col1.write("이미지 없음")

        # 오른쪽: 차량 정보 나열
        with col2:
            st.markdown(f"**모델:** {row['model']}")
            st.markdown(f"**브랜드:** {row['vehicle_brand']}")
            st.markdown(
                f"**1회 충전 거리:** {row.get('driving_range_clean', '정보없음')} km"
            )
            st.markdown(f"**보조금:** {row.get('vehicle_subsidy', '정보없음')} 만원")
            if v_type == "승용":
                a = row.get("vehicle_model_detail", "")
                if a != "정보없음":
                    st.markdown(f"**차분류:** {row.get('vehicle_model_detail', '')}")

        st.markdown("---")  # 구분선

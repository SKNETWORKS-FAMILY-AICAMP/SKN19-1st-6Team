from modules.db_handling import get_data
import streamlit as st
import pandas as pd 

st.title('자동차 페이지 만들기')
df = get_data('car')
st.dataframe(df.reset_index(drop=True))
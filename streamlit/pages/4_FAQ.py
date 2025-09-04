from modules.db_handling import get_data
import streamlit as st
import pandas as pd 

st.title('FAQ 페이지 만들기')
df = get_data('faq')
st.dataframe(df.reset_index(drop=True))
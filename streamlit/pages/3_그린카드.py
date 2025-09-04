from modules.db_handling import get_data
import streamlit as st
import pandas as pd 

st.title('카드 혜택 페이지 만들기')
df = get_data('card')
st.dataframe(df.reset_index(drop=True))
st.image("img/card/2290card.png")
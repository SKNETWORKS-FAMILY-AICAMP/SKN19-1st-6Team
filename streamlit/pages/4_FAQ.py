from modules.db_handling import get_data
import streamlit as st
import pandas as pd 

# 커스텀 CSS
st.markdown("""
<style>
    /* 전체 페이지 배경 설정 - 어두운 배경 */
    .stApp {
        background-color: #1E1E1E !important;
    }
    
    .main .block-container {
        background-color: #1E1E1E !important;
        padding-top: 2rem;
        color: white;
    }
    
    /* 사이드바 배경 */
    .css-1d391kg {
        background: linear-gradient(180deg, #2C3E50, #34495E) !important;
    }
    
    .main-title {
        background: linear-gradient(135deg, #2C3E50, #34495E);
        padding: 2rem 1rem;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(44, 62, 80, 0.5);
    }
    
    .main-title h1 {
        color: white !important;
        margin: 0;
        font-size: 2.5rem;
    }
    
    .main-title .subtitle {
        color: #BDC3C7 !important;
        font-size: 1.1rem;
        margin-top: 0.5rem;
        opacity: 0.9;
    }
    
    .stats-container {
        background: #2A2D3A;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #5DADE2;
        margin: 1.5rem 0;
        font-size: 1.1rem;
        font-weight: 500;
        color: white;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
    }
    
    .question-card {
        background: #2A2D3A;
        border: 2px solid #3A3F4B;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        color: white;
    }
    
    .question-card:hover {
        border-color: #5DADE2;
        box-shadow: 0 6px 20px rgba(93, 173, 226, 0.3);
        transform: translateY(-2px);
    }
    
    .answer-container {
        background: #353A47;
        border-radius: 10px;
        padding: 1.5rem;
        margin-top: 1rem;
        border-left: 4px solid #5DADE2;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        color: #E8E8E8;
    }
    
    .company-tag {
        background: #2C3E50;
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        display: inline-block;
        margin-right: 0.5rem;
        margin-top: 0.5rem;
    }
    
    .keyword-tag {
        background: #5DADE2;
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        display: inline-block;
        margin-top: 0.5rem;
    }
    
    .pagination-area {
        background: #2A2D3A;
        border-radius: 12px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        border: 1px solid #3A3F4B;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
        color: white;
    }
    
    .no-results-container {
        text-align: center;
        padding: 3rem 2rem;
        background: #2A2D3A;
        border-radius: 15px;
        margin: 2rem 0;
        border: 2px dashed #5DADE2;
        color: white;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
    }
    
    .sidebar-header {
        background: linear-gradient(135deg, #2C3E50, #34495E);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        text-align: center;
        font-weight: bold;
    }
    
    /* Streamlit 기본 버튼 스타일 오버라이드 */
    .stButton > button {
        background: #2A2D3A;
        color: white;
        border: 2px solid #3A3F4B;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
        font-weight: 500;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .stButton > button:hover {
        border-color: #5DADE2;
        background: linear-gradient(135deg, #5DADE2, #3498DB);
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 4px 16px rgba(93, 173, 226, 0.3);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    .stButton > button:disabled {
        background: #1A1D26;
        color: #666;
        border-color: #333;
        cursor: not-allowed;
    }
    
    /* 체크박스 스타일 */
    .stCheckbox {
        background: #2A2D3A;
        padding: 0.8rem;
        border-radius: 8px;
        border: 1px solid #3A3F4B;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    }
    
    .stCheckbox label {
        color: white !important;
    }
    
    /* 라디오 버튼 스타일 */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
    }
    
    .stRadio label {
        color: white !important;
    }
    
    /* 멀티셀렉트 스타일 */
    .stMultiSelect label {
        color: white !important;
    }
    
    /* 구분선 스타일 */
    hr {
        border-color: #3A3F4B;
        opacity: 0.8;
    }
    
    /* Expander 스타일 */
    .streamlit-expanderHeader {
        background: #2A2D3A !important;
        border-radius: 8px !important;
        border: 2px solid #3A3F4B !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
        color: white !important;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: #5DADE2 !important;
    }
    
    .streamlit-expanderContent {
        background: #2A2D3A !important;
        color: white !important;
    }
    
    /* 텍스트 색상 강제 지정 */
    p, div, span {
        color: white !important;
    }
    
    /* 사이드바 텍스트 색상 */
    .sidebar .sidebar-content {
        color: white !important;
    }
    
    .sidebar .sidebar-content label {
        color: white !important;
    }
    
    .sidebar .sidebar-content .stSelectbox label {
        color: white !important;
    }
    
    /* 헤더 텍스트 */
    .sidebar .sidebar-content h1, 
    .sidebar .sidebar-content h2, 
    .sidebar .sidebar-content h3 {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# 제목과 부제목
st.markdown("""
<div class="main-title">
    <h1>자주 묻는 질문</h1>
    <div class="subtitle">친환경 차에 대한 궁금한 내용을 빠르게 조회 가능합니다.</div>
</div>
""", unsafe_allow_html=True)

df = get_data('faq')

# 답변이 비어있는 데이터 제거
df = df.dropna(subset=['answer'])  # NaN 값 제거
df = df[df['answer'].astype(str).str.strip() != '']  # 빈 문자열 및 공백만 있는 값 제거

# 질문도 함께 확인 (선택사항)
df = df.dropna(subset=['question'])  # 질문이 NaN인 경우 제거
df = df[df['question'].astype(str).str.strip() != '']  # 빈 질문 제거

st.sidebar.header('회사명')
selected_company = st.sidebar.radio(
    '회사 선택', 
    df['company'].unique()
)

selected_keyword = st.sidebar.multiselect(
    '키워드 선택', 
    df['keyword'].unique()
)

# 데이터 필터링 (수정된 부분)
filter_df = df.copy()

# 회사 필터 적용 - 라디오 버튼이므로 단일 값 비교
if selected_company:
    filter_df = filter_df[filter_df['company'] == selected_company]

# 키워드 필터 적용 - 멀티셀렉트이므로 isin 사용
if selected_keyword:
    filter_df = filter_df[filter_df['keyword'].isin(selected_keyword)]

# 페이지네이션을 위한 설정
items_per_page = 10
total_items = len(filter_df)
total_pages = (total_items - 1) // items_per_page + 1 if total_items > 0 else 1

# 현재 페이지 상태 관리
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1

# 페이지 번호가 범위를 벗어나는 경우 조정
if st.session_state.current_page > total_pages:
    st.session_state.current_page = 1

# FAQ 리스트 표시
st.markdown(f"""
<div class="stats-container">
    총 {total_items}개의 질문이 있습니다.
</div>
""", unsafe_allow_html=True)

# 디버깅 정보 (필요시 주석 해제)
# st.write(f"선택된 회사: {selected_company}")
# st.write(f"선택된 키워드: {selected_keyword}")
# st.write(f"전체 데이터 개수: {len(df)}")
# st.write(f"필터링된 데이터 개수: {len(filter_df)}")

st.write("---")

# 질문이 있는 경우에만 표시
if total_items > 0:
    # 펼침/접힘 방식 선택 (페이지 상단에 배치하고 세션 상태로 관리)
    if 'use_expander' not in st.session_state:
        st.session_state.use_expander = False

    st.session_state.use_expander = st.checkbox("펼침/접힘 방식으로 보기", value=st.session_state.use_expander)

    # 현재 페이지에 해당하는 데이터 추출
    start_idx = (st.session_state.current_page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    current_page_df = filter_df.iloc[start_idx:end_idx]

    if st.session_state.use_expander:
        # Expander 방식
        for idx, row in current_page_df.iterrows():
            with st.expander(f"Q: {row['question']}"):
                st.markdown(f"""
                <div class="answer-container">
                    <strong>답변:</strong> {row['answer']}
                    <div style="margin-top: 1rem;">
                        <span class="company-tag">회사: {row['company']}</span>
                        <span class="keyword-tag">키워드: {row['keyword']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        # 버튼 클릭 방식
        for idx, row in current_page_df.iterrows():
            # 질문을 버튼으로 표시
            if st.button(f"Q: {row['question']}", key=f"question_{idx}"):
                # 선택된 질문의 인덱스를 세션 상태에 저장
                st.session_state.selected_question = idx
            
            # 해당 질문이 선택되었다면 답변 표시
            if hasattr(st.session_state, 'selected_question') and st.session_state.selected_question == idx:
                st.markdown(f"""
                <div class="answer-container">
                    <strong>답변:</strong> {row['answer']}
                    <div style="margin-top: 1rem;">
                        <span class="company-tag">회사: {row['company']}</span>
                        <span class="keyword-tag">키워드: {row['keyword']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.write("---")
            else:
                st.write("---")

    # 페이지네이션 컨트롤 (하단에 배치)
    st.write("---")
    if total_pages > 1:
        st.markdown("""
        <div class="pagination-area">
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.button("◀ 이전", disabled=st.session_state.current_page == 1):
                st.session_state.current_page -= 1
                st.rerun()
        
        with col2:
            st.markdown(f"""
            <div style="text-align: center; font-size: 1.2rem; font-weight: bold; padding: 1rem;">
                페이지 {st.session_state.current_page} / {total_pages}
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            if st.button("다음 ▶", disabled=st.session_state.current_page == total_pages):
                st.session_state.current_page += 1
                st.rerun()
        
        st.markdown("""
        </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="no-results-container">
        <h2>선택한 조건에 맞는 질문이 없습니다.</h2>
        <p>다른 회사나 키워드를 선택해보세요.</p>
    </div>
    """, unsafe_allow_html=True)
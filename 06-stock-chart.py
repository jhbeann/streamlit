# 터미널에 설치 : pip install finance-datareader
# FinanceDataReader : 주식 정보 라이브러리
import streamlit as st
import FinanceDataReader as fdr
import datetime
import time

#  사용자가 시작 일자 지정 : date input
date = st.date_input(
    "조회 시작일을 선택해 주세요",
    datetime.datetime(2022,1,1)
)

code = st.text_input(
    '종목코드',
    value='',
    placeholder='종목코드를 입력해 주세요'

)

if code and date:
    # 지정 date 부터 현재까지의 정보 모두 dataframe 으로 가져옴
    df = fdr.DataReader(code, date)
    # 날짜 기준 정렬
    data = df.sort_index(ascending=True).loc[:,'Close']  # close : 종가 정보
    st.line_chart(data)




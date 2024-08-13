import streamlit as st
import random
import datetime

st.title(':sparkles:로또 생성기:sparkles:')

def generate_lotto():
    # 중복 값 방지 : set
    lotto = set()

    while len(lotto) <6:
        number = random.randint(1,46)
        lotto.add(number)

    # set -> list
    lotto = list(lotto)
    # 정렬
    lotto.sort()
    # 반환
    return lotto


st.subheader(f'행운의 번호: :green[{generate_lotto()}]')
st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

button = st.button('로또를 생성해 주세요!')

if button:
     # 5개 세트 
     for i in range(1, 6):
         st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
     st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
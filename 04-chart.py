import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = "NanumGothic"

# DataFrame 생성
data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})

st.dataframe(data, use_container_width=True)

# matplotlib
# fig 전체 그림, ax : 실제 그래프
fig, ax = plt.subplots()
ax.bar(data['이름'],data['나이'])
st.pyplot(fig)

# seaborn
barplot = sns.barplot(x='이름',y='나이',data=data, ax=ax, palette='Set2' )
fig = barplot.get_figure()

st.pyplot(fig)


#----------------------------------------------------------------
# Barcode

code = np.array([
    1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

pixel_per_bar = 4
dpi =100
fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
# span the whole figure
ax = fig.add_axes([0,0,1,1])
ax.set_axis_off()
ax.imshow(code.reshape(1,-1), cmap='binary', aspect='auto',
          interpolation='nearest')
st.pyplot(fig)
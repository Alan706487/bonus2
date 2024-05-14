import streamlit as st

# 標題
st.title('獎金試算工具')

# 用戶選擇職位
position = st.selectbox('選擇你的職位:', ('職位A', '職位B'))

# 輸入參數 X 和 Y
x = st.number_input('請輸入 X 的值:', value=0)
y = st.number_input('請輸入 Y 的值:', value=0)

# 計算按鈕
if st.button('計算獎金'):
    if position == '職位A':
        bonus = x + y
    else:
        bonus = x - y

    # 顯示結果
    st.write(f'你的獎金是: {bonus}')



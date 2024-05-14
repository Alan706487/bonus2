# import streamlit as st
# import pandas as pd
# st.title("練習1")
# st.write("建立表格")
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })
# df

import streamlit as st
from args import *  # 導入args.py中data、positions_df、regions_df

st.title('當月獎金計算器')

with st.form("bonus_form"):  # 使用表單來封裝輸入和按鈕
    position = st.selectbox('選擇職位', positions_df['職位'])
    region = st.selectbox('服務地區', regions_df['地區'])
    achievement_rate = st.number_input('指標達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100)
    performance_rate = st.number_input('業績達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100)
    accumulated_bonus = st.number_input('當季累積成果獎金', min_value=0, value=0)
    submitted = st.form_submit_button("計算總獎金")

if submitted:
    total_bonus = calculate_total_bonus(position, region, achievement_rate/100, performance_rate/100, accumulated_bonus)
    st.write(f'總獎金: {total_bonus:.0f}')

def calculate_total_bonus(position, region, achievement_rate, performance_rate, accumulated_bonus):
    """根據提供的職位、地區、指標達成率、業績達成率和累積獎金計算總獎金。"""
    position_data = positions_df[positions_df['職位'] == position].iloc[0]
    region_multiplier = regions_df[regions_df['地區'] == region]['成果倍數'].values[0]
    indicator_bonus = position_data['職務份額'] * position_data['指標占比'] * (1 + position_data['指標倍數'] * (achievement_rate - 1))
    performance_bonus = position_data['職務份額'] * position_data['成果占比'] * (1 + region_multiplier * (performance_rate - 1))
    total_bonus = indicator_bonus + max(0, performance_bonus - accumulated_bonus)
    return total_bonus


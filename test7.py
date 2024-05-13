import pandas as pd
import streamlit as st

# 建立職位相關的 DataFrame
data = {
    '職位': ['北業務', '南業務', '北區域業務', '南區域業務', '北電訪', '南電訪', '北產品顧問', '南產品顧問',
             '北高級顧問', '南高級顧問', '北資深顧問', '南資深顧問'],
    '職務份額': [22000, 21000, 24000, 23000, 14000, 13000, 16000, 15000, 18000, 17000, 20000, 19000],
    '指標占比': [0.3, 0.3, 0.3, 0.3, 1, 1, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
    '成果占比': [0.7, 0.7, 0.7, 0.7, 0, 0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    '指標倍數': [1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3]
}
positions_df = pd.DataFrame(data)

# 建立地區 DataFrame
regions_data = {
    '地區': ['台新馬', '其他'],
    '成果倍數': [3, 1]
}
regions_df = pd.DataFrame(regions_data)

# 網頁介面設定
st.title('當月獎金計算器')

# 選擇人員類型
personnel_type = st.selectbox('選擇人員類型', ['一般人員', '保障人員'])

# 根據人員類型選擇，顯示額外的輸入選項
if personnel_type == '保障人員':
    greater_than_3_months = st.radio('累積保障月數是否大於3個月', ['是', '否'])

# 使用者選擇職位和服務地區
position = st.selectbox('選擇職位', positions_df['職位'])
region = st.selectbox('服務地區', regions_df['地區'])

# 使用者輸入指標達成率和業績達成率
achievement_rate = st.number_input('指標達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
performance_rate = st.number_input('業績達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
accumulated_bonus = st.number_input('當季累積成果獎金', min_value=0, value=0, step=1000)

# 計算總獎金的函式
def calculate_total_bonus(personnel_type, position, achievement_rate, performance_rate, accumulated_bonus, region, greater_than_3_months=None):
    position_data = positions_df[positions_df['職位'] == position].iloc[0]
    region_multiplier = regions_df[regions_df['地區'] == region]['成果倍數'].values[0]

    if personnel_type == '一般人員':
        # 一般人員獎金計算
        indicator_bonus = position_data['職務份額'] * position_data['指標占比'] * (1 + position_data['指標倍數'] * (achievement_rate - 1))
        performance_bonus = position_data['職務份額'] * position_data['成果占比'] * (1 + region_multiplier * (performance_rate - 1))
        total_bonus = indicator_bonus + max(0, performance_bonus - accumulated_bonus)
    else:
        # 保障人員獎金計算
        protection_ratio = 0.75 if greater_than_3_months == '是' else 0.5
        performance_bonus = position_data['職務份額'] * protection_ratio * position_data['成果占比']
        indicator_bonus = performance_bonus * position_data['指標占比'] * (1 + position_data['指標倍數'] * (achievement_rate - 1))
        total_bonus = indicator_bonus + performance_bonus

    return total_bonus

# 計算按鈕
if st.button('計算總獎金'):
    total_bonus = calculate_total_bonus(personnel_type, position, achievement_rate, performance_rate, accumulated_bonus, region, greater_than_3_months if personnel_type == '保障人員' else None)
    st.write(f'總獎金: {total_bonus:.2f}')

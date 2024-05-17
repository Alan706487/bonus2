import pandas as pd
import streamlit as st
from datetime import datetime

# 設定 Streamlit 的網頁標題
st.title('當月獎金計算器')
# 設定 Streamlit 的網頁副標題 說明計算器適用限制
st.write('*台灣區非保障一般職員，排除海外部、定製部*')
# # 加入計算規則說明
# st.image(r'logic0514.png')


# 創建年、月調整乘數對照表
# m1 = 指標月份調整乘數
# m2 = 成果月份調整乘數
adj_data = {
    '年': [2024]*12 + [2025]*12,
    '月份': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'm2': [0, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3]
}
adj_df = pd.DataFrame(adj_data)


# 新增年份的函數 先創造新的年資料表格再按axis=0按照相同欄位合併
def add_year_data(df, year, m1_data, m2_data):
    new_data = {
        '年': [year] * 12,
        '月份': list(range(1, 13)),
        'm1': m1_data,
        'm2': m2_data
    }
    new_df = pd.DataFrame(new_data)
    return pd.concat([df, new_df], ignore_index=True)


# 刪除年份的函數 用filter篩選出要的年份留下
def remove_year_data(df, year):
    return df[df['年'] != year]


# # 新增2026年的數據
# m1_2026 = [1] * 12
# m2_2026 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# adj_df = add_year_data(adj_df, 2026, m1_2026, m2_2026)
#
# # 刪除2024年的數據
# adj_df = remove_year_data(adj_df, 2024)


# 年、月份選擇框 確保未輸入時是目前月份
# 獲取當前年和月
current_year = datetime.now().year
current_month = datetime.now().month
year = st.selectbox('選擇年份', adj_df['年'].unique(), index=adj_df['年'].tolist().index(current_year))
month = st.selectbox('選擇月份', adj_df['月份'].unique(), index=current_month-1)


# 定義提取m1、m2的函式
def get_m_values():
    m1_m2_data = adj_df[(adj_df['年'] == year) & (adj_df['月份'] == month)]  # adj_df[(adj_df['年'] == year) & (adj_df['月份'] == month)]返回df 賦值給m1_m2_data
    return m1_m2_data['m1'].values[0], m1_m2_data['m2'].values[0]  # 指定m1_m2_data特定欄位 再取出第一列數值(只有一列)


# 獲取 m1 和 m2 值
m1, m2 = get_m_values()


# 測試结果
# st.write(f'您選擇的是：{year} 年 {month} 月')
# st.write(f'm1 值：{m1}')
# st.write(f'm2 值：{m2}')


# 創建職位的獎金參數對照表
data = {
    '區域': ['北', '中南', '北', '中南', '北', '中南', '北', '中南', '北', '中南', '北', '中南'],
    '職位': ['業務', '業務', '區域業務', '區域業務', '電訪', '電訪', '產品顧問', '產品顧問', '高級顧問', '高級顧問', '資深顧問', '資深顧問'],
    '職位份額': [22000, 21000, 24000, 23000, 14000, 13000, 16000, 15000, 20000, 19000, 18000, 17000],
    '指標占比': [0.3, 0.3, 0.3, 0.3, 1, 1, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
    '成果占比': [0.7, 0.7, 0.7, 0.7, 0, 0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    '指標倍數': [1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3],
    '成果倍數': [3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3]
}
positions_df = pd.DataFrame(data)

# 透過下拉選單讓使用者選擇職位
region = st.selectbox("選擇區域", positions_df['區域'].unique())
position = st.selectbox('選擇職位', positions_df['職位'].unique())  # positions_df['職位'].unique()


# 使用者輸入指標達成率，轉換成百分比形式，預設值100%，再除以100轉化為實際數值
indicator_ach_rate = st.number_input('指標達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
# 使用者輸入成果達成率，轉換成百分比形式
perform_ach_rate = st.number_input('成果達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
# 使用者輸入當季累積成果獎金
accumulated_bonus = st.number_input('當季累積成果獎金(累積獎金)', min_value=0, value=0)  # 可指定step=1000讓使用者一次調整1000


# 定義獎金參數提取函式
def get_bonus_values():
    bonus_data = positions_df[(positions_df['區域'] == region) & (positions_df['職位'] == position)]
    return bonus_data['職位份額'].values[0], bonus_data['指標占比'].values[0], bonus_data['成果占比'].values[0], bonus_data['指標倍數'].values[0], bonus_data['成果倍數'].values[0]


# 獲取特定職位的各獎金參數
position_quota, indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values()


# 獎金計算公式(加入月份調整參數)
def calculate_total_bonus():
    indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate-1)) * m1
    perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate-1)) * m2
    total_bonus = indicator_bonus + max(0, perform_bonus - accumulated_bonus)
    return total_bonus, indicator_bonus, perform_bonus


# 獲取總將金與其組成
total_bonus, indicator_bonus, perform_bonus = calculate_total_bonus()


# 判斷成果獎金(已調整)與累積獎金差額與零大小，返回比較運算子
perform_bonus_accumulated_bonus_diff = perform_bonus - accumulated_bonus


def compare_differ():
    if perform_bonus_accumulated_bonus_diff > 0:
        return ">"
    elif perform_bonus_accumulated_bonus_diff < 0:
        return "<"
    else:
        return "="


# 下方顯示文字
# 月份調整乘數
st.write(f'您選擇的是：{year} 年 {month} 月')
st.write(f"<span style='font-size:25px'>**月份調整乘數**</span>", unsafe_allow_html=True)
st.write(f"指標月份調整乘數 = {m1} , 成果月份調整乘數 = {m2}")


# 輸出提取結果
st.write(f"<span style='font-size:25px'>**獎金參數值**</span>", unsafe_allow_html=True)
st.write(f"職位份額 = {position_quota} , 指標占比 = {indicator_per} , 成果占比 = {perform_per} , 指標倍數 = {indicator_multi} , 成果倍數 = {perform_multi}")


# 輸出計算過程與總獎金
st.write(f"<span style='font-size:25px'>**計算過程**</span>", unsafe_allow_html=True)
st.write(f"指標獎金: {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = {indicator_bonus:.0f}")
st.write(f"成果獎金: {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = {perform_bonus:.0f}")


st.write(f"成果獎金 - 累積獎金 = {perform_bonus:.0f} - {accumulated_bonus} = {perform_bonus_accumulated_bonus_diff:.0f} {compare_differ()} 0")
st.write(f"<span style='font-size:35px'>**總獎金: {total_bonus:.0f}**</span>", unsafe_allow_html=True)



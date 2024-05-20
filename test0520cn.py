import pandas as pd
import streamlit as st
from datetime import datetime


# 設定 Streamlit 的網頁標題
st.title('當月獎金計算器')
# 設定 Streamlit 的網頁副標題 說明計算器適用限制
st.write('*台灣區非保障一般職員，排除海外部、定製部*')

# 創建年、月調整乘數對照表
adj_data = {
    '年': [2024] * 12 + [2025] * 12,
    '月份': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'm2': [0, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3]
}
adj_df = pd.DataFrame(adj_data)

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

# 獲取當前年和月
current_year = datetime.now().year
current_month = datetime.now().month

# 定義提取m1、m2的函式
def get_m_values(year, month):
    m1_m2_data = adj_df[(adj_df['年'] == year) & (adj_df['月份'] == month)]
    return m1_m2_data['m1'].values[0], m1_m2_data['m2'].values[0]


# 定義獎金參數提取函式
def get_bonus_values(region, position):
    bonus_data = positions_df[(positions_df['區域'] == region) & (positions_df['職位'] == position)]
    return bonus_data['職位份額'].values[0], bonus_data['指標占比'].values[0], bonus_data['成果占比'].values[0], \
           bonus_data['指標倍數'].values[0], bonus_data['成果倍數'].values[0]


# 定義獎金計算函式
def calculate_total_bonus(position_quota, indicator_per, perform_per, indicator_multi, perform_multi,
                          indicator_ach_rate, perform_ach_rate, accumulated_bonus, m1, m2):
    indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1
    perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2
    total_bonus = indicator_bonus + max(0, perform_bonus - accumulated_bonus)
    return total_bonus, indicator_bonus, perform_bonus


# 使用四列布局(年分、月份、區域、職位選擇欄)
col1, col2, col3, col4 = st.columns(4)
with col1:
    year = st.selectbox('選擇年份', adj_df['年'].unique(), index=adj_df['年'].tolist().index(current_year))
with col2:
    month = st.selectbox('選擇月份', adj_df['月份'].unique(), index=current_month - 1)
with col3:
    region = st.selectbox("選擇區域", positions_df['區域'].unique())
with col4:
    position = st.selectbox('選擇職位', positions_df['職位'].unique())

# 獲取 m1 和 m2 值
m1, m2 = get_m_values(year, month)

# 獲取特定職位的各獎金參數
position_quota, indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values(region, position)

# 使用兩列布局(指標、成果獎金計算過程在右邊)
col1, col2 = st.columns(2)


# 第一列放使用者輸入(左邊)
with col1:
    indicator_ach_rate = st.number_input('指標達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
    perform_ach_rate = st.number_input('成果達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
    accumulated_bonus = st.number_input('當季累積成果獎金(累積獎金)', min_value=0, value=0)

# 第二列放計算結果(右邊)
with col2:
    st.write(" ")
    st.write(" ")
    st.write(
        f"<span style='font-size:16px'>指標獎金: {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = "
        f"{position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1:.0f}</span>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(
        f"<span style='font-size:16px'>成果獎金: {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = "
        f"{position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2:.0f}</span>", unsafe_allow_html=True)

    # 獲取總獎金與其組成
    total_bonus, indicator_bonus, perform_bonus = calculate_total_bonus(position_quota, indicator_per, perform_per, indicator_multi, perform_multi,
                                                                        indicator_ach_rate, perform_ach_rate, accumulated_bonus, m1, m2)
    st.write(" ")
    st.write("")
    st.write(f"<span style='font-size:35px'>**總獎金: {total_bonus:.0f}**</span>", unsafe_allow_html=True)


# # 使用兩列布局(指標、成果達成率左右擺放)
# col1, col2 = st.columns(2)
#
# # 第一列放使用者輸入 指標達成率
# with col1:
#     indicator_ach_rate = st.number_input('指標達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
#
# # 第二列放使用者輸入 成果達成率
# with col2:
#     perform_ach_rate = st.number_input('成果達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
#
# # 使用兩列布局(指標、成果獎金在達成率下方)
# col1, col2 = st.columns(2)
# with col1:
#     st.write(
#     f"<span style='font-size:16px'>指標獎金: {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = "
#     f"{position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1:.0f}</span>", unsafe_allow_html=True)
# with col2:
#     st.write(
#    f"<span style='font-size:16px'>成果獎金: {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = "
#     f"{position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2:.0f}</span>", unsafe_allow_html=True)
# accumulated_bonus = st.number_input('當季累積成果獎金(累積獎金)', min_value=0, value=0)


# # 獲取總獎金與其組成
# total_bonus, indicator_bonus, perform_bonus = calculate_total_bonus(position_quota, indicator_per, perform_per, indicator_multi, perform_multi,
# indicator_ach_rate, perform_ach_rate, accumulated_bonus, m1, m2)
# st.write(f"<span style='font-size:35px'>**總獎金: {total_bonus:.0f}**</span>", unsafe_allow_html=True)


# 使用expander隱藏詳細過程
with st.expander("點擊查看詳細過程"):
    st.write(f'您選擇的是：{year} 年 {month} 月')
    st.write(f"<span style='font-size:25px'>**月份調整乘數**</span>", unsafe_allow_html=True)
    st.write(f"指標月份調整乘數 = {m1} , 成果月份調整乘數 = {m2}")
    st.write(f"<span style='font-size:25px'>**獎金參數值**</span>", unsafe_allow_html=True)
    st.write(
        f"職位份額 = {position_quota} , 指標占比 = {indicator_per} , 成果占比 = {perform_per} , 指標倍數 = {indicator_multi} , 成果倍數 = {perform_multi}")

    # 判斷成果獎金(已調整)與累積獎金差額與零大小，返回比較運算子
    perform_bonus_accumulated_bonus_diff = perform_bonus - accumulated_bonus
    def compare_differ(diff):
        if diff > 0:
            return ">"
        elif diff < 0:
            return "<"
        else:
            return "="

    st.write(f"<span style='font-size:25px'>**計算過程**</span>", unsafe_allow_html=True)
    st.write(
        f"<span style='font-size:16px'>指標獎金 = 職位份額×指標占比×[1+指標倍數×(指標達成率-1)]×指標月份調整乘數</span>",
        unsafe_allow_html=True)
    st.write(
        f"<span style='font-size:16px'> = {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = "
        f"{indicator_bonus:.0f}</span>", unsafe_allow_html=True)
    st.write(
        f"<span style='font-size:16px'>成果獎金 = 職位份額×成果占比×[1+成果倍數×(成果達成率-1)]×成果月份調整乘數</span>",
        unsafe_allow_html=True)
    st.write(
        f"<span style='font-size:16px'> = {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = "
        f"{perform_bonus:.0f}</span>", unsafe_allow_html=True)
    st.write(
        f"成果獎金 - 累積獎金 = {perform_bonus:.0f} - {accumulated_bonus} = {perform_bonus_accumulated_bonus_diff:.0f} {compare_differ(perform_bonus_accumulated_bonus_diff)} 0")
    st.write(f"<span style='font-size:18px'>***總獎金 = 指標獎金 + max(0, 成果獎金 - 累積獎金) = "
             f"{indicator_bonus:.0f} + {max(0, perform_bonus_accumulated_bonus_diff):.0f} = {total_bonus:.0f}***</span>", unsafe_allow_html=True)



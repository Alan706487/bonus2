# # import pandas as pd
# # import streamlit as st
# #
# # st.title('當月獎金計算器')
# # st.write('*台灣區非保障一般職員，排除海外部、定制部*')
# #
# # # 創建年、月調整乘數對照表
# # adj_data = {
# #     '年': [2024]*12 + [2025]*12,
# #     '月份': list(range(1, 13)) * 2,
# #     'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# #     'm2': [0, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# # }
# # adj_df = pd.DataFrame(adj_data)
# #
# # # 創建職位的獎金參數對照表
# # data = {
# #     '區域': ['北', '中南', '北', '中南', '北', '中南', '北', '中南', '北', '中南', '北', '中南'],
# #     '職位': ['業務', '業務', '區域業務', '區域業務', '電訪', '電訪', '產品顧問', '產品顧問', '高級顧問', '高級顧問', '資深顧問', '資深顧問'],
# #     '職位份額': [22000, 21000, 24000, 23000, 14000, 13000, 16000, 15000, 20000, 19000, 18000, 17000],
# #     '指標占比': [0.3, 0.3, 0.3, 0.3, 1, 1, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
# #     '成果占比': [0.7, 0.7, 0.7, 0.7, 0, 0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
# #     '指標倍數': [1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3],
# #     '成果倍數': [3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3]
# # }
# # positions_df = pd.DataFrame(data)
# #
# # # 定義函式
# # def get_m_values():
# #     m1_m2_data = adj_df[(adj_df['年'] == year) & (adj_df['月份'] == month)]
# #     return m1_m2_data['m1'].values[0], m1_m2_data['m2'].values[0]
# #
# # def get_bonus_values():
# #     bonus_data = positions_df[(positions_df['區域'] == region) & (positions_df['職位'] == position)]
# #     return bonus_data['職位份額'].values[0], bonus_data['指標占比'].values[0], bonus_data['成果占比'].values[0], bonus_data['指標倍數'].values[0], bonus_data['成果倍數'].values[0]
# #
# # def calculate_total_bonus():
# #     indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate-1)) * m1
# #     perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate-1)) * m2
# #     total_bonus = indicator_bonus + max(0, perform_bonus - accumulated_bonus)
# #     return total_bonus, indicator_bonus, perform_bonus
# #
# # def compare_differ():
# #     if perform_bonus_accumulated_bonus_diff > 0:
# #         return ">"
# #     elif perform_bonus_accumulated_bonus_diff < 0:
# #         return "<"
# #     else:
# #         return "="
# #
# # # 使用 st.form() 創建一個表單
# # with st.form(key='bonus_calculator'):
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         year = st.selectbox('選擇年份', adj_df['年'].unique())
# #         month = st.selectbox('選擇月份', adj_df['月份'].unique())
# #         region = st.selectbox("選擇區域", positions_df['區域'].unique())
# #         position = st.selectbox('選擇職位', positions_df['職位'].unique())
# #     with col2:
# #         indicator_ach_rate = st.number_input('指標達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
# #         perform_ach_rate = st.number_input('成果達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
# #         accumulated_bonus = st.number_input('當季累積成果獎金(累積獎金)', min_value=0, value=0)
# #
# #     submit_button = st.form_submit_button(label='計算獎金')
# #
# # # 在表單提交後顯示計算結果
# # if submit_button:
# #     m1, m2 = get_m_values()
# #     position_quota, indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values()
# #     total_bonus, indicator_bonus, perform_bonus = calculate_total_bonus()
# #     perform_bonus_accumulated_bonus_diff = perform_bonus - accumulated_bonus
# #
# #     with st.expander("查看詳細計算過程"):
# #         st.write(f'您選擇的是：{year} 年 {month} 月')
# #         st.write(f"月份調整乘數")
# #         st.write(f"指標月份調整乘數 = {m1} , 成果月份調整乘數 = {m2}")
# #         st.write(f"獎金參數值")
# #         st.write(f"職位份額 = {position_quota} , 指標占比 = {indicator_per} , 成果占比 = {perform_per} , 指標倍數 = {indicator_multi} , 成果倍數 = {perform_multi}")
# #         st.write(f"計算過程")
# #         st.write(f"指標獎金: {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = {indicator_bonus:.0f}")
# #         st.write(f"成果獎金: {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = {perform_bonus:.0f}")
# #         st.write(f"成果獎金 - 累積獎金 = {perform_bonus:.0f} - {accumulated_bonus} = {perform_bonus_accumulated_bonus_diff:.0f} {compare_differ()} 0")
# #
# #     st.markdown(f"<h2 style='text-align: center;'>總獎金: {total_bonus:.0f}</h2>", unsafe_allow_html=True)
#
#
# # --
#
import pandas as pd
import streamlit as st

st.title('當月獎金計算器')
st.write('*台灣區非保障一般職員，排除海外部、定制部*')

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
    '職位': ['業務', '業務', '區域業務', '區域業務', '電訪', '電訪', '產品顧問', '產品顧問', '高級顧問', '高級顧問',
             '資深顧問', '資深顧問'],
    '職位份額': [22000, 21000, 24000, 23000, 14000, 13000, 16000, 15000, 20000, 19000, 18000, 17000],
    '指標占比': [0.3, 0.3, 0.3, 0.3, 1, 1, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
    '成果占比': [0.7, 0.7, 0.7, 0.7, 0, 0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    '指標倍數': [1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3],
    '成果倍數': [3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3]
}
positions_df = pd.DataFrame(data)


# 定義函式
def get_m_values():
    m1_m2_data = adj_df[(adj_df['年'] == year) & (adj_df['月份'] == month)]
    return m1_m2_data['m1'].values[0], m1_m2_data['m2'].values[0]


def get_bonus_values():
    bonus_data = positions_df[(positions_df['區域'] == region) & (positions_df['職位'] == position)]
    return bonus_data['職位份額'].values[0], bonus_data['指標占比'].values[0], bonus_data['成果占比'].values[0], \
    bonus_data['指標倍數'].values[0], bonus_data['成果倍數'].values[0]


def calculate_total_bonus():
    indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1
    perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2
    total_bonus = indicator_bonus + max(0, perform_bonus - accumulated_bonus)
    return total_bonus, indicator_bonus, perform_bonus


def compare_differ():
    if perform_bonus_accumulated_bonus_diff > 0:
        return ">"
    elif perform_bonus_accumulated_bonus_diff < 0:
        return "<"
    else:
        return "="

#
# # 輸入欄位
# col1, col2 , col3 = st.columns(3)
# with col1:
#     year = st.selectbox('選擇年份', adj_df['年'].unique())
#     month = st.selectbox('選擇月份', adj_df['月份'].unique())
# with col2:
#     region = st.selectbox("選擇區域", positions_df['區域'].unique())
#     position = st.selectbox('選擇職位', positions_df['職位'].unique())
# with col3:
#     indicator_ach_rate = st.number_input('指標達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
#     perform_ach_rate = st.number_input('成果達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
#     accumulated_bonus = st.number_input('當季累積成果獎金(累積獎金)', min_value=0, value=0)

# 獲取計算所需的參數值
m1, m2 = get_m_values()
position_quota, indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values()
total_bonus, indicator_bonus, perform_bonus = calculate_total_bonus()

col1, col2 = st.columns(2)
with col1:
    year = st.selectbox('選擇年份', adj_df['年'].unique())
    month = st.selectbox('選擇月份', adj_df['月份'].unique())
    region = st.selectbox("選擇區域", positions_df['區域'].unique())
    position = st.selectbox('選擇職位', positions_df['職位'].unique())
with col2:
    indicator_ach_rate = st.number_input('指標達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
    st.write(f"指標獎金: {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = {indicator_bonus:.0f}")
    perform_ach_rate = st.number_input('成果達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
    accumulated_bonus = st.number_input('當季累積成果獎金(累積獎金)', min_value=0, value=0)
perform_bonus_accumulated_bonus_diff = perform_bonus - accumulated_bonus


# 顯示計算結果
st.markdown(f"<h2 style='text-align: center;'>總獎金: {total_bonus:.0f}</h2>", unsafe_allow_html=True)

# 折疊部分顯示詳細信息
with st.expander("查看詳細信息"):
    st.write(f'您選擇的是：{year} 年 {month} 月')
    st.write(f"月份調整乘數：指標月份調整乘數 = {m1} , 成果月份調整乘數 = {m2}")

    st.write(f"獎金參數值")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(f"職位份額 = {position_quota}")
    with col2:
        st.write(f"指標占比 = {indicator_per}")
    with col3:
        st.write(f"成果占比 = {perform_per}")
    with col4:
        st.write(f"指標倍數 = {indicator_multi}")
    with col5:
        st.write(f"成果倍數 = {perform_multi}")

    st.write(f"計算過程")
    st.write(
        f"指標獎金: {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = {indicator_bonus:.0f}")
    st.write(
        f"成果獎金: {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = {perform_bonus:.0f}")
    st.write(
        f"成果獎金 - 累積獎金 = {perform_bonus:.0f} - {accumulated_bonus} = {perform_bonus_accumulated_bonus_diff:.0f} {compare_differ()} 0")

#
# import pandas as pd
# import streamlit as st
#
# st.title('當月獎金計算器')
# st.write('*台灣區非保障一般職員，排除海外部、定制部*')
#
# # 創建年、月調整乘數對照表
# adj_data = {
#     '年': [2024]*12 + [2025]*12,
#     '月份': list(range(1, 13)) * 2,
#     'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     'm2': [0, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# }
# adj_df = pd.DataFrame(adj_data)
#
# # 創建職位的獎金參數對照表
# data = {
#     '區域': ['北', '中南', '北', '中南', '北', '中南', '北', '中南', '北', '中南', '北', '中南'],
#     '職位': ['業務', '業務', '區域業務', '區域業務', '電訪', '電訪', '產品顧問', '產品顧問', '高級顧問', '高級顧問', '資深顧問', '資深顧問'],
#     '職位份額': [22000, 21000, 24000, 23000, 14000, 13000, 16000, 15000, 20000, 19000, 18000, 17000],
#     '指標占比': [0.3, 0.3, 0.3, 0.3, 1, 1, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
#     '成果占比': [0.7, 0.7, 0.7, 0.7, 0, 0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
#     '指標倍數': [1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3],
#     '成果倍數': [3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3]
# }
# positions_df = pd.DataFrame(data)
#
# # 定義函式
# def get_m_values():
#     m1_m2_data = adj_df[(adj_df['年'] == year) & (adj_df['月份'] == month)]
#     return m1_m2_data['m1'].values[0], m1_m2_data['m2'].values[0]
#
# def get_bonus_values():
#     bonus_data = positions_df[(positions_df['區域'] == region) & (positions_df['職位'] == position)]
#     return bonus_data['職位份額'].values[0], bonus_data['指標占比'].values[0], bonus_data['成果占比'].values[0], bonus_data['指標倍數'].values[0], bonus_data['成果倍數'].values[0]
#
# def calculate_total_bonus():
#     indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate-1)) * m1
#     perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate-1)) * m2
#     total_bonus = indicator_bonus + max(0, perform_bonus - accumulated_bonus)
#     return total_bonus, indicator_bonus, perform_bonus
#
# def compare_differ():
#     if perform_bonus_accumulated_bonus_diff > 0:
#         return ">"
#     elif perform_bonus_accumulated_bonus_diff < 0:
#         return "<"
#     else:
#         return "="
#
# # 在側邊欄中放置輸入欄位
# st.sidebar.header('輸入參數')
# year = st.sidebar.selectbox('選擇年份', adj_df['年'].unique())
# month = st.sidebar.selectbox('選擇月份', adj_df['月份'].unique())
# region = st.sidebar.selectbox("選擇區域", positions_df['區域'].unique())
# position = st.sidebar.selectbox('選擇職位', positions_df['職位'].unique())
# indicator_ach_rate = st.sidebar.number_input('指標達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
# perform_ach_rate = st.sidebar.number_input('成果達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
# accumulated_bonus = st.sidebar.number_input('當季累積成果獎金(累積獎金)', min_value=0, value=0)
#
# # 獲取計算所需的參數值
# m1, m2 = get_m_values()
# position_quota, indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values()
# total_bonus, indicator_bonus, perform_bonus = calculate_total_bonus()
# perform_bonus_accumulated_bonus_diff = perform_bonus - accumulated_bonus
#
#
#
# st.write(f'您選擇的是：{year} 年 {month} 月')
# st.write(f"月份調整乘數：指標月份調整乘數 = {m1} , 成果月份調整乘數 = {m2}")
#
# st.write(f"獎金參數值")
# col1, col2, col3, col4, col5 = st.columns(5)
# with col1:
#     st.write(f"職位份額 = {position_quota}")
# with col2:
#     st.write(f"指標占比 = {indicator_per}")
# with col3:
#     st.write(f"成果占比 = {perform_per}")
# with col4:
#     st.write(f"指標倍數 = {indicator_multi}")
# with col5:
#     st.write(f"成果倍數 = {perform_multi}")
#
# st.write(f"計算過程")
# st.write(
#     f"指標獎金: {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = {indicator_bonus:.0f}")
# st.write(
#     f"成果獎金: {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = {perform_bonus:.0f}")
# st.write(
#     f"成果獎金 - 累積獎金 = {perform_bonus:.0f} - {accumulated_bonus} = {perform_bonus_accumulated_bonus_diff:.0f} {compare_differ()} 0")
#
# # 在主頁面顯示計算結果
# st.markdown(f"<h2 style='text-align: center;'>總獎金: {total_bonus:.0f}</h2>", unsafe_allow_html=True)


# # 在側邊欄中顯示詳細計算過程
# st.sidebar.header('詳細計算過程')
# st.sidebar.write(f'您選擇的是：{year} 年 {month} 月')
# st.sidebar.write(f"月份調整乘數：指標月份調整乘數 = {m1} , 成果月份調整乘數 = {m2}")
#
# st.sidebar.write(f"獎金參數值")
# st.sidebar.write(f"職位份額 = {position_quota}")
# st.sidebar.write(f"指標占比 = {indicator_per}")
# st.sidebar.write(f"成果占比 = {perform_per}")
# st.sidebar.write(f"指標倍數 = {indicator_multi}")
# st.sidebar.write(f"成果倍數 = {perform_multi}")
#
# st.sidebar.write(f"計算過程")
# st.sidebar.write(f"指標獎金: {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = {indicator_bonus:.0f}")
# st.sidebar.write(f"成果獎金: {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = {perform_bonus:.0f}")
# st.sidebar.write(f"成果獎金 - 累積獎金 = {perform_bonus:.0f} - {accumulated_bonus} = {perform_bonus_accumulated_bonus_diff:.0f} {compare_differ()} 0")
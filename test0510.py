import pandas as pd
import streamlit as st

# 建立職位相關的 DataFrame，包括職位名稱、職位份額、指標占比、成果占比與指標倍數、成果倍數
# data = {
#     '職位': ['北業務', '南業務', '北區域業務', '南區域業務', '北電訪', '南電訪', '北產品顧問', '南產品顧問',
#              '北高級顧問', '南高級顧問', '北資深顧問', '南資深顧問'],
#     '職位份額': [22000, 21000, 24000, 23000, 14000, 13000, 16000, 15000, 20000, 19000, 18000, 17000],
#     '指標占比': [0.3, 0.3, 0.3, 0.3, 1, 1, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
#     '成果占比': [0.7, 0.7, 0.7, 0.7, 0, 0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
#     '指標倍數': [1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3],
#     '成果倍數': [3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3]  # 新增
# }

# 创建对照表数据
data = {
    '年': [2024]*12 + [2025]*12,
    '月份': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'm2': [0, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3]
}

# 转换为 DataFrame
df = pd.DataFrame(data)


# 定义函数来提取 m1 和 m2 值
def get_m_values(year, month):
    result = df[(df['年'] == year) & (df['月份'] == month)]
    if not result.empty:
        m1 = result['m1'].values[0]
        m2 = result['m2'].values[0]
        return m1, m2
    else:
        return None, None

# Streamlit 应用
# st.title('选择年份和月份以获取对应的 m1 和 m2 值')


# 年份选择框
year = st.selectbox('选择年份', df['年'].unique())

# 月份选择框
month = st.selectbox('选择月份', df['月份'].unique())

# 获取 m1 和 m2 值
m1, m2 = get_m_values(year, month)

# 显示结果
if m1 is not None and m2 is not None:
    st.write(f'您选择的是：{year} 年 {month} 月')
    st.write(f'm1 值：{m1}')
    st.write(f'm2 值：{m2}')
else:
    st.write('找不到对应的数据')

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

# # 建立地區相關的 DataFrame，包括地區名稱與對應的成果倍數
# regions_data = {
#     '地區': ['台新馬', '其他'],
#     '成果倍數': [3, 1]
# }
# regions_df = pd.DataFrame(regions_data)

# 導入模組
# import streamlit as st
# from args import *  # 導入args.py中data、positions_df、regions_df

# 設定 Streamlit 的網頁標題
st.title('當月獎金計算器')
# 設定 Streamlit 的網頁副標題 說明計算器適用限制
st.write('*台灣區非保障一般職員，排除海外部、定製部*')

# 加入公式說明圖片
# st.image(r'C:\Users\11021249\Desktop\alan\logic.png')  # 複製絕對路徑完前面加r就不用取改裡面斜線
st.image(r'logic.png')  # 複製絕對路徑完前面加r就不用取改裡面斜線

# 加入對應的獎金參數設定表格
st.sidebar.write("**獎金參數設定**")  # 粗體
st.sidebar.write(positions_df)
# st.sidebar.write(regions_df)

adj_data = pd.DataFrame({
    '年度'
})
year = st.selectbox('年度', range(2024, 2026))
month = st.selectbox('月份', range(1, 13))
# selected_month = st.slider("選擇月份", 1, 12, 1)
# st.write(2*selected_month)
# # months = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]





# 透過下拉選單讓使用者選擇職位
position = st.selectbox('選擇職位', positions_df['職位'].unique())  # positions_df['職位'].unique()
region = st.selectbox("選擇區域", positions_df['區域'].unique())
# 透過下拉選單讓使用者選擇服務地區
# region = st.selectbox('服務地區', regions_df['地區'])

# 使用者輸入指標達成率，轉換成百分比形式，預設值100%，再除以100轉化為實際數值
achievement_rate = st.number_input('指標達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
# 使用者輸入成果達成率，轉換成百分比形式
performance_rate = st.number_input('成果達成率（輸入百分比值，例如150表示150%）', min_value=0, value=100) / 100
# 使用者輸入當季累積成果獎金
accumulated_bonus = st.number_input('當季累積成果獎金(累積獎金)', min_value=0, value=0)  # 可指定step=1000讓使用者一次調整1000


# position, achievement_rate, performance_rate, accumulated_bonus, region
# 定義計算總獎金的函式 return總獎金值total_bonus
def calculate_total_bonus():
    # 從 DataFrame 中根據職位獲取相關數據 過濾遮罩寫法
    #  positions_df['職位'] == position 返回布林series
    #  positions_df[positions_df['職位'] == position] 返回符合特定職位的行，是橫dataframe
    #  .iloc[0]返回索引為0的行 是直series
    position_data = positions_df[positions_df['職位'] == position].iloc[0]
    # 從 DataFrame 中根據地區獲取成果倍數
    #  .values[0]用來取得所選取的「成果倍數」欄位的第一個值
    # region_multiplier = regions_df[regions_df['地區'] == region]['成果倍數'].values[0]

    # 計算指標獎金
    # position_data 是series 看作字典 key是職位、職務份額.. value是北業務、22000.. 所以可以直接用key取出value
    indicator_bonus = position_data['職位份額'] * position_data['指標占比'] * (
                1 + position_data['指標倍數'] * (achievement_rate - 1)) * m1
    # 計算成果獎金
    # performance_bonus = position_data['職務份額'] * position_data['成果占比'] * (
    #             1 + region_multiplier * (performance_rate - 1))
    performance_bonus = position_data['職位份額'] * position_data['成果占比'] * (
            1 + position_data['成果倍數'] * (performance_rate - 1)) * m2

    # 計算總獎金，當成果獎金減去累積獎金為負時，總獎金為指標獎金
    total_bonus = indicator_bonus + max(0, performance_bonus - accumulated_bonus)
    return total_bonus, indicator_bonus, performance_bonus, position_data
    # return total_bonus

# calculate_total_bonus_result = calculate_total_bonus()


# 當使用者點擊計算按鈕時，進行獎金計算並顯示結果
# 如果想指定 Streamlit 的 port 埠號，只要在後方加上--server.port 參數：streamlit run <py程式檔案路徑> --server.port 8888
# if st.button('計算總獎金'):
#     # total_bonus = calculate_total_bonus()
#     # 使用格式化輸出，四捨五入到整數位
#     # st.write(f'總獎金: {total_bonus:.0f}')
#
    # st.write(f"<span style='font-size:25px'>*指標獎金: {calculate_total_bonus()[1]:.0f}*</span>", unsafe_allow_html=True )
#     st.write(f"<span style='font-size:25px'>*成果獎金: {calculate_total_bonus()[2]:.0f}*</span>",
#              unsafe_allow_html=True)
#     st.write(f"<span style='font-size:30px'>**總獎金: {calculate_total_bonus()[0]:.0f}**</span>",
#              unsafe_allow_html=True)
#
#     # st.write(f'**成果獎金: {calculate_total_bonus()[2]:.0f}**')
#     # st.write(f'**總獎金: {calculate_total_bonus()[0]:.0f}**')
#
# # st.write("<span style='font-size:30px'>這是放大的文字</span>", unsafe_allow_html=True)
# # st.write("<span style='font-size:15px'>這是放大的文字</span>", unsafe_allow_html=True)
# #
# # st.write("這是放大的文本", "<big>這是放大的文本</big>", unsafe_allow_html=True)
# # st.write("這是縮小的文本", "<small>這是縮小的文本</small>", unsafe_allow_html=True)
# # # --server.address 192.168.1.62

# 當使用者輸入數據變化時，自動計算獎金
total_bonus, indicator_bonus, performance_bonus, position_data = calculate_total_bonus()
# st.write(f"指標獎金: {indicator_bonus:.0f}*{position_data['職位份額']}")
st.write(f"職位份額 = {position_data['職位份額']} , 指標占比 = {position_data['指標占比']} , 指標倍數 = {position_data['指標倍數']} , 指標月份調整乘數 = {m1} , 成果月份調整乘數 = {m2}")
st.write(f"指標獎金: {position_data['職位份額']} * {position_data['指標占比']} * [1 + {position_data['指標倍數']} * ({achievement_rate} - 1) ]* {m1} = {indicator_bonus:.0f}")
st.write(f"成果獎金: {position_data['職位份額']} * {position_data['成果占比']} * [1 + {position_data['指標倍數']} * ({achievement_rate} - 1) ]* {m1} = {indicator_bonus:.0f}")

# st.write(f"成果獎金: {performance_bonus:.0f}")
st.write(f"**總獎金: {total_bonus:.0f}**")

# indicator_bonus = position_data['職位份額'] * position_data['指標占比'] * (
#                 1 + position_data['指標倍數'] * (achievement_rate - 1))

# df = {
#     'year': [2024, 2025]
# }


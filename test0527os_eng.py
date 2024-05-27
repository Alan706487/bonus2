import pandas as pd
import streamlit as st
from datetime import datetime
from decimal import Decimal

# 為了之後要自由配置版面的顯示大小，預設用到全部版面
st.set_page_config(layout="wide")

# 創建海外(在台)的年、月調整乘數對照表  1、2月過年
adj_df_ost = pd.DataFrame({
    'Year': [2024] * 12 + [2025] * 12,
    'Month': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年
    'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建新加坡的年、月調整乘數對照表  1、2月過年
adj_df_sig = pd.DataFrame({
    'Year': [2024] * 12 + [2025] * 12,
    'Month': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年
    'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建馬來西亞的年、月調整乘數對照表  1、2月過年
adj_df_mal = pd.DataFrame({
    'Year': [2024] * 12 + [2025] * 12,
    'Month': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年
    'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建菲律賓的年、月調整乘數對照表  12、1月過年
adj_df_phi = pd.DataFrame({
    'Year': [2024] * 12 + [2025] * 12,
    'Month': list(range(1, 13)) * 2,
    'm1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # 假設海外1月過年
    'm2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
})

# 創建印度的年、月調整乘數對照表  10、11月過年
adj_df_india = pd.DataFrame({
    'Year': [2024] * 12 + [2025] * 12,
    'Month': list(range(1, 13)) * 2,
    'm1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],  # 假設海外1月過年
    'm2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
})

# 創建印尼的年、月調整乘數對照表  3、4月過年
adj_df_indo = pd.DataFrame({
    'Year': [2024] * 12 + [2025] * 12,
    'Month': list(range(1, 13)) * 2,
    'm1': [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年
    'm2': [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建越南的年、月調整乘數對照表  1、2月過年
adj_df_viet = pd.DataFrame({
    'Year': [2024] * 12 + [2025] * 12,
    'Month': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年
    'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建泰國的年、月調整乘數對照表 4、5月過年
adj_df_thai = pd.DataFrame({
    'Year': [2024] * 12 + [2025] * 12,
    'Month': list(range(1, 13)) * 2,
    'm1': [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年
    'm2': [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 將不同區域的DataFrame存儲在字典adj_dfs中
adj_dfs = {
    'Overseas (Taiwan)': adj_df_ost,
    'Singapore': adj_df_sig,
    'Malaysia': adj_df_mal,
    'Philippines': adj_df_phi,
    'India': adj_df_india,
    'Indonesia': adj_df_indo,
    'Vietnam': adj_df_viet,
    'Thailand': adj_df_thai
}

# 創建職位的獎金參數對照表
positions_df = pd.DataFrame({
    'Region': ['Overseas (Taiwan)', 'Overseas (Taiwan)', 'Overseas (Taiwan)', 'Overseas (Taiwan)', 'Singapore', 'Singapore', 'Malaysia', 'Philippines', 'Philippines', 'Philippines', 'Philippines',
            'Indonesia', 'Indonesia', 'Indonesia', 'Indonesia', 'India', 'India', 'India', 'India', 'Vietnam', 'Vietnam', 'Vietnam', 'Vietnam', 'Thailand', 'Thailand', 'Thailand', 'Thailand'],
    'Position': [
        'Call Center Executive', 'Product Consultant', 'Junior Product Consultant', 'Senior Product Consultant', 'Sales Representative', 'Territory Sales Representative',
        'Territory Sales Representative', 'Call Center Executive', 'Product Consultant', 'Sales Representative', 'Territory Sales Representative', 'Call Center Executive',
        'Product Consultant', 'Sales Representative', 'Territory Sales Representative', 'Call Center Executive', 'Product Consultant', 'Sales Representative',
        'Territory Sales Representative', 'Call Center Executive', 'Product Consultant', 'Sales Representative', 'Territory Sales Representative', 'Call Center Executive',
        'Product Consultant', 'Sales Representative', 'Territory Sales Representative'],
    'Position Quota': [16000, 18000, 20000, 22000, 1800, 1800, 2500, 25000, 32000, 39000, 50000,
              3300000, 4100000, 4300000, 5200000, 27000, 35000, 38000, 40000, 7500000, 10000000,
              12000000, 15000000, 18000, 22000, 24000, 31000],
    'Indicator Percentage': [1, 0.7, 0.7, 0.7, 0.3, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3],
    'Performance Percentage': [0, 0.3, 0.3, 0.3, 0.7, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7],
    'Indicator Multiplier': [3, 3, 3, 3, 1, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1],
    'Performance Multiplier': [0, 1, 1, 1, 3, 3, 3, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
})

# 獲取當前年和月
current_year, current_month = datetime.now().year, datetime.now().month

# 定義提取特定區域m1、m2的新函式
@st.cache_data
def get_m_values(region, year, month):
    # adj_df = adj_df[region]
    m1_m2_data = adj_dfs[region][(adj_dfs[region]['Year'] == year) & (adj_dfs[region]['Month'] == month)]
    return m1_m2_data.iloc[0][['m1', 'm2']]  # 返回series 但分別對元素賦值後會是int

# 定義獎金參數提取函式
@st.cache_data
def get_bonus_values(region, position):
    bonus_data = positions_df[(positions_df['Region'] == region) & (positions_df['Position'] == position)]
    # return bonus_data['職位份額'].values[0], bonus_data['指標占比'].values[0], bonus_data['成果占比'].values[0], \
    #        bonus_data['指標倍數'].values[0], bonus_data['成果倍數'].values[0]
    return bonus_data.iloc[0][['Position Quota', 'Indicator Percentage', 'Performance Percentage', 'Indicator Multiplier', 'Performance Multiplier']]

# 定義海外獎金計算函式(最低50%，最高%)
lowest = 50
highest = 200

def calculate_total_bonus(position_quota, indicator_percentage, performance_percentage, indicator_multiplier, performance_multiplier,
                          indicator_ach_rate, performance_ach_rate, m1, m2):
    base_performance_bonus = position_quota * performance_percentage * m2  # 原本的成果獎金 要月份調整
    indicator_bonus = position_quota * indicator_percentage * (1 + indicator_multiplier * (indicator_ach_rate - 1)) * m1
    unadjusted_performance_bonus = position_quota * performance_percentage * (1 + performance_multiplier * (performance_ach_rate - 1)) * m2
    # 對performance_bonus進行上下限限制
    adjusted_performance_bonus = max(base_performance_bonus * (lowest/100), min(unadjusted_performance_bonus, base_performance_bonus * (highest/100)))
    total_bonus = indicator_bonus + adjusted_performance_bonus
    return base_performance_bonus, indicator_bonus, unadjusted_performance_bonus, adjusted_performance_bonus, total_bonus

# 創建區域與驗證碼的對應字典
region_codes = {
    '0': 'Overseas (Taiwan)',
    '1': 'Singapore',
    '2': 'Malaysia',
    '3': 'Philippines',
    '4': 'Indonesia',
    '5': 'India',
    '6': 'Vietnam',
    '7': 'Thailand'
    # 可以繼續添加其他區域和驗證碼
}

# 使用者輸入驗證碼 不要讓輸入框那麼長
c1, c2, c3 = st.columns((1, 0.5, 1))
with c2:
    # 使用 st.empty() 創建一个占位符
    input_placeholder = st.empty()
    # 在占位符中顯示文本输入框
    user_input = input_placeholder.text_input('Please enter your region verification code to access the calculator:', '')

# 檢查驗證碼並設定區域
if user_input in region_codes:
    region = region_codes[user_input]
    # 當用户輸入文字後，清空了佔位符，從而隐藏文本输入框
    input_placeholder.empty()

    # 以下是該區域的試算器相關代碼
    # 需要根據區域調整的參數或功能，你可以在這裡加入
    # 可以使用區域變量 `region` 來加載和顯示特定區域的數據
    # 整個網頁置中，但能自由設定比例布局
    c1, c2, c3 = st.columns((1, 2, 1))  # tw、cn 2.5
    with c2:
        # 設定 Streamlit 的網頁標題
        st.write("<h1 style='font-size: 44px;'>Simple Bonus Calculator<span style='font-size: 30px;'>(For Reference)</span></h1>", unsafe_allow_html=True)
        # 附註:*6月啟用
        st.write(f"<span style='font-size:22px'>**:red-background[*Enable in June]**</span>", unsafe_allow_html=True)
        # st.success(f"驗證成功！歡迎訪問 **{region}** 的試算器。")
        # 設定 Streamlit 的網頁副標題 說明計算器適用限制
        st.write('*Overseas Business Department*')

        # 使用四列布局(年分、月份、區域、職位選擇欄)
        # 因前面adj_dfs是dict 要用list(adj_dfs.keys())[0]保證取出第一個鍵(區域) list(adj_dfs.keys())返回所有的key包成list
        # list(adj_dfs.keys())[0] 預設取adj_dfs第一個國家且年月資料完整
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            year = st.selectbox('Select Year', adj_dfs[list(adj_dfs.keys())[0]]['Year'].unique(), index=adj_dfs[list(adj_dfs.keys())[0]]['Year'].tolist().index(current_year))  # 保證預設是目前年份
        with col2:
            month = st.selectbox('Select Month', adj_dfs[list(adj_dfs.keys())[0]]['Month'].unique(), index=current_month - 1)  # 保證預設是目前月份
        with col3:
            # region = st.selectbox("選擇區域", positions_df['區域'].unique())
            # region = st.selectbox("選擇區域", region_codes[user_input])
            # 選的東西options 要能迭代 如[region]=['泰國']才能完整取出"泰國"，只放region='泰國'，會視為兩個元素，'泰'、'國'
            region = st.selectbox("Select Region", [region])
            # 獲取 m1 和 m2 值
            m1, m2 = get_m_values(region, year, month)
        with col4:
            # 6月規則只剩產品顧問、無資深、高級顧問
            # 各國有的職位不同，要篩選出特定區域的職位讓使用者選，'同時'排除資深、高級、區域業務
            filtered_positions = positions_df[(positions_df['Region'] == region) &
                                              (positions_df['Position'] != 'Junior Product Consultant') &
                                              (positions_df['Position'] != 'Senior Product Consultant') &
                                              (positions_df['Position'] != 'Territory Sales Representative')]['Position'].unique()

            # 避免某地區沒有職位，取不到值
            if len(filtered_positions) == 0:
                # 要給以下設定否則會取不到值報錯
                position = ''
                position_quota, indicator_percentage, performance_percentage, indicator_multiplier, performance_multiplier = 0, 0, 0, 0, 0
                st.warning("No positions available for the selected region, unable to calculate bonus.")
            else:
                position = st.selectbox('Select Position', filtered_positions)
                # 獲取特定職位的各獎金參數
                position_quota, indicator_percentage, performance_percentage, indicator_multiplier, performance_multiplier = get_bonus_values(region, position)

        # 當沒有職位可以選時(選到空值時)，以下都不執行，反之都執行
        if position != '':
            col1, col2 = st.columns((1, 2))
            # 第一列放使用者輸入(左邊)
            with col1:
                st.write('<br>', unsafe_allow_html=True)  # 讓selectbox跟input達成率之間不要太擠
                indicator_ach_rate = st.text_input('Indicator Achievement Rate (%)', value='100', help='Please enter the percentage value, e.g., 131.0781 means 131.0781%')
                perform_ach_rate = st.text_input('Performance Achievement Rate (%)', value='100', help='Please enter the percentage value, e.g., 131.0781 means 131.0781%')

                # 將百分比值轉換為小數 .strip('%')確保就算使用者多輸入%符號也沒差
                indicator_ach_rate = float(Decimal(indicator_ach_rate.strip('%')) / 100)
                perform_ach_rate = float(Decimal(perform_ach_rate.strip('%')) / 100)

            # 第二列放計算結果(右邊)
            with col2:
                # 獲取當月獎金與其組成
                base_performance_bonus, indicator_bonus, unadjusted_performance_bonus, adjusted_performance_bonus, total_bonus = calculate_total_bonus(
                                                                                    position_quota, indicator_percentage,
                                                                                    performance_percentage, indicator_multiplier,
                                                                                    performance_multiplier, indicator_ach_rate,
                                                                                    perform_ach_rate, m1, m2)
                st.markdown(
                    """
                    <style>
                    .stMarkdown p {
                        margin-top: 50px;
                        margin-bottom: 50px;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
                st.write(f"<span style='font-size:21px'>**Indicator Bonus**:</span>", unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:18px'>{position_quota:,.0f} * {indicator_percentage} * [1 + {indicator_multiplier} * ({indicator_ach_rate} - 1)] * {m1} = **{indicator_bonus:,.0f}**</span>",
                    unsafe_allow_html=True)

                st.write(f"<span style='font-size:21px'>**Performance Bonus**</span>", unsafe_allow_html=True)
                if 1 + performance_multiplier * (perform_ach_rate - 1) > highest / 100:
                    st.write(
                        f"<span style='font-size:18px'>{position_quota:,.0f} * {performance_percentage} *  {highest / 100} * {m2} = **{position_quota * performance_percentage * (highest / 100) * m2:,.0f}**</span>",
                        unsafe_allow_html=True)
                elif 1 + performance_multiplier * (perform_ach_rate - 1) < lowest / 100:
                    st.write(
                        f"<span style='font-size:18px'>{position_quota:,.0f} * {performance_percentage} *  {lowest / 100} * {m2} = **{position_quota * performance_percentage * (lowest / 100) * m2:,.0f}**</span>",
                        unsafe_allow_html=True)
                else:
                    st.write(
                        f"<span style='font-size:18px'>{position_quota:,.0f} * {performance_percentage} * [1 + {performance_multiplier} * ({perform_ach_rate} - 1)] * {m2} = **{adjusted_performance_bonus:,.0f}**</span>",
                        unsafe_allow_html=True)
                st.markdown(
                    """
                    <style>
                    .stMarkdown p {
                        margin-top: 5.7px;
                        margin-bottom: 5.7px;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )

                    # if 1 + perform_multi * (perform_ach_rate - 1) > highest / 100:
                    #     st.write(
                    #         f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} *  {highest / 100} * {m2} = **{position_quota * perform_per * (highest / 100) * m2:,.0f}**</span>",
                    #         unsafe_allow_html=True)
                    # elif 1 + perform_multi * (perform_ach_rate - 1) < lowest / 100:
                    #     st.write(
                    #         f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} *  {lowest / 100} * {m2} = **{position_quota * perform_per * (lowest / 100) * m2:,.0f}**</span>",
                    #         unsafe_allow_html=True)
                    # else:
                    #     st.write(
                    #         f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = **{n_perform_bonus:,.0f}**</span>",
                    #         unsafe_allow_html=True)
                    #     # # 添加自定义CSS
                    # st.markdown(
                    #     """
                    #     <style>
                    #     .stMarkdown p {
                    #         margin-top: 5.7px;
                    #         margin-bottom: 5.7px;
                    #     }
                    #     </style>
                    #     """,
                    #     unsafe_allow_html=True,
                    # )
            # 少了累積已發獎金，調整當月獎金位置
            st.write(f"""
                <div style='text-align:center; font-size: 40px;'>
                    <strong>Monthly Bonus: {total_bonus:,.0f}</strong>
                </div>
                 """, unsafe_allow_html=True)  # 調整置中、大小、粗體
            # 附註計算限制
            st.write(f"""
                <div style='text-align: center; font-size: 15px;'>
                       *Bonus amount does not include attendance, collections, rewards and penalties, etc.
                </div>
                """, unsafe_allow_html=True)

        # 使用expander隱藏詳細過程
            with st.expander("Click to see detailed process", expanded=False):
                st.write("")
                st.write(f'You selected: {year} Year {month} Month')
                st.write(f"<span style='font-size:25px'>**Monthly Adjustment Multipliers**</span>", unsafe_allow_html=True)
                st.write(f"Indicator Monthly Adjustment Multiplier = {m1} , Performance Monthly Adjustment Multiplier = {m2}")
                st.write(f"<span style='font-size:25px'>**Bonus Parameter Values**</span>", unsafe_allow_html=True)
                st.write(
                    f"Position Quota = {position_quota:,.0f} , Indicator Percentage = {indicator_percentage} , Performance Percentage = {performance_percentage} , Indicator Multiplier = {indicator_multiplier} , Performance Multiplier = {performance_multiplier}")

                st.write(f"<span style='font-size:25px'>**Calculation Process**</span>", unsafe_allow_html=True)

                st.write(
                    f"<span style='font-size:16px'>**Indicator Bonus** = Position Quota × Indicator Percentage × [1 + Indicator Multiplier × (Indicator Achievement Rate - 1)] × Indicator Monthly Adjustment Multiplier</span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px; margin-left: 112px;'> = {position_quota:,.0f} * {indicator_percentage} * [1 + {indicator_multiplier} * ({indicator_ach_rate} - 1)] * {m1} = **{indicator_bonus:,.0f}**</span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px'>**Performance Bonus (Unadjusted)** = Position Quota × Performance Percentage × [1 + Performance Multiplier × (Performance Achievement Rate - 1)] × Performance Monthly Adjustment Multiplier</span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px; margin-left: 231px;'> = {position_quota:,.0f} * {performance_percentage} * [1 + {performance_multiplier} * ({perform_ach_rate} - 1)] * {m2} = **{unadjusted_performance_bonus:,.0f}**</span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px; margin-left: 30px;'>***Minimum Performance Bonus** = Position Quota × Performance Percentage × {lowest} % × Performance Monthly Adjustment Multiplier </span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px; margin-left: 244px;'> = {position_quota:,.0f} * {performance_percentage} * {lowest / 100} * {m2} = **{position_quota * performance_percentage * (lowest / 100) * m2:,.0f}**</span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px; margin-left: 30px;'>***Maximum Performance Bonus** = Position Quota × Performance Percentage × {highest} % × Performance Monthly Adjustment Multiplier </span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px; margin-left: 247px;'> = {position_quota:,.0f} * {performance_percentage} * {highest / 100} * {m2} = **{position_quota * performance_percentage * (highest / 100) * m2:,.0f}**</span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px'>**Performance Bonus (Adjusted)** = max(Minimum Performance Bonus, min(Maximum Performance Bonus, Performance Bonus (Unadjusted)))</span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px; margin-left: 212px;'> = max({base_performance_bonus * (lowest/100) * m2:,.0f}, min({base_performance_bonus * (highest/100) * m2:,.0f}, {unadjusted_performance_bonus:,.0f})) = **{adjusted_performance_bonus:,.0f}**</span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:22px'>***Monthly Bonus*** *= Indicator Bonus + Performance Bonus (Adjusted) = {indicator_bonus:,.0f} + {adjusted_performance_bonus:,.0f} =* ***{total_bonus:,.0f}***</span>",
                    unsafe_allow_html=True)
    # with c3:
    #     st.empty()
else:
    if user_input:  # 如果有輸入但不在字典中，顯示錯誤訊息
        c1, c2, c3 = st.columns((1, 0.5, 1))
        with c2:
            st.error("Invalid verification code, please re-enter!")  # 如果沒有輸入或驗證碼無效，不顯示試算器介面


# import pandas as pd
# import streamlit as st
# from datetime import datetime
# from decimal import Decimal
# #
# # 為了之後要自由配置版面的顯示大小，預設用到全部版面
# st.set_page_config(layout="wide")
#
# # 創建海外(在台)的年、月調整乘數對照表  1、2月過年
# adj_df_ost = pd.DataFrame({
#     'Year': [2024] * 12 + [2025] * 12,
#     'Month': list(range(1, 13)) * 2,
#     'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
#     'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# })
#
# # 創建新加坡的年、月調整乘數對照表  1、2月過年
# adj_df_sig = pd.DataFrame({
#     'Year': [2024] * 12 + [2025] * 12,
#     'Month': list(range(1, 13)) * 2,
#     'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
#     'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# })
#
# # 創建馬來西亞的年、月調整乘數對照表  1、2月過年
# adj_df_mal = pd.DataFrame({
#     'Year': [2024] * 12 + [2025] * 12,
#     'Month': list(range(1, 13)) * 2,
#     'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
#     'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# })
#
# # 創建菲律賓的年、月調整乘數對照表  12、1月過年
# adj_df_phi = pd.DataFrame({
#     'Year': [2024] * 12 + [2025] * 12,
#     'Month': list(range(1, 13)) * 2,
#     'm1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
#     'm2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
# })
#
# # 創建印度的年、月調整乘數對照表  10、11月過年
# adj_df_india = pd.DataFrame({
#     'Year': [2024] * 12 + [2025] * 12,
#     'Month': list(range(1, 13)) * 2,
#     'm1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
#     'm2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
# })
#
# # 創建印尼的年、月調整乘數對照表  3、4月過年
# adj_df_indo = pd.DataFrame({
#     'Year': [2024] * 12 + [2025] * 12,
#     'Month': list(range(1, 13)) * 2,
#     'm1': [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
#     'm2': [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# })
#
# # 創建越南的年、月調整乘數對照表  1、2月過年
# adj_df_viet = pd.DataFrame({
#     'Year': [2024] * 12 + [2025] * 12,
#     'Month': list(range(1, 13)) * 2,
#     'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
#     'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# })
#
# # 創建泰國的年、月調整乘數對照表 4、5月過年
# adj_df_thai = pd.DataFrame({
#     'Year': [2024] * 12 + [2025] * 12,
#     'Month': list(range(1, 13)) * 2,
#     'm1': [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
#     'm2': [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
# })
#
# # 將不同區域的DataFrame存儲在字典adj_dfs中
# adj_dfs = {
#     'Overseas (in Taiwan)': adj_df_ost,
#     'Singapore': adj_df_sig,
#     'Malaysia': adj_df_mal,
#     'Philippines': adj_df_phi,
#     'India': adj_df_india,
#     'Indonesia': adj_df_indo,
#     'Vietnam': adj_df_viet,
#     'Thailand': adj_df_thai
# }
#
# # 創建職位的獎金參數對照表
# positions_df = pd.DataFrame({
#     'Region': ['Overseas (in Taiwan)', 'Overseas (in Taiwan)', 'Overseas (in Taiwan)', 'Overseas (in Taiwan)', 'Singapore', 'Singapore', 'Malaysia', 'Philippines', 'Philippines', 'Philippines', 'Philippines',
#             'Indonesia', 'Indonesia', 'Indonesia', 'Indonesia', 'India', 'India', 'India', 'India', 'Vietnam', 'Vietnam', 'Vietnam', 'Vietnam', 'Thailand', 'Thailand', 'Thailand', 'Thailand'],
#     'Position': ['Telemarketing Specialist', 'Product Consultant', 'Senior Consultant', 'Senior Consultant', 'Sales', 'Regional Sales', 'Regional Sales', 'Telemarketing Specialist', 'Product Consultant', 'Sales', 'Regional Sales',
#             'Telemarketing Specialist', 'Product Consultant', 'Sales', 'Regional Sales', 'Telemarketing Specialist', 'Product Consultant', 'Sales', 'Regional Sales', 'Telemarketing Specialist', 'Product Consultant', 'Sales', 'Regional Sales',
#             'Telemarketing Specialist', 'Product Consultant', 'Sales', 'Regional Sales'],
#     'Position Quota': [16000, 18000, 20000, 22000, 1800, 1800, 2500, 25000, 32000, 39000, 50000,
#               3300000, 4100000, 4300000, 5200000, 27000, 35000, 38000, 40000, 7500000, 10000000,
#               12000000, 15000000, 18000, 22000, 24000, 31000],
#     'Indicator Percentage': [1, 0.7, 0.7, 0.7, 0.3, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3],
#     'Performance Percentage': [0, 0.3, 0.3, 0.3, 0.7, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7],
#     'Indicator Multiplier': [3, 3, 3, 3, 1, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1],
#     'Performance Multiplier': [0, 1, 1, 1, 3, 3, 3, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
# })
#
# # 獲取當前年和月
# current_year, current_month = datetime.now().year, datetime.now().month
#
#
# # 定義提取特定區域m1、m2的新函式
# @st.cache_data
# def get_m_values(region, year, month):
#     # adj_df = adj_df[region]
#     m1_m2_data = adj_dfs[region][(adj_dfs[region]['Year'] == year) & (adj_dfs[region]['Month'] == month)]
#     return m1_m2_data.iloc[0][['m1', 'm2']]  # 返回series 但分別對元素賦值後會是int
#
#
# # 定義獎金參數提取函式
# @st.cache_data
# def get_bonus_values(region, position):
#     bonus_data = positions_df[(positions_df['Region'] == region) & (positions_df['Position'] == position)]
#     return bonus_data.iloc[0][['Position Quota', 'Indicator Percentage', 'Performance Percentage', 'Indicator Multiplier', 'Performance Multiplier']]
#
#
# # 定義海外獎金計算函式(最低50%，最高%)
# lowest = 50
# highest = 200
#
#
# def calculate_total_bonus(position_quota, indicator_percentage, performance_percentage, indicator_multiplier, performance_multiplier,
#                           indicator_ach_rate, performance_ach_rate, m1, m2):
#     base_performance_bonus = position_quota * performance_percentage * m2  # 原本的成果獎金 要月份調整
#     indicator_bonus = position_quota * indicator_percentage * (1 + indicator_multiplier * (indicator_ach_rate - 1)) * m1
#     unadjusted_performance_bonus = position_quota * performance_percentage * (1 + performance_multiplier * (performance_ach_rate - 1)) * m2
#     # 對perform_bonus進行上下限限制
#     adjusted_performance_bonus = max(base_performance_bonus * (lowest/100), min(unadjusted_performance_bonus, base_performance_bonus * (highest/100)))
#     total_bonus = indicator_bonus + adjusted_performance_bonus
#     return base_performance_bonus, indicator_bonus, unadjusted_performance_bonus, adjusted_performance_bonus, total_bonus
#
# # 創建區域與驗證碼的對應字典
# region_codes = {
#     '0': 'Overseas (in Taiwan)',
#     '1': 'Singapore',
#     '2': 'Malaysia',
#     '3': 'Philippines',
#     '4': 'Indonesia',
#     '5': 'India',
#     '6': 'Vietnam',
#     '7': 'Thailand'
#     # 可以繼續添加其他區域和驗證碼
# }
#
#
# # 使用者輸入驗證碼 不要讓輸入框那麼長
# c1, c2, c3 = st.columns((1, 0.5, 1))
# with c2:
#     # 使用 st.empty() 創建一个占位符
#     input_placeholder = st.empty()
#     # 在占位符中顯示文本输入框
#     user_input = input_placeholder.text_input('Please enter your region verification code to access the calculator:', '')
#
# # 檢查驗證碼並設定區域
# if user_input in region_codes:
#     region = region_codes[user_input]
#     # 當用户輸入文字後，清空了佔位符，從而隐藏文本输入框
#     input_placeholder.empty()
#
#     # 以下是該區域的試算器相關代碼
#     # 需要根據區域調整的參數或功能，你可以在這裡加入
#     # 可以使用區域變量 `region` 來加載和顯示特定區域的數據
#     # 整個網頁置中，但能自由設定比例布局
#     c1, c2, c3 = st.columns((1, 1.5, 1))  # tw、cn 2.5
#     with c2:
#         # 設定 Streamlit 的網頁標題
#         st.write("<h1 style='font-size: 44px;'>Simple Bonus Calculator<span style='font-size: 30px;'>(For Reference)</span></h1>", unsafe_allow_html=True)
#         # 附註:*6月啟用
#         st.write(f"<span style='font-size:22px'>**:red-background[*Active in June]**</span>", unsafe_allow_html=True)
#         # 設定 Streamlit 的網頁副標題 說明計算器適用限制
#         st.write('*Overseas Business Department*')
#
#         # 使用四列布局(年分、月份、區域、職位選擇欄)
#         # 因前面adj_dfs是dict 要用list(adj_dfs.keys())[0]保證取出第一個鍵(區域) list(adj_dfs.keys())返回所有的key包成list
#         # list(adj_dfs.keys())[0] 預設取adj_dfs第一個國家且年月資料完整
#         col1, col2, col3, col4 = st.columns(4)
#         with col1:
#             year = st.selectbox('Select Year', adj_dfs[list(adj_dfs.keys())[0]]['Year'].unique(), index=adj_dfs[list(adj_dfs.keys())[0]]['Year'].tolist().index(current_year))  # 保證預設是目前年份
#         with col2:
#             month = st.selectbox('Select Month', adj_dfs[list(adj_dfs.keys())[0]]['Month'].unique(), index=current_month - 1)  # 保證預設是目前月份
#         with col3:
#             region = st.selectbox("Select Region", [region])
#             # 獲取 m1 和 m2 值
#             m1, m2 = get_m_values(region, year, month)
#         with col4:
#             # 6月規則只剩產品顧問、無資深、高級顧問
#             # 各國有的職位不同，要篩選出特定區域的職位讓使用者選，'同時'排除資深、高級、區域業務
#             filtered_positions = positions_df[(positions_df['Region'] == region) &
#                                               (positions_df['Position'] != 'Senior Consultant') &
#                                               (positions_df['Position'] != 'Senior Consultant') &
#                                               (positions_df['Position'] != 'Regional Sales')]['Position'].unique()
#
#             # 避免某地區沒有職位，取不到值
#             if len(filtered_positions) == 0:
#                 # 要給以下設定否則會取不到值報錯
#                 position = ''
#                 position_quota, indicator_percentage, performance_percentage, indicator_multiplier, performance_multiplier = 0, 0, 0, 0, 0
#                 st.warning("No positions available in the selected region. Cannot calculate the bonus.")
#             else:
#                 position = st.selectbox('Select Position', filtered_positions)
#                 # 獲取特定職位的各獎金參數
#                 position_quota, indicator_percentage, performance_percentage, indicator_multiplier, performance_multiplier = get_bonus_values(region, position)
#
#         # 當沒有職位可以選時(選到空值時)，以下都不執行，反之都執行
#         if position != '':
#             # 使用兩列布局(指標、累積成果獎金計算過程在右邊)
#             col1, col2 = st.columns((1, 2.2))
#             # 第一列放使用者輸入(左邊)
#             with col1:
#                 st.write('<br>', unsafe_allow_html=True)  # 讓selectbox跟input達成率之間不要太擠
#                 # 為了讓使用者可以輸入任意位數的小數，indicator_ach_rate、perform_ach_rate 改用text_input才能存所有位數，
#                 # number_input只能輸入小數點後兩位(調format也只能強制輸入固定位數)
#                 # 並用Decimal保留精度
#                 # 缺點是text_input沒有微調按鍵
#                 indicator_ach_rate = st.text_input('Indicator Achievement Rate (%)', value='100', help='Please enter the percentage value, e.g., 131.0781 represents 131.0781%')
#                 performance_ach_rate = st.text_input('Performance Achievement Rate (%)', value='100', help='Please enter the percentage value, e.g., 131.0781 represents 131.0781%')
#
#                 # 將百分比值轉換為小數 .strip('%')確保就算使用者多輸入%符號也沒差
#                 # Decimal()傳入str型小數可保留精確的位數(預設28位)，但做運算後類型還會是 decimal.Decimal，故最外面要包float()，後續才能運算
#                 # 後面相關的達成率都不用調，因為基本上都會四捨五入
#                 indicator_ach_rate = float(Decimal(indicator_ach_rate.strip('%')) / 100)
#                 performance_ach_rate = float(Decimal(performance_ach_rate.strip('%')) / 100)
#
#             # 第二列放計算結果(右邊)
#             with col2:
#                 # 獲取當月獎金與其組成
#                 base_performance_bonus, indicator_bonus, unadjusted_performance_bonus, adjusted_performance_bonus, total_bonus = calculate_total_bonus(
#                     position_quota, indicator_percentage, performance_percentage, indicator_multiplier, performance_multiplier, indicator_ach_rate, performance_ach_rate, m1, m2)
#
#                 st.markdown(
#                     """
#                     <style>
#                     .stMarkdown p {
#                         margin-top: 50px;
#                         margin-bottom: 50px;
#                     }
#                     </style>
#                     """,
#                     unsafe_allow_html=True,
#                 )
#                 st.write(f"<span style='font-size:21px'>**Indicator Bonus**:</span>", unsafe_allow_html=True)
#                 st.write(f"<span style='font-size:18px'>{position_quota:,.0f} * {indicator_percentage} * [1 + {indicator_multiplier} * ({indicator_ach_rate} - 1)] * {m1} = **{indicator_bonus:,.0f}**</span>", unsafe_allow_html=True)
#
#                 st.write(f"<span style='font-size:21px'>**Performance Bonus (Adjusted)**:</span>", unsafe_allow_html=True)
#                 if 1 + performance_multiplier * (performance_ach_rate - 1) > highest / 100:
#                     st.write(f"<span style='font-size:18px'>{position_quota:,.0f} * {performance_percentage} *  {highest / 100} * {m2} = **{position_quota * performance_percentage * (highest / 100) * m2:,.0f}**</span>", unsafe_allow_html=True)
#                 elif 1 + performance_multiplier * (performance_ach_rate - 1) < lowest / 100:
#                     st.write(f"<span style='font-size:18px'>{position_quota:,.0f} * {performance_percentage} *  {lowest / 100} * {m2} = **{position_quota * performance_percentage * (lowest / 100) * m2:,.0f}**</span>", unsafe_allow_html=True)
#                 else:
#                     st.write(f"<span style='font-size:18px'>{position_quota:,.0f} * {performance_percentage} * [1 + {performance_multiplier} * ({performance_ach_rate} - 1)] * {m2} = **{adjusted_performance_bonus:,.0f}**</span>", unsafe_allow_html=True)
#
#                 st.markdown(
#                     """
#                     <style>
#                     .stMarkdown p {
#                         margin-top: 5.7px;
#                         margin-bottom: 5.7px;
#                     }
#                     </style>
#                     """,
#                     unsafe_allow_html=True,
#                 )
#
#             st.write(f"""
#                 <div style='text-align:center; font-size: 40px;'>
#                     <strong>Bonus for the month: {total_bonus:,.0f}</strong>
#                 </div>
#                  """, unsafe_allow_html=True)  # 調整置中、大小、粗體
#             # 附註計算限制
#             st.write(f"""
#                 <div style='text-align: center; font-size: 15px;'>
#                        *Bonus amount does not include attendance, collection rewards and penalties, and other calculations
#                 </div>
#                 """, unsafe_allow_html=True)
#
#         # 使用expander隱藏詳細過程
#             with st.expander("Click to view detailed process", expanded=False):
#                 st.write("")
#                 st.write(f'You selected: {year} Year {month} Month')
#                 st.write(f"<span style='font-size:25px'>**Monthly Adjustment Multipliers**</span>", unsafe_allow_html=True)
#                 st.write(f"Indicator Monthly Adjustment Multiplier = {m1} , Performance Monthly Adjustment Multiplier = {m2}")
#                 st.write(f"<span style='font-size:25px'>**Bonus Parameter Values**</span>", unsafe_allow_html=True)
#                 st.write(f"Position Quota = {position_quota:,.0f} , Indicator Percentage = {indicator_percentage} , Performance Percentage = {performance_percentage} , Indicator Multiplier = {indicator_multiplier} , Performance Multiplier = {performance_multiplier}")
#
#                 st.write(f"<span style='font-size:25px'>**Calculation Process**</span>", unsafe_allow_html=True)
#
#                 st.write(f"<span style='font-size:16px'>**Indicator Bonus** = Position Quota × Indicator Percentage × [1 + Indicator Multiplier × (Indicator Achievement Rate - 1)] × Indicator Monthly Adjustment Multiplier</span>", unsafe_allow_html=True)
#                 st.write(f"<span style='font-size:16px; margin-left: 68px;'> = {position_quota:,.0f} * {indicator_percentage} * [1 + {indicator_multiplier} * ({indicator_ach_rate} - 1)] * {m1} = **{indicator_bonus:,.0f}**</span>", unsafe_allow_html=True)
#
#                 st.write(f"<span style='font-size:16px'>**Performance Bonus (Unadjusted)** = Position Quota × Performance Percentage × [1 + Performance Multiplier × (Performance Achievement Rate - 1)] × Performance Monthly Adjustment Multiplier</span>", unsafe_allow_html=True)
#                 st.write(f"<span style='font-size:16px; margin-left: 126px;'> = {position_quota:,.0f} * {performance_percentage} * [1 + {performance_multiplier} * ({performance_ach_rate} - 1)] * {m2} = **{unadjusted_performance_bonus:,.0f}**</span>", unsafe_allow_html=True)
#
#                 st.write(f"<span style='font-size:16px; margin-left: 30px;'>***Minimum Performance Bonus** = Position Quota × Performance Percentage × {lowest} % × Performance Monthly Adjustment Multiplier </span>", unsafe_allow_html=True)
#                 st.write(f"<span style='font-size:16px; margin-left: 136px;'> = {position_quota:,.0f} * {performance_percentage} * {lowest / 100} * {m2} = **{position_quota * performance_percentage * (lowest / 100) * m2:,.0f}**</span>", unsafe_allow_html=True)
#
#                 st.write(f"<span style='font-size:16px; margin-left: 30px;'>***Maximum Performance Bonus** = Position Quota × Performance Percentage × {highest} % × Performance Monthly Adjustment Multiplier </span>", unsafe_allow_html=True)
#                 st.write(f"<span style='font-size:16px; margin-left: 136px;'> = {position_quota:,.0f} * {performance_percentage} * {highest / 100} * {m2} = **{position_quota * performance_percentage * (highest / 100) * m2:,.0f}**</span>", unsafe_allowhtml=True)
#
#                 st.write(f"<span style='font-size:16px'>**Adjusted Performance Bonus** = max(Minimum Performance Bonus, min(Maximum Performance Bonus, Performance Bonus (Unadjusted)))</span>", unsafe_allow_html=True)
#                 st.write(f"<span style='font-size:16px; margin-left: 126px;'> = max({base_performance_bonus * (lowest/100) * m2:,.0f}, min({base_performance_bonus * (highest/100) * m2:,.0f}, {unadjusted_performance_bonus:,.0f})) = **{adjusted_performance_bonus:,.0f}**</span>", unsafe_allow_html=True)
#                 st.write(f"<span style='font-size:22px'>***Bonus for the Month*** *= Indicator Bonus + Adjusted Performance Bonus = {indicator_bonus:,.0f} + {adjusted_performance_bonus:,.0f} =* ***{total_bonus:,.0f}***</span>", unsafe_allow_html=True)
#     # with c3:
#     #     st.empty()
# else:
#     if user_input:  # 如果有輸入但不在字典中，顯示錯誤訊息
#         c1, c2, c3 = st.columns((1, 0.5, 1))
#         with c2:
#             st.error("Invalid verification code, please re-enter!")  # 如果沒有輸入或驗證碼無效，不顯示試算器介面
#
#
# # import pandas as pd
# # import streamlit as st
# # from datetime import datetime
# # from decimal import Decimal
# # #
# # # 為了之後要自由配置版面的顯示大小，預設用到全部版面
# # st.set_page_config(layout="wide")
# #
# # # 創建海外(在台)的年、月調整乘數對照表  1、2月過年
# # adj_df_ost = pd.DataFrame({
# #     'Year': [2024] * 12 + [2025] * 12,
# #     'Month': list(range(1, 13)) * 2,
# #     'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
# #     'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# # })
# #
# # # 創建新加坡的年、月調整乘數對照表  1、2月過年
# # adj_df_sig = pd.DataFrame({
# #     'Year': [2024] * 12 + [2025] * 12,
# #     'Month': list(range(1, 13)) * 2,
# #     'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
# #     'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# # })
# #
# # # 創建馬來西亞的年、月調整乘數對照表  1、2月過年
# # adj_df_mal = pd.DataFrame({
# #     'Year': [2024] * 12 + [2025] * 12,
# #     'Month': list(range(1, 13)) * 2,
# #     'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
# #     'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# # })
# #
# # # 創建菲律賓的年、月調整乘數對照表  12、1月過年
# # adj_df_phi = pd.DataFrame({
# #     'Year': [2024] * 12 + [2025] * 12,
# #     'Month': list(range(1, 13)) * 2,
# #     'm1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
# #     'm2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
# # })
# #
# # # 創建印度的年、月調整乘數對照表  10、11月過年
# # adj_df_india = pd.DataFrame({
# #     'Year': [2024] * 12 + [2025] * 12,
# #     'Month': list(range(1, 13)) * 2,
# #     'm1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
# #     'm2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
# # })
# #
# # # 創建印尼的年、月調整乘數對照表  3、4月過年
# # adj_df_indo = pd.DataFrame({
# #     'Year': [2024] * 12 + [2025] * 12,
# #     'Month': list(range(1, 13)) * 2,
# #     'm1': [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
# #     'm2': [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# # })
# #
# # # 創建越南的年、月調整乘數對照表  1、2月過年
# # adj_df_viet = pd.DataFrame({
# #     'Year': [2024] * 12 + [2025] * 12,
# #     'Month': list(range(1, 13)) * 2,
# #     'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
# #     'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# # })
# #
# # # 創建泰國的年、月調整乘數對照表 4、5月過年
# # adj_df_thai = pd.DataFrame({
# #     'Year': [2024] * 12 + [2025] * 12,
# #     'Month': list(range(1, 13)) * 2,
# #     'm1': [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
# #     'm2': [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
# # })
# #
# # # 將不同區域的DataFrame存儲在字典adj_dfs中
# # adj_dfs = {
# #     'Overseas (in Taiwan)': adj_df_ost,
# #     'Singapore': adj_df_sig,
# #     'Malaysia': adj_df_mal,
# #     'Philippines': adj_df_phi,
# #     'India': adj_df_india,
# #     'Indonesia': adj_df_indo,
# #     'Vietnam': adj_df_viet,
# #     'Thailand': adj_df_thai
# # }
# #
# #
# # # 創建職位的獎金參數對照表
# # positions_df = pd.DataFrame({
# #     'Region': ['Overseas (Taiwan)', 'Overseas (Taiwan)', 'Overseas (Taiwan)', 'Overseas (Taiwan)', 'Singapore', 'Singapore', 'Malaysia', 'Philippines', 'Philippines', 'Philippines', 'Philippines',
# #             'Indonesia', 'Indonesia', 'Indonesia', 'Indonesia', 'India', 'India', 'India', 'India', 'Vietnam', 'Vietnam', 'Vietnam', 'Vietnam', 'Thailand', 'Thailand', 'Thailand', 'Thailand'],
# #     'Position': ['Telemarketer', 'Product Consultant', 'Senior Consultant', 'Expert Consultant', 'Sales', 'Regional Sales', 'Regional Sales', 'Telemarketer', 'Product Consultant', 'Sales', 'Regional Sales',
# #             'Telemarketer', 'Product Consultant', 'Sales', 'Regional Sales', 'Telemarketer', 'Product Consultant', 'Sales', 'Regional Sales', 'Telemarketer', 'Product Consultant', 'Sales', 'Regional Sales',
# #             'Telemarketer', 'Product Consultant', 'Sales', 'Regional Sales'],
# #     'Quota': [16000, 18000, 20000, 22000, 1800, 1800, 2500, 25000, 32000, 39000, 50000,
# #               3300000, 4100000, 4300000, 5200000, 27000, 35000, 38000, 40000, 7500000, 10000000,
# #               12000000, 15000000, 18000, 22000, 24000, 31000],
# #     'Indicator Proportion': [1, 0.7, 0.7, 0.7, 0.3, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3],
# #     'Performance Proportion': [0, 0.3, 0.3, 0.3, 0.7, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7],
# #     'Indicator Multiplier': [3, 3, 3, 3, 1, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1],
# #     'Performance Multiplier': [0, 1, 1, 1, 3, 3, 3, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
# # })
# #
# # # 獲取當前年和月
# # current_year, current_month = datetime.now().year, datetime.now().month
# #
# #
# # # 定義提取特定區域m1、m2的新函式
# # @st.cache_data
# # def get_m_values(region, year, month):
# #     # adj_df = adj_df[region]
# #     m1_m2_data = adj_dfs[region][(adj_dfs[region]['Year'] == year) & (adj_dfs[region]['Month'] == month)]
# #     return m1_m2_data.iloc[0][['m1', 'm2']]  # 返回series 但分別對元素賦值後會是int
# #
# #
# # # 定義獎金參數提取函式
# # @st.cache_data
# # def get_bonus_values(region, position):
# #     bonus_data = positions_df[(positions_df['Region'] == region) & (positions_df['Position'] == position)]
# #     return bonus_data.iloc[0][['Quota', 'Indicator Proportion', 'Performance Proportion', 'Indicator Multiplier', 'Performance Multiplier']]
# #
# #
# # # 定義海外獎金計算函式(最低50%，最高%)
# # lowest = 50
# # highest = 200
# #
# #
# # def calculate_total_bonus(position_quota, indicator_per, perform_per, indicator_multi, perform_multi,
# #                           indicator_ach_rate, perform_ach_rate, m1, m2):
# #     base_perform_bonus = position_quota * perform_per * m2  # 原本的成果獎金 要月份調整
# #     indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1
# #     o_perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2
# #     # 對perform_bonus進行上下限限制
# #     n_perform_bonus = max(base_perform_bonus * (lowest/100), min(o_perform_bonus, base_perform_bonus * (highest/100)))
# #     total_bonus = indicator_bonus + n_perform_bonus
# #     return base_perform_bonus, indicator_bonus, o_perform_bonus, n_perform_bonus, total_bonus
# #
# # # 創建區域與驗證碼的對應字典
# # region_codes = {
# #     '0': 'Overseas (Taiwan)',
# #     '1': 'Singapore',
# #     '2': 'Malaysia',
# #     '3': 'Philippines',
# #     '4': 'Indonesia',
# #     '5': 'India',
# #     '6': 'Vietnam',
# #     '7': 'Thailand'
# #     # 可以繼續添加其他區域和驗證碼
# # }
# #
# # # 使用者輸入驗證碼 不要讓輸入框那麼長
# # c1, c2, c3 = st.columns((1, 0.5, 1))
# # with c2:
# #     # 使用 st.empty() 創建一个占位符
# #     input_placeholder = st.empty()
# #     # 在占位符中顯示文本输入框
# #     user_input = input_placeholder.text_input('Please enter your region verification code to access the calculator:', '')
# #
# # # 檢查驗證碼並設定區域
# # if user_input in region_codes:
# #     region = region_codes[user_input]
# #     # 當用户輸入文字後，清空了佔位符，從而隐藏文本输入框
# #     input_placeholder.empty()
# #
# #     # 以下是該區域的試算器相關代碼
# #     # 需要根據區域調整的參數或功能，你可以在這裡加入
# #     # 可以使用區域變量 `region` 來加載和顯示特定區域的數據
# #     # 整個網頁置中，但能自由設定比例布局
# #     c1, c2, c3 = st.columns((1, 1.5, 1))  # tw、cn 2.5
# #     with c2:
# #         # 設定 Streamlit 的網頁標題
# #         st.write("<h1 style='font-size: 44px;'>Simple Bonus Calculator<span style='font-size: 30px;'>(For Reference)</span></h1>", unsafe_allow_html=True)
# #         # 附註:*6月啟用
# #         st.write(f"<span style='font-size:22px'>**:red-background[*Effective from June]**</span>", unsafe_allow_html=True)
# #         # 設定 Streamlit 的網頁副標題 說明計算器適用限制
# #         st.write('*Overseas Division*')
# #
# #         # 使用四列布局(年分、月份、區域、職位選擇欄)
# #         # 因前面adj_dfs是dict 要用list(adj_dfs.keys())[0]保證取出第一個鍵(區域) list(adj_dfs.keys())返回所有的key包成list
# #         # list(adj_dfs.keys())[0] 預設取adj_dfs第一個國家且年月資料完整
# #         col1, col2, col3, col4 = st.columns(4)
# #         with col1:
# #             year = st.selectbox('Select Year', adj_dfs[list(adj_dfs.keys())[0]]['Year'].unique(), index=adj_dfs[list(adj_dfs.keys())[0]]['Year'].tolist().index(current_year))  # 保證預設是目前年份
# #         with col2:
# #             month = st.selectbox('Select Month', adj_dfs[list(adj_dfs.keys())[0]]['Month'].unique(), index=current_month - 1)  # 保證預設是目前月份
# #         with col3:
# #             region = st.selectbox("Select Region", [region])
# #             # 獲取 m1 和 m2 值
# #             m1, m2 = get_m_values(region, year, month)
# #         with col4:
# #             # 6月規則只剩產品顧問、無資深、高級顧問
# #             # 各國有的職位不同，要篩選出特定區域的職位讓使用者選，'同時'排除資深、高級、區域業務
# #             filtered_positions = positions_df[(positions_df['Region'] == region) &
# #                                               (positions_df['Position'] != 'Expert Consultant') &
# #                                               (positions_df['Position'] != 'Senior Consultant') &
# #                                               (positions_df['Position'] != 'Regional Sales')]['Position'].unique()
# #
# #             # 避免某地區沒有職位，取不到值
# #             if len(filtered_positions) == 0:
# #                 # 要給以下設定否則會取不到值報錯
# #                 position = ''
# #                 position_quota, indicator_per, perform_per, indicator_multi, perform_multi = 0, 0, 0, 0, 0
# #                 st.warning("No available positions for the selected region, cannot calculate bonus.")
# #             else:
# #                 position = st.selectbox('Select Position', filtered_positions)
# #                 # 獲取特定職位的各獎金參數
# #                 position_quota, indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values(region, position)
# #
# #         # 當沒有職位可以選時(選到空值時)，以下都不執行，反之都執行
# #         if position != '':
# #             # 使用兩列布局(指標、累積成果獎金計算過程在右邊)
# #             col1, col2 = st.columns((1, 2))
# #             # 第一列放使用者輸入(左邊)
# #             with col1:
# #                 st.write('<br>', unsafe_allow_html=True)  # 讓selectbox跟input達成率之間不要太擠
# #                 # #為了讓使用者可以輸入任意位數的小數，indicator_ach_rate、perform_ach_rate 改用text_input才能存所有位數，
# #                 # number_input只能輸入小數點後兩位(調format也只能強制輸入固定位數)
# #                 # 並用Decimal保留精度
# #                 # 缺點是text_input沒有微調按鍵
# #                 indicator_ach_rate = st.text_input('Indicator Achievement Rate (%)', value='100', help='Please enter percentage value, e.g., 131.0781 means 131.0781%')
# #                 perform_ach_rate = st.text_input('Performance Achievement Rate (%)', value='100', help='Please enter percentage value, e.g., 131.0781 means 131.0781%')
# #
# #                 # 將百分比值轉換為小數 .strip('%')確保就算使用者多輸入%符號也沒差
# #                 # Decimal()傳入str型小數可保留精確的位數(預設28位)，但做運算後類型還會是 decimal.Decimal，故最外面要包float()，後續才能運算
# #                 # 後面相關的達成率都不用調，因為基本上都會四捨五入
# #                 indicator_ach_rate = float(Decimal(indicator_ach_rate.strip('%')) / 100)
# #                 perform_ach_rate = float(Decimal(perform_ach_rate.strip('%')) / 100)
# #
# #             # 第二列放計算結果(右邊)
# #             with col2:
# #                 # 獲取當月獎金與其組成
# #                 base_perform_bonus, indicator_bonus, o_perform_bonus, n_perform_bonus, total_bonus = calculate_total_bonus(
# #                                                                                     position_quota, indicator_per,
# #                                                                                     perform_per, indicator_multi,
# #                                                                                     perform_multi, indicator_ach_rate,
# #                                                                                     perform_ach_rate, m1, m2)
# #                 st.markdown(
# #                     """
# #                     <style>
# #                     .stMarkdown p {
# #                         margin-top: 50px;
# #                         margin-bottom: 50px;
# #                     }
# #                     </style>
# #                     """,
# #                     unsafe_allow_html=True,
# #                 )
# #                 st.write(f"<span style='font-size:21px'>**Indicator Bonus**:</span>",
# #                          unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:18px'>{position_quota:,.0f} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = **{indicator_bonus:,.0f}**</span>",
# #                     unsafe_allow_html=True)
# #
# #                 st.write(
# #                     f"<span style='font-size:21px'>**Performance Bonus**</span>",
# #                     unsafe_allow_html=True)
# #                 if 1 + perform_multi * (perform_ach_rate - 1) > highest / 100:
# #                     st.write(
# #                         f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} *  {highest / 100} * {m2} = **{position_quota * perform_per * (highest / 100) * m2:,.0f}**</span>",
# #                         unsafe_allow_html=True)
# #                 elif 1 + perform_multi * (perform_ach_rate - 1) < lowest / 100:
# #                     st.write(
# #                         f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} *  {lowest / 100} * {m2} = **{position_quota * perform_per * (lowest / 100) * m2:,.0f}**</span>",
# #                         unsafe_allow_html=True)
# #                 else:
# #                     st.write(
# #                         f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = **{n_perform_bonus:,.0f}**</span>",
# #                         unsafe_allow_html=True)
# #                 st.markdown(
# #                     """
# #                     <style>
# #                     .stMarkdown p {
# #                         margin-top: 5.7px;
# #                         margin-bottom: 5.7px;
# #                     }
# #                     </style>
# #                     """,
# #                     unsafe_allow_html=True,
# #                 )
# #
# #             st.write(f"""
# #                 <div style='text-align:center; font-size: 40px;'>
# #                     <strong>Monthly Bonus: {total_bonus:,.0f}</strong>
# #                 </div>
# #                  """, unsafe_allow_html=True)  # 調整置中、大小、粗體
# #             # 附註計算限制
# #             st.write(f"""
# #                 <div style='text-align: center; font-size: 15px;'>
# #                        *Bonus amount does not include attendance, collection rewards/penalties, etc.
# #                 </div>
# #                 """, unsafe_allow_html=True)
# #
# #         # 使用expander隱藏詳細過程
# #             with st.expander("Click to view detailed process", expanded=False):
# #                 st.write("")
# #                 st.write(f'You selected: {year} Year {month} Month')
# #                 st.write(f"<span style='font-size:25px'>**Monthly Adjustment Multipliers**</span>", unsafe_allow_html=True)
# #                 st.write(f"Indicator Adjustment Multiplier = {m1} , Performance Adjustment Multiplier = {m2}")
# #                 st.write(f"<span style='font-size:25px'>**Bonus Parameter Values**</span>", unsafe_allow_html=True)
# #                 st.write(
# #                     f"Quota = {position_quota:,.0f} , Indicator Proportion = {indicator_per} , Performance Proportion = {perform_per} , Indicator Multiplier = {indicator_multi} , Performance Multiplier = {perform_multi}")
# #
# #                 st.write(f"<span style='font-size:25px'>**Calculation Process**</span>", unsafe_allow_html=True)
# #
# #                 st.write(
# #                     f"<span style='font-size:16px'>**Indicator Bonus** = Quota × Indicator Proportion × [1 + Indicator Multiplier × (Indicator Achievement Rate - 1)] × Indicator Adjustment Multiplier</span>",
# #                     unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:16px; margin-left: 68px;'> = {position_quota:,.0f} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = **{indicator_bonus:,.0f}**</span>",
# #                     unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:16px'>**Performance Bonus (Unadjusted)** = Quota × Performance Proportion × [1 + Performance Multiplier × (Performance Achievement Rate - 1)] × Performance Adjustment Multiplier</span>",
# #                     unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:16px; margin-left: 126px;'> = {position_quota:,.0f} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = **{o_perform_bonus:,.0f}**</span>",
# #                     unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:16px; margin-left: 30px;'>***Minimum Performance Bonus** = Quota × Performance Proportion × {lowest} % × Performance Adjustment Multiplier </span>",
# #                     unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:16px; margin-left: 136px;'> = {position_quota:,.0f} * {perform_per} * {lowest / 100} * {m2} = **{position_quota * perform_per * (lowest / 100) * m2:,.0f}**</span>",
# #                     unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:16px; margin-left: 30px;'>***Maximum Performance Bonus** = Quota × Performance Proportion × {highest} % × Performance Adjustment Multiplier </span>",
# #                     unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:16px; margin-left: 136px;'> = {position_quota:,.0f} * {perform_per} * {highest / 100} * {m2} = **{position_quota * perform_per * (highest / 100) * m2:,.0f}**</span>",
# #                     unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:16px'>**Adjusted Performance Bonus** = max(Minimum Performance Bonus, min(Maximum Performance Bonus, Unadjusted Performance Bonus))</span>",
# #                     unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:16px; margin-left: 126px;'> = max({base_perform_bonus * (lowest/100) * m2:,.0f}, min({base_perform_bonus * (highest/100) * m2:,.0f}, {o_perform_bonus:,.0f})) = **{n_perform_bonus:,.0f}**</span>",
# #                     unsafe_allow_html=True)
# #                 st.write(
# #                     f"<span style='font-size:22px'>***Monthly Bonus*** *= Indicator Bonus + Adjusted Performance Bonus = {indicator_bonus:,.0f} + {n_perform_bonus:,.0f} =* ***{total_bonus:,.0f}***</span>",
# #                     unsafe_allow_html=True)
# # else:
# #     if user_input:  # 如果有輸入但不在字典中，顯示錯誤訊息
# #         c1, c2, c3 = st.columns((1, 0.5, 1))
# #         with c2:
# #             st.error("Invalid verification code, please re-enter!")  # 如果沒有輸入或驗證碼無效，不顯示試算器介面

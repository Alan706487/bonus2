import pandas as pd
import streamlit as st
from datetime import datetime
from decimal import Decimal
import os

# 為了之後要自由配置版面的顯示大小，預設用到全部版面
st.set_page_config(layout="wide")

# 創建海外(在台)的年、月調整乘數對照表  1、2月過年
adj_df_ost = pd.DataFrame({
    'Year': [2024] * 12 + [2025] * 12,
    'Month': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年
    'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建大陸(在台)的年、月調整乘數對照表  1、2月過年
adj_df_osc = pd.DataFrame({
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
    'Overseas (China)': adj_df_osc,  # 大陸在台
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
    'Indicator Percentage': [1, 0.5, 0.7, 0.7, 0.3, 0.3, 0.3, 1, 0.5, 0.3, 0.3, 1, 0.5, 0.3, 0.3, 1, 0.5, 0.3, 0.3, 1, 0.5, 0.3, 0.3, 1, 0.5, 0.3, 0.3],
    'Performance Percentage': [0, 0, 0.3, 0.3, 0.7, 0.4, 0.4, 0, 0, 0.7, 0.4, 0, 0, 0.7, 0.4, 0, 0, 0.7, 0.4, 0, 0, 0.7, 0.4, 0, 0, 0.7, 0.4],
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
    'tw': 'Overseas (Taiwan)',
    'cn': 'Overseas (China)',  # 大陸在台
    'sg': 'Singapore',
    'my': 'Malaysia',
    'ph': 'Philippines',
    'id': 'Indonesia',
    'in': 'India',
    'vn': 'Vietnam',
    'th': 'Thailand'
    # 可以繼續添加其他區域和驗證碼
}

# 使用者輸入驗證碼 不要讓輸入框那麼長
c1, c2, c3 = st.columns((1, 0.5, 1))
with c2:
    # 使用 st.empty() 創建一个占位符
    input_placeholder = st.empty()
    # 在占位符中顯示文本输入框
    user_input = input_placeholder.text_input('Please enter your region verification code to access the calculator:',
                                              '').lower()

# 檢查驗證碼並設定區域
if user_input in region_codes:
    region = region_codes[user_input]
    # 當用户輸入文字後，清空了佔位符，從而隐藏文本输入框
    input_placeholder.empty()

    # 以下是該區域的試算器相關代碼
    # 需要根據區域調整的參數或功能，你可以在這裡加入
    # 可以使用區域變量 `region` 來加載和顯示特定區域的數據
    # 整個網頁置中，但能自由設定比例布局
    #--------
    if region == 'Overseas (China)':
        # st.write(f'{region}')
        # 創建年、月調整乘數對照表
        adj_df = pd.DataFrame({
            '年': [2024] * 12 + [2025] * 12,
            '月份': list(range(1, 13)) * 2,
            'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'm2': [0, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3]
        })

        # # 創建職位的獎金參數對照表 大陸無區域、職位份額
        # positions_df = pd.DataFrame({
        #     '职位': ['电访专员', '产品顾问', '资深顾问', '高级顾问', '业务', '区域业务'],
        #     '指标占比': [1, 0.5, 0.7, 0.7, 0.3, 0.3],
        #     '成果占比': [0, 0, 0.3, 0.3, 0.7, 0.4],
        #     '指标倍数': [3, 3, 3, 3, 1, 1],
        #     '成果倍数': [0, 3, 3, 3, 3, 3]
        # })

        # # 大陸在台 創建職位的獎金參數對照表 大陸在台無區域
        # positions_df = pd.DataFrame({
        #     '职位': ['电访专员', '产品顾问', '资深顾问', '高级顾问', '业务', '区域业务'],
        #     '职位份额':[16000, 20000, 20000, 20000, 0, 0],  # 新增
        #     '指标占比': [1, 0.5, 0.7, 0.7, 0.3, 0.3],
        #     '成果占比': [0, 0, 0.3, 0.3, 0.7, 0.4],
        #     '指标倍数': [3, 3, 3, 3, 1, 1],
        #     '成果倍数': [0, 3, 3, 3, 3, 3]
        # })
        # 大陸在台 創建職位的獎金參數對照表 大陸在台無區域
        positions_df = pd.DataFrame({
            '職位': ['電訪專員', '產品顧問', '業務', '區域業務'],
            '職位份額': [14000, 20000, 28000, 24000],  # 新增
            '指標占比': [1, 0.5, 0.3, 0.3],
            '成果占比': [0, 0, 0.7, 0.4],
            '指標倍数': [3, 3, 1, 1],
            '成果倍数': [0, 3, 3, 3]
        })

        # 獲取當前年和月
        current_year, current_month = datetime.now().year, datetime.now().month


        # 定義提取m1、m2的函式
        @st.cache_data
        def get_m_values(year, month):
            m1_m2_data = adj_df[(adj_df['年'] == year) & (adj_df['月份'] == month)]
            # return m1_m2_data['m1'].values[0], m1_m2_data['m2'].values[0]
            return m1_m2_data.iloc[0][['m1', 'm2']]  # 返回series 但分別對元素賦值後會是int


        # 定義獎金參數提取函式  大陸不用提區域、職位份額 用輸入的職位提取其他獎金參數
        @st.cache_data
        def get_bonus_values(position):
            bonus_data = positions_df[positions_df['職位'] == position]
            # return bonus_data['指標占比'].values[0], bonus_data['成果占比'].values[0], bonus_data['指標倍數'].values[0], bonus_data['成果倍數'].values[0]
            # return bonus_data.iloc[0][['指标占比', '成果占比', '指标倍数', '成果倍数']]
            return bonus_data.iloc[0][['職位份額', '指標占比', '成果占比', '指標倍数', '成果倍数']]


        # 定義獎金計算函式  大陸position_quota是自輸，涵式不用放
        # def calculate_total_bonus(indicator_per, perform_per, indicator_multi, perform_multi,
        #                           indicator_ach_rate, perform_ach_rate, accumulated_bonus, m1, m2):
        #     indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1
        #     perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2
        #     total_bonus = indicator_bonus + max(0, perform_bonus - accumulated_bonus)
        #     return total_bonus, indicator_bonus, perform_bonus


        def calculate_total_bonus(position_quota, indicator_per, perform_per, indicator_multi, perform_multi,
                                  indicator_ach_rate, perform_ach_rate, accumulated_bonus, m1, m2):
            indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1
            perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2
            total_bonus = indicator_bonus + max(0, perform_bonus - accumulated_bonus)
            return total_bonus, indicator_bonus, perform_bonus  # 海大陸在台 取得職位份額


        # 整個網頁置中，但能自由設定比例布局
        c1, c2, c3 = st.columns((1, 2, 1))
        # with c1:
        #     st.empty()
        with c2:
            # 設定 Streamlit 的網頁標題
            st.write("<h1 style='font-size: 44px;'>獎金簡易試算器<span style='font-size: 30px;'>(參考用)</span></h1>",
                     unsafe_allow_html=True)
            # 附註:*6月啟用
            st.write(f"<span style='font-size:22px'>**:red-background[*6月啟用]**</span>", unsafe_allow_html=True)

            # 設定 Streamlit 的網頁副標題 說明計算器適用限制
            # st.write('*大陆事业部、业管部电访组( 不考虑新人成果奖金保障阶段 )*')
            st.write('*大陸事業部*')  # 不用註明大陸在台


            # # 使用四列布局(年分、月份、區域、職位選擇欄)
            # col1, col2, col3, col4 = st.columns(4)
            # 大陸在台使用三列布局(年分、月份、職位選擇欄)
            # col1, col2, col3 = st.columns(3)
            # with col1:
            #     year = st.selectbox('选择年份', adj_df['年'].unique(),
            #                         index=adj_df['年'].tolist().index(current_year))  # 保证默认是当前年份
            # with col2:
            #     month = st.selectbox('选择月份', adj_df['月份'].unique(), index=current_month - 1)  # 保证默认是当前月份
            # with col3:
            #     # position = st.selectbox('选择职位', positions_df[positions_df['职位'] != '区域业务']['职位'].unique())  # 大陸現在沒有區域業務，先不顯示
            #     # 大陸新規則也是沒有資深、高級顧問了、也沒有區域業務，先不顯示
            #     position = st.selectbox('选择职位',
            #                             positions_df[(positions_df['职位'] != '区域业务') & (
            #                                         positions_df['职位'] != '资深顾问') & (
            #                                                      positions_df['职位'] != '高级顾问')][
            #                                 '职位'].unique())  # 大陸現在沒有區域業務，先不顯示
            # with col4:
            #     position_quota = st.number_input('职位份额', min_value=0,
            #                                      value=3000)  # 大陸讓使用者自訂 資料設計關係，配合選擇職位是電訪專員，預設值=30000

            # 還是改有選擇區域 預設大陸(在台)
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                year = st.selectbox('選擇年份', adj_df['年'].unique(),
                                    index=adj_df['年'].tolist().index(current_year))  # 保证默认是当前年份
            with col2:
                month = st.selectbox('選擇月份', adj_df['月份'].unique(), index=current_month - 1)  # 保证默认是当前月份
            with col3:
                region = st.selectbox('選擇區域', ['大陸(在台)'])  # 假裝可以選
            with col4:
                # position = st.selectbox('选择职位', positions_df[positions_df['职位'] != '区域业务']['职位'].unique())  # 大陸現在沒有區域業務，先不顯示
                # 大陸新規則也是沒有資深、高級顧問了、也沒有區域業務，先不顯示
                position = st.selectbox('選擇職位', positions_df[(positions_df['職位'] != '區域業務') &
                                                                 (positions_df['職位'] != '資深顧問') &
                                                                 (positions_df['職位'] != '高級顧問')]['職位'].unique())  # 大陸現在沒有區域業務，先不顯示
            # 獲取 m1 和 m2 值
            m1, m2 = get_m_values(year, month)

            # # 獲取特定職位的各獎金參數 排除職位份額、區域
            # indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values(position)
            # 大陸在台 獲取特定職位的各獎金參數 排除區域
            position_quota, indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values(position)


            # 使用兩列布局(指標、成果獎金計算過程在右邊)
            col1, col2 = st.columns((1, 1.8))  # 讓selectbox跟inout之間、"指標獎金"跟selectbox之間不要太擠，
            # 第一列放使用者輸入(左邊)
            with col1:
                st.write('<br>', unsafe_allow_html=True)
                # #為了讓使用者可以輸入任意位數的小數，indicator_ach_rate、perform_ach_rate 改用text_input才能存所有位數，
                # number_input只能輸入小數點後兩位(調format也只能強制輸入固定位數)
                # 並用Decimal保留精度
                # 缺點是text_input沒有微調按鍵
                indicator_ach_rate = st.text_input('指標達成率(%)', value='100',
                                                   help='請輸入百分比值,例如131.0781表示131.0781%')
                perform_ach_rate = st.text_input('累積當區成果達成率(%)', value='100',
                                                 help='请輸入百分比值,例如131.0781表示131.0781%')
                accumulated_bonus = st.number_input('當季前面月份已領的當區成果獎金', min_value=0, value=0)

                # 將百分比值轉換為小數 .strip('%')確保就算使用者多輸入%符號也沒差
                # Decimal()傳入str型小數可保留精確的位數(預設28位)，但做運算後類型還會是 decimal.Decimal，故最外面要包float()，後續才能運算
                # 後面相關的達成率都不用調，因為基本上都會四捨五入
                indicator_ach_rate = float(Decimal(indicator_ach_rate.strip('%')) / 100)
                perform_ach_rate = float(Decimal(perform_ach_rate.strip('%')) / 100)

            # 大陸特殊規則 每季前兩個月成果獎金是min(2n,3n)，成果獎金 = 2n if perform_ach_rate>1 else 3n，每季第三個月一樣是3n
            # 要寫在這因為perform_ach_rate已被定義 且實際計算與顯示用到的perform_multi、calculate_total_bonus都在下面，在這邊寫才能影響到
            # max((perform_multi-1), 0) 避免像電訪員指標倍數本身是0被減到<0
            # 注意是控制使用者輸入的month 不是current_month
            if month % 3 != 0:  # month != 3,6,9,12
                if (1 + max((perform_multi - 1), 0) * (perform_ach_rate - 1)) < (
                        1 + perform_multi * (perform_ach_rate - 1)):
                    perform_multi -= 1

            # 第二列放計算結果(右邊)
            with col2:
                # st.write('<br>', unsafe_allow_html=True)
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
                st.write(f"<span style='font-size:21px'>**指標獎金**:</span>", unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:18px'>{position_quota:,.0f} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = **{position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1:,.0f}**</span>",
                    unsafe_allow_html=True)
                st.write(f"<span style='font-size:21px'>**累積當區成果獎金**:</span>", unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = **{position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2:,.0f}**</span>",
                    unsafe_allow_html=True)
                # st.text('*个人成果奖金部分请自行根据业绩排名计算*')

                # # 獲取總獎金與其組成
                # total_bonus, indicator_bonus, perform_bonus = calculate_total_bonus(indicator_per, perform_per,
                #                                                                     indicator_multi,
                #                                                                     perform_multi, indicator_ach_rate,
                #                                                                     perform_ach_rate, accumulated_bonus,
                #                                                                     m1,
                #                                                                     m2)
                # 大陸在台、獲取當月獎金與其組成(要放職位份額)
                total_bonus, indicator_bonus, perform_bonus = calculate_total_bonus(position_quota, indicator_per,
                                                                                    perform_per, indicator_multi,
                                                                                    perform_multi, indicator_ach_rate,
                                                                                    perform_ach_rate, accumulated_bonus,
                                                                                    m1,
                                                                                    m2)

                st.write(f"""
                            <div style='text-align: center; font-size: 40px;'>
                                <strong>當月獎金: {total_bonus:,.0f}</strong>
                            </div>
                             """, unsafe_allow_html=True)  # 調整置中、大小、粗體
                # 附註計算限制
                st.write(f"""
                            <div style='text-align: center; font-size: 15px;'>
                                *獎金金額不包含個人成果獎金、出缺勤、收款賞罰、獎懲等計算*
                            </div>
                             """, unsafe_allow_html=True)
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

            # 使用expander隱藏詳細過程
            with st.expander("點擊查看詳細過程", expanded=False):  # 預設本就是 expanded=False
                st.write("")
                st.write(f'您選擇的是：{year} 年 {month} 月')
                st.write(f"<span style='font-size:25px'>**月份調整乘數**</span>", unsafe_allow_html=True)
                st.write(f"指標月份調整乘數 = {m1} , 成果月份調整乘數 = {m2}")
                st.write(f"<span style='font-size:25px'>**獎金參數值**</span>", unsafe_allow_html=True)
                st.write(
                    f"職位份額 = {position_quota:,.0f} , 指標占比 = {indicator_per} , 成果占比 = {perform_per} , 指標倍數 = {indicator_multi} , 成果倍數 = {perform_multi}")

                st.info(f"註:每季前兩個月，累積當區成果獎金為min(2n，3n)。意即，當累積當區成果達成率小於100%，成果倍數為3；反之，成果倍數為2。而第三個月成果倍數固定為3")

                # 判斷成果獎金(已調整)與累積獎金差額與零大小，返回比較運算子
                perform_bonus_accumulated_bonus_diff = perform_bonus - accumulated_bonus


                def compare_differ(diff):
                    if diff > 0:
                        return ">"
                    elif diff < 0:
                        return "<"
                    else:
                        return "="



                # 計算過程
                st.write(f"<span style='font-size:25px'>**計算過程**</span>", unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px'>**指標獎金** = 職位份額 × 指標占比 × [ 1 + 指標倍數 × (指標達成率 - 1) ] × 指標月份調整乘數</span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px'> = {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = "
                    f"**{indicator_bonus:,.0f}**</span>", unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px'>**累積當區成果獎金** = 職位份額 × 成果占比 × [ 1 + 成果倍數 × (累積當區成果達成率 - 1) ] × 成果月份調整乘數</span>",
                    unsafe_allow_html=True)
                st.write(
                    f"<span style='font-size:16px'> = {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = "
                    f"**{perform_bonus:,.0f}**</span>", unsafe_allow_html=True)
                st.write(
                    f"**累積當區成果獎金 - 當季前面月份已領的當區成果獎金** = {perform_bonus:,.0f} - {accumulated_bonus} = **{perform_bonus_accumulated_bonus_diff:,.0f} {compare_differ(perform_bonus_accumulated_bonus_diff)} 0** ")
                st.write(
                    f"<span style='font-size:23px'>**當月獎金** = 指標獎金 + max(0, 累積當區成果獎金 - 當季前面月份已領的當區成果獎金) = "
                    f"{indicator_bonus:,.0f} + {max(0, perform_bonus_accumulated_bonus_diff):,.0f} = **{total_bonus:,.0f}**</span>",
                    unsafe_allow_html=True)


    #-----------------
    else:

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
                col1, col2 = st.columns((1, 1.8))
                # 第一列放使用者輸入(左邊)
                with col1:
                    st.write('<br>', unsafe_allow_html=True)  # 讓selectbox跟input達成率之間不要太擠
                    indicator_ach_rate = st.text_input('Indicator Achievement Rate (%)', value='100', help='Please enter the percentage value, e.g., 131.0781 means 131.0781%')
                    perform_ach_rate = st.text_input('Local Performance Achievement Rate (%)', value='100', help='Please enter the percentage value, e.g., 131.0781 means 131.0781%')

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

                    st.write(f"<span style='font-size:21px'>**Local Performance Bonus:**</span>", unsafe_allow_html=True)
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
                    # 註解
                    # st.write('*Please calculate the individual performance bonus based on the performance ranking.*')


                # 少了累積已發獎金，調整當月獎金位置
                st.write(f"""
                    <div style='text-align:center; font-size: 40px;'>
                        <strong>Monthly Bonus: {total_bonus:,.0f}</strong>
                    </div>
                     """, unsafe_allow_html=True)  # 調整置中、大小、粗體
                # 附註計算限制
                st.write(f"""
                    <div style='text-align: center; font-size: 15px;'>
                           *Bonus amount does not include individual performance bonus, attendance, collections, rewards and penalties, etc.*
                    </div>
                    """, unsafe_allow_html=True)
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

            # 使用expander隱藏詳細過程
                with st.expander("Click to see detailed process", expanded=False):
                    st.write("")
                    st.write(f'You selected: {year} Year {month} Month')
                    st.write(f"<span style='font-size:25px'>**Monthly Adjustment Multipliers**</span>", unsafe_allow_html=True)
                    st.write(f"Indicator Monthly Adjustment Multiplier = {m1} , Performance Monthly Adjustment Multiplier = {m2}")
                    st.write(f"<span style='font-size:25px'>**Bonus Parameter Values**</span>", unsafe_allow_html=True)

                    st.write(f"Position Quota = {position_quota:,.0f} , Indicator Percentage = {indicator_percentage} , Performance Percentage = {performance_percentage} ,")
                    st.write(f"Indicator Multiplier = {indicator_multiplier} , Performance Multiplier = {performance_multiplier}")

                    st.write(f"<span style='font-size:25px'>**Calculation Process**</span>", unsafe_allow_html=True)
                    # new_line = '\n'
                    # 英文太長 換行加對齊等號
                    n = '&nbsp;'  # html字元符號 半形的不換行空格，就是一般鍵盤上的空白鍵(space key)產生的空格
                    st.write(
                        f"<span style='font-size:16px'>**Indicator Bonus** = Position Quota × Indicator Percentage"
                        f" <br>{n*35}× [1 + Indicator Multiplier × (Indicator Achievement Rate - 1)] "
                        f" <br>{n*35}× Indicator Monthly Adjustment Multiplier"
                        f" <br>{n*35}= {position_quota:,.0f} * {indicator_percentage} * [1 + {indicator_multiplier} * ({indicator_ach_rate} - 1)] * {m1} = **{indicator_bonus:,.0f}**</span>",
                        unsafe_allow_html=True)

                    # st.write(
                    #     f"<span style='font-size:16px; margin-left: 112px;'> = {position_quota:,.0f} * {indicator_percentage} * [1 + {indicator_multiplier} * ({indicator_ach_rate} - 1)] * {m1} = **{indicator_bonus:,.0f}**</span>",
                    #     unsafe_allow_html=True)
                    st.write(
                        f"<span style='font-size:16px'>**Local Performance Bonus (Unadjusted)** = Position Quota × Performance Percentage "
                        f" <br>{n*85}× [1 + Performance Multiplier × (Local Performance Achievement Rate - 1)] "
                        f" <br>{n*85}× Performance Monthly Adjustment Multiplier "
                        f" <br>{n*85}= {position_quota:,.0f} * {performance_percentage} * [1 + {performance_multiplier} * ({perform_ach_rate} - 1)] * {m2} = **{unadjusted_performance_bonus:,.0f}**</span>",
                        unsafe_allow_html=True)  # 舊版{n*72}
                    # st.write(
                    #     f"<span style='font-size:16px; margin-left: 232px;'> = {position_quota:,.0f} * {performance_percentage} * [1 + {performance_multiplier} * ({perform_ach_rate} - 1)] * {m2} = **{unadjusted_performance_bonus:,.0f}**</span>",
                    #     unsafe_allow_html=True)
                    st.write(
                        f"<span style='font-size:16px; margin-left: 21px;'>***Minimum Local Performance Bonus** = Position Quota × Performance Percentage "
                        f" <br>{n*86}× {lowest} % × Performance Monthly Adjustment Multiplier "
                        f" <br>{n*86}= {position_quota:,.0f} * {performance_percentage} * {lowest / 100} * {m2} = **{position_quota * performance_percentage * (lowest / 100) * m2:,.0f}**</span>",
                        unsafe_allow_html=True)
                    # st.write(
                    #     f"<span style='font-size:16px; margin-left: 234px;'> = {position_quota:,.0f} * {performance_percentage} * {lowest / 100} * {m2} = **{position_quota * performance_percentage * (lowest / 100) * m2:,.0f}**</span>",
                    #     unsafe_allow_html=True)
                    st.write(
                        f"<span style='font-size:16px; margin-left: 20px;'>***Maximum Local Performance Bonus** = Position Quota × Performance Percentage "
                        f" <br>{n*86}× {highest} % × Performance Monthly Adjustment Multiplier"
                        f" <br>{n*86}= {position_quota:,.0f} * {performance_percentage} * {highest / 100} * {m2} = **{position_quota * performance_percentage * (highest / 100) * m2:,.0f}** </span>",
                        unsafe_allow_html=True)
                    # st.write(
                    #     f"<span style='font-size:16px; margin-left: 237px;'> = {position_quota:,.0f} * {performance_percentage} * {highest / 100} * {m2} = **{position_quota * performance_percentage * (highest / 100) * m2:,.0f}**</span>",
                    #     unsafe_allow_html=True)
                    st.write(
                        f"<span style='font-size:16px'>**Local Performance Bonus (Adjusted)** <br>= max(Minimum Local Performance Bonus, min(Maximum Local Performance Bonus, Local Performance Bonus (Unadjusted)))</span>",
                        unsafe_allow_html=True)
                    st.write(
                        f"<span style='font-size:16px'> = max({base_performance_bonus * (lowest/100) * m2:,.0f}, min({base_performance_bonus * (highest/100) * m2:,.0f}, {unadjusted_performance_bonus:,.0f})) = **{adjusted_performance_bonus:,.0f}**</span>",
                        unsafe_allow_html=True)
                    st.write(
                        f"<span style='font-size:23px'>**Monthly Bonus** = Indicator Bonus + Local Performance Bonus (Adjusted) "
                        f"<br>{n*33}= {indicator_bonus:,.0f} + {adjusted_performance_bonus:,.0f} = **{total_bonus:,.0f}**</span>",
                        unsafe_allow_html=True)
        # with c3:
        #     st.empty()
else:
    if user_input:  # 如果有輸入但不在字典中，顯示錯誤訊息
        c1, c2, c3 = st.columns((1, 0.5, 1))
        with c2:
            st.error("Invalid verification code, please re-enter!")  # 如果沒有輸入或驗證碼無效，不顯示試算器介面


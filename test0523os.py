import pandas as pd
import streamlit as st
from datetime import datetime
from decimal import Decimal

# 為了之後要自由配置版面的顯示大小，預設用到全部版面
st.set_page_config(layout="wide")

# 創建海外(在台)的年、月調整乘數對照表  1、2月過年
adj_df_ost = pd.DataFrame({
    '年': [2024] * 12 + [2025] * 12,
    '月份': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
    'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建新加坡的年、月調整乘數對照表  1、2月過年
adj_df_sig = pd.DataFrame({
    '年': [2024] * 12 + [2025] * 12,
    '月份': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
    'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建馬來西亞的年、月調整乘數對照表  1、2月過年
adj_df_mal = pd.DataFrame({
    '年': [2024] * 12 + [2025] * 12,
    '月份': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
    'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建菲律賓的年、月調整乘數對照表  12、1月過年
adj_df_phi = pd.DataFrame({
    '年': [2024] * 12 + [2025] * 12,
    '月份': list(range(1, 13)) * 2,
    'm1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
    'm2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建印度的年、月調整乘數對照表  10、11月過年
adj_df_india = pd.DataFrame({
    '年': [2024] * 12 + [2025] * 12,
    '月份': list(range(1, 13)) * 2,
    'm1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
    'm2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
})

# 創建印尼的年、月調整乘數對照表  3、4月過年
adj_df_indo = pd.DataFrame({
    '年': [2024] * 12 + [2025] * 12,
    '月份': list(range(1, 13)) * 2,
    'm1': [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
    'm2': [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建越南的年、月調整乘數對照表  1、2月過年
adj_df_viet = pd.DataFrame({
    '年': [2024] * 12 + [2025] * 12,
    '月份': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
    'm2': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
})

# 創建泰國的年、月調整乘數對照表 4、5月過年
adj_df_thai = pd.DataFrame({
    '年': [2024] * 12 + [2025] * 12,
    '月份': list(range(1, 13)) * 2,
    'm1': [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],  # 假設海外1月過年 索引0 是1月過年月 [0 if i in [0] else 1 for i in range(12)]
    'm2': [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
})

# 將不同區域的DataFrame存儲在字典adj_dfs中
adj_dfs = {
    '海外(在台)': adj_df_ost,
    '新加坡': adj_df_sig,
    '馬來西亞': adj_df_mal,
    '菲律賓': adj_df_phi,
    '印度': adj_df_india,
    '印尼': adj_df_indo,
    '越南': adj_df_viet,
    '泰國': adj_df_thai
}


# # 定義提取m1、m2的函式
# @st.cache_data
# def get_m_values(region, year, month):
#     adj_df = adj_df[region]
#     m1_m2_data = adj_df[(adj_df['年'] == year) & (adj_df['月份'] == month)]
#     return m1_m2_data.iloc[0][['m1', 'm2']]


# 創建職位的獎金參數對照表
positions_df = pd.DataFrame({
    '區域': ['海外(在台)', '海外(在台)', '海外(在台)', '海外(在台)', '新加坡', '新加坡', '馬來西亞', '菲律賓', '菲律賓', '菲律賓', '菲律賓',
            '印尼', '印尼', '印尼', '印尼', '印度', '印度', '印度', '印度', '越南', '越南', '越南', '越南', '泰國', '泰國', '泰國', '泰國'],
    '職位': ['電訪專員', '產品顧問', '高級顧問', '資深顧問', '業務', '區域業務', '區域業務', '電訪專員', '產品顧問', '業務', '區域業務',
            '電訪專員', '產品顧問', '業務', '區域業務', '電訪專員', '產品顧問', '業務', '區域業務', '電訪專員', '產品顧問', '業務', '區域業務',
            '電訪專員', '產品顧問', '業務', '區域業務'],
    '職位份額': [16000, 18000, 20000, 22000, 1800, 1800, 2500, 25000, 32000, 39000, 50000,
              3300000, 4100000, 4300000, 5200000, 27000, 35000, 38000, 40000, 7500000, 10000000,
              12000000, 15000000, 18000, 22000, 24000, 31000],
    '指標占比': [1, 0.7, 0.7, 0.7, 0.3, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3, 1, 0.7, 0.3, 0.3],
    '成果占比': [0, 0.3, 0.3, 0.3, 0.7, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7, 0, 0.3, 0.7, 0.7],
    '指標倍數': [3, 3, 3, 3, 1, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 1, 1],
    '成果倍數': [0, 1, 1, 1, 3, 3, 3, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
})

# 獲取當前年和月
current_year, current_month = datetime.now().year, datetime.now().month


# 定義提取特定區域m1、m2的新函式
@st.cache_data
def get_m_values(region, year, month):
    # adj_df = adj_df[region]
    m1_m2_data = adj_dfs[region][(adj_dfs[region]['年'] == year) & (adj_dfs[region]['月份'] == month)]
    return m1_m2_data.iloc[0][['m1', 'm2']]  # 返回series 但分別對元素賦值後會是int


# 定義獎金參數提取函式
@st.cache_data
def get_bonus_values(region, position):
    bonus_data = positions_df[(positions_df['區域'] == region) & (positions_df['職位'] == position)]
    # return bonus_data['職位份額'].values[0], bonus_data['指標占比'].values[0], bonus_data['成果占比'].values[0], \
    #        bonus_data['指標倍數'].values[0], bonus_data['成果倍數'].values[0]
    return bonus_data.iloc[0][['職位份額', '指標占比', '成果占比', '指標倍數', '成果倍數']]


# 定義海外獎金計算函式(保障50%，最高%)
lowest = 50
highest = 200


def calculate_total_bonus(position_quota, indicator_per, perform_per, indicator_multi, perform_multi,
                          indicator_ach_rate, perform_ach_rate, m1, m2):
    base_perform_bonus = position_quota * perform_per * m2  # 原本的成果獎金 要月份調整
    indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1
    o_perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2
    # 對perform_bonus進行上下限限制
    n_perform_bonus = max(base_perform_bonus * (lowest/100), min(o_perform_bonus, base_perform_bonus * (highest/100)))
    total_bonus = indicator_bonus + n_perform_bonus
    return base_perform_bonus, indicator_bonus, o_perform_bonus, n_perform_bonus, total_bonus


# 整個網頁置中，但能自由設定比例布局
c1, c2, c3 = st.columns((1, 2.5, 1))
with c1:
    st.empty()
with c2:

    # 設定 Streamlit 的網頁標題
    st.write("<h1 style='font-size: 44px;'>獎金簡易試算器<span style='font-size: 30px;'>(參考用)</span></h1>", unsafe_allow_html=True)
    # 附註:*6月啟用
    st.write(f"<span style='font-size:22px'>**:red-background[*6月啟用]**</span>", unsafe_allow_html=True)

    # 設定 Streamlit 的網頁副標題 說明計算器適用限制
    st.write('*海外事業部、業管部電訪組(不考慮新人成果獎金保障階段)*')

    # 使用四列布局(年分、月份、區域、職位選擇欄)
    # 因前面adj_dfs是dict 要用list(adj_dfs.keys())[0]保證取出第一個鍵(區域) list(adj_dfs.keys())返回所有的key包成list
    # list(adj_dfs.keys())[0] 預設取adj_dfs第一個國家且年月資料完整
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        year = st.selectbox('選擇年份', adj_dfs[list(adj_dfs.keys())[0]]['年'].unique(), index=adj_dfs[list(adj_dfs.keys())[0]]['年'].tolist().index(current_year))  # 保證預設是目前年份
    with col2:
        month = st.selectbox('選擇月份', adj_dfs[list(adj_dfs.keys())[0]]['月份'].unique(), index=current_month - 1)  # 保證預設是目前月份
    with col3:
        region = st.selectbox("選擇區域", positions_df['區域'].unique())
        # 獲取 m1 和 m2 值
        m1, m2 = get_m_values(region, year, month)
    with col4:
        # 6月規則只剩產品顧問、無資深、高級顧問
        # 各國有的職位不同，要篩選出特定區域的職位讓使用者選，'同時'排除資深、高級、區域業務
        filtered_positions = positions_df[(positions_df['區域'] == region) &
                                          (positions_df['職位'] != '資深顧問') &
                                          (positions_df['職位'] != '高級顧問') &
                                          (positions_df['職位'] != '區域業務')]['職位'].unique()

        # 避免某地區沒有職位，取不到值
        if len(filtered_positions) == 0:
            # 要給以下設定否則會取不到值
            position = ''
            position_quota, indicator_per, perform_per, indicator_multi, perform_multi = 0, 0, 0, 0, 0
            st.warning("所選區域沒有可選的職位,無法計算獎金。")
        else:
            position = st.selectbox('選擇職位', filtered_positions)
            # 獲取特定職位的各獎金參數
            position_quota, indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values(region,
                                                                                                          position)

    # 當沒有職位可以選時(選到空值時)，以下都不執行，反之都執行
    if position != '':
        # 讓selectbox跟input之間、"指標獎金"跟selectbox之間不要太擠，
        c1, c2 = st.columns(2)
        with c1:
            # st.empty()
            st.write('<br>', unsafe_allow_html=True)
        with c2:
            # st.empty()
            st.write('<br>', unsafe_allow_html=True)
        # 使用兩列布局(指標、累積成果獎金計算過程在右邊)
        col1, col2 = st.columns((1, 2.2))
        # 第一列放使用者輸入(左邊)
        with col1:
            # #為了讓使用者可以輸入任意位數的小數，indicator_ach_rate、perform_ach_rate 改用text_input才能存所有位數，
            # number_input只能輸入小數點後兩位(調format也只能強制輸入固定位數)
            # 並用Decimal保留精度
            # 缺點是text_input沒有微調按鍵
            indicator_ach_rate = st.text_input('指標達成率(%)', value='100', help='請輸入百分比值,例如131.0781表示131.0781%')
            perform_ach_rate = st.text_input('成果達成率(%)', value='100', help='請輸入百分比值,例如131.0781表示131.0781%')
            # accumulated_bonus = st.number_input('當季前面月份已領的成果獎金', min_value=0, value=0)

            # 將百分比值轉換為小數 .strip('%')確保就算使用者多輸入%符號也沒差
            # Decimal()傳入str型小數可保留精確的位數(預設28位)，但做運算後類型還會是 decimal.Decimal，故最外面要包float()，後續才能運算
            # 後面相關的達成率都不用調，因為基本上都會四捨五入
            indicator_ach_rate = float(Decimal(indicator_ach_rate.strip('%')) / 100)
            perform_ach_rate = float(Decimal(perform_ach_rate.strip('%')) / 100)

        # 第二列放計算結果(右邊)
        with col2:
            # 獲取當月獎金與其組成
            base_perform_bonus, indicator_bonus, o_perform_bonus, n_perform_bonus, total_bonus = calculate_total_bonus(
                                                                                position_quota, indicator_per,
                                                                                perform_per, indicator_multi,
                                                                                perform_multi, indicator_ach_rate,
                                                                                perform_ach_rate, m1, m2)

            print(total_bonus,indicator_bonus,o_perform_bonus,n_perform_bonus, m2)
            st.write('<br>', unsafe_allow_html=True)
            st.write(f"<span style='font-size:22px'>**指標獎金**:</span>", unsafe_allow_html=True)
            st.write(f"<span style='font-size:18px'>{position_quota:,.0f} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = **{indicator_bonus:,.0f}**</span>",
                     unsafe_allow_html=True)
            st.write(f"<span style='font-size:22px'>**成果獎金(已調整)**<span style='font-size: 15px;'>*保障{lowest}%，最高{highest}%* :</span></span>", unsafe_allow_html=True)
            # 假設成果達成率標準=1 動態顯示成果獎金算式
            if 1+perform_multi*(perform_ach_rate-1) > highest/100:
                st.write(
                    f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} *  {highest / 100} * {m2} = **{position_quota * perform_per * (highest / 100) * m2:,.0f}**</span>",
                    unsafe_allow_html=True)
            elif 1+perform_multi*(perform_ach_rate-1) < lowest/100:
                st.write(
                    f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} *  {lowest / 100} * {m2} = **{position_quota * perform_per * (lowest / 100) * m2:,.0f}**</span>",
                    unsafe_allow_html=True)
            else:
                st.write(f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = **{n_perform_bonus:,.0f}**</span>",
                         unsafe_allow_html=True)
        # 少了累積已發獎金，調整當月獎金位置
        st.write(f"""
            <div style='text-align: center; font-size: 35px;'>
                <strong>當月獎金: {total_bonus:,.0f}</strong>
            </div>
             """, unsafe_allow_html=True)  # 調整置中、大小、粗體
        # 附註計算限制
        st.write(f"""
            <div style='text-align: center; font-size: 15px;'>
                   *獎金金額不包含出缺勤、收款賞罰、獎懲等計算
            </div>
            """, unsafe_allow_html=True)

    # 使用expander隱藏詳細過程
        with st.expander("點擊查看詳細過程", expanded=False):
            # if position != '':
            st.write("")
            st.write(f'您選擇的是：{year} 年 {month} 月')
            st.write(f"<span style='font-size:25px'>**月份調整乘數**</span>", unsafe_allow_html=True)
            st.write(f"指標月份調整乘數 = {m1} , 成果月份調整乘數 = {m2}")
            st.write(f"<span style='font-size:25px'>**獎金參數值**</span>", unsafe_allow_html=True)
            st.write(
                f"職位份額 = {position_quota:,.0f} , 指標占比 = {indicator_per} , 成果占比 = {perform_per} , 指標倍數 = {indicator_multi} , 成果倍數 = {perform_multi}")

            # base_perform_bonus = position_quota * perform_per

            st.write(f"<span style='font-size:25px'>**計算過程**</span>", unsafe_allow_html=True)

            st.write(
                f"<span style='font-size:16px'>**指標獎金** = 職位份額 × 指標占比 × [1 + 指標倍數 × (指標達成率 - 1)] × 指標月份調整乘數</span>",
                unsafe_allow_html=True)
            st.write(
                f"<span style='font-size:16px'> = {position_quota:,.0f} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = **{indicator_bonus:,.0f}**</span>",
                unsafe_allow_html=True)
            st.write(
                f"<span style='font-size:16px'>**成果獎金(未調整)** = 職位份額 × 成果占比 × [1 + 成果倍數 × (成果達成率 - 1)] × 成果月份調整乘數</span>",
                unsafe_allow_html=True)
            st.write(
                f"<span style='font-size:16px'> = {position_quota:,.0f} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = **{o_perform_bonus:,.0f}**</span>",
                unsafe_allow_html=True)
            st.write(
                f"<span style='font-size:16px'>保障成果獎金 = 職位份額 × 成果占比 × {lowest} % × 成果月份調整乘數 = {position_quota:,.0f} * {perform_per} * {lowest/100} * {m2} = **{base_perform_bonus * (lowest/100) * m2:,.0f}**</span>",
                unsafe_allow_html=True)
            st.write(
                f"<span style='font-size:16px'>最高成果獎金 = 職位份額 × 成果占比 × {highest} % × 成果月份調整乘數 = {position_quota:,.0f} * {perform_per} * {highest / 100} * {m2} = **{base_perform_bonus * (highest / 100) * m2:,.0f}**</span>",
                unsafe_allow_html=True)
            st.write(
                f"<span style='font-size:22px'>***當月獎金*** *= 指標獎金 + 成果獎金(調整後) = {indicator_bonus:,.0f} + {n_perform_bonus:,.0f} =* ***{total_bonus:,.0f}***</span>",
                unsafe_allow_html=True)
with c3:
    st.empty()



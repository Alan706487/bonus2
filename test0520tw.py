import pandas as pd
import streamlit as st
from datetime import datetime
from decimal import Decimal

# 為了之後要自由配置版面的顯示大小，預設用到全部版面
st.set_page_config(layout="wide")

# 創建年、月調整乘數對照表
adj_df = pd.DataFrame({
    '年': [2024] * 12 + [2025] * 12,
    '月份': list(range(1, 13)) * 2,
    'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'm2': [0, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3]
})

# 創建職位的獎金參數對照表
positions_df = pd.DataFrame({
    '區域': ['北', '中南', '北', '中南', '北', '中南', '北', '中南', '北', '中南', '北', '中南'],
    '職位': ['電訪專員', '電訪專員', '產品顧問', '產品顧問', '資深顧問', '資深顧問', '高級顧問', '高級顧問', '業務', '業務', '區域業務', '區域業務'],
    '職位份額': [14000, 13000, 20000, 19000, 18000, 17000, 20000, 19000, 28000, 27000, 24000, 23000],
    '指標占比': [1, 1, 0.5, 0.5, 0.7, 0.7, 0.7, 0.7, 0.3, 0.3, 0.3, 0.3],
    '成果占比': [0, 0, 0, 0, 0.3, 0.3, 0.3, 0.3, 0.7, 0.7, 0.4, 0.4],
    '指標倍數': [3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1],
    '成果倍數': [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
})

# 獲取當前年和月
current_year, current_month = datetime.now().year, datetime.now().month

# 定義提取m1、m2的函式
@st.cache_data
def get_m_values(year, month):
    m1_m2_data = adj_df[(adj_df['年'] == year) & (adj_df['月份'] == month)]
    # return m1_m2_data['m1'].values[0], m1_m2_data['m2'].values[0]
    return m1_m2_data.iloc[0][['m1', 'm2']]  # 返回series 但分別對元素賦值後會是int


# 定義獎金參數提取函式
@st.cache_data
def get_bonus_values(region, position):
    bonus_data = positions_df[(positions_df['區域'] == region) & (positions_df['職位'] == position)]
    # return bonus_data['職位份額'].values[0], bonus_data['指標占比'].values[0], bonus_data['成果占比'].values[0], \
    #        bonus_data['指標倍數'].values[0], bonus_data['成果倍數'].values[0]
    return bonus_data.iloc[0][['職位份額', '指標占比', '成果占比', '指標倍數', '成果倍數']]


# 定義獎金計算函式
def calculate_total_bonus(position_quota, indicator_per, perform_per, indicator_multi, perform_multi,
                          indicator_ach_rate, perform_ach_rate, accumulated_bonus, m1, m2):
    indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1
    perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2
    total_bonus = indicator_bonus + max(0, perform_bonus - accumulated_bonus)
    return total_bonus, indicator_bonus, perform_bonus


# 整個網頁置中，但能自由設定比例布局
c1, c2, c3 = st.columns((1, 2, 1))
with c1:
    st.empty()
with c2:

    # 設定 Streamlit 的網頁標題
    st.write("<h1 style='font-size: 44px;'>獎金簡易試算器<span style='font-size: 30px;'>(參考用)</span></h1>", unsafe_allow_html=True)
    # 附註:*6月啟用
    st.write(f"<span style='font-size:22px'>**:red-background[*6月啟用]**</span>", unsafe_allow_html=True)

    # 設定 Streamlit 的網頁副標題 說明計算器適用限制
    st.write('*台灣事業部、業管部電訪組( 不考慮新人成果獎金保障階段 )*')

    # 使用四列布局(年分、月份、區域、職位選擇欄)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        year = st.selectbox('選擇年份', adj_df['年'].unique(), index=adj_df['年'].tolist().index(current_year))  # 保證預設是目前年份
    with col2:
        month = st.selectbox('選擇月份', adj_df['月份'].unique(), index=current_month - 1)  # 保證預設是目前月份
    with col3:
        region = st.selectbox("選擇區域", positions_df['區域'].unique())
    with col4:
        # position = st.selectbox('選擇職位', positions_df['職位'].unique())
        # 6月規則只剩產品顧問、無資深、高級顧問
        position = st.selectbox('選擇職位',
                                positions_df[(positions_df['職位'] != '資深顧問') & (positions_df['職位'] != '高級顧問')]['職位'].unique())

    # 獲取 m1 和 m2 值
    m1, m2 = get_m_values(year, month)

    # 獲取特定職位的各獎金參數
    position_quota, indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values(region, position)

    # 使用兩列布局(指標、累積當區成果獎金計算過程在右邊)
    col1, col2 = st.columns((1, 1.8))
    # 第一列放使用者輸入(左邊)
    with col1:
        st.write('<br>', unsafe_allow_html=True)  # 讓selectbox跟inout之間、"指標獎金"跟selectbox之間不要太擠
        # #為了讓使用者可以輸入任意位數的小數，indicator_ach_rate、perform_ach_rate 改用text_input才能存所有位數，
        # number_input只能輸入小數點後兩位(調format也只能強制輸入固定位數)
        # 並用Decimal保留精度
        # 缺點是text_input沒有微調按鍵
        indicator_ach_rate = st.text_input('指標達成率(%)', value='100', help='請輸入百分比值,例如131.0781表示131.0781%')
        perform_ach_rate = st.text_input('累積當區成果達成率(%)', value='100', help='請輸入百分比值,例如131.0781表示131.0781%')
        accumulated_bonus = st.number_input('當季前面月份已領的當區成果獎金', min_value=0, value=0)

        # 將百分比值轉換為小數 .strip('%')確保就算使用者多輸入%符號也沒差
        # Decimal()傳入str型小數可保留精確的位數(預設28位)，但做運算後類型還會是 decimal.Decimal，故最外面要包float()，後續才能運算
        # 後面相關的達成率都不用調，因為基本上都會四捨五入
        indicator_ach_rate = float(Decimal(indicator_ach_rate.strip('%')) / 100)
        perform_ach_rate = float(Decimal(perform_ach_rate.strip('%')) / 100)

    # 第二列放計算結果(右邊)
    with col2:
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

        # st.write('<br>', unsafe_allow_html=True)
        st.write(f"<span style='font-size:21px'>**指標獎金**:</span>", unsafe_allow_html=True)
        st.write(f"<span style='font-size:18px'>{position_quota:,.0f} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = **{position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1:,.0f}**</span>",
                 unsafe_allow_html=True)


        #成果獎金需區分為個人業績與當區業績 本試算器只算當區業績(業務一樣)
        st.markdown(f"<span style='font-size:21px'>**累積當區成果獎金**:</span>", unsafe_allow_html=True)
        st.markdown(
            f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = **{position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2:,.0f}**</span>",
            unsafe_allow_html=True)  # help='個人成果獎金部分請自行根據業績排名計算'
        # st.text('*個人成果獎金部分請自行根據業績排名計算*')

        # 獲取當月獎金與其組成
        total_bonus, indicator_bonus, perform_bonus = calculate_total_bonus(position_quota, indicator_per,
                                                                            perform_per, indicator_multi,
                                                                            perform_multi, indicator_ach_rate,
                                                                            perform_ach_rate, accumulated_bonus, m1,
                                                                            m2)
        st.write(f"""
            <div style='text-align: center; font-size: 40px;'>
                <strong>當月獎金: {total_bonus:,.0f}
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
        st.write("")  # 在此添加一行空內容
        st.write(f'您選擇的是：{year} 年 {month} 月')
        st.write(f"<span style='font-size:25px'>**月份調整乘數**</span>", unsafe_allow_html=True)
        st.write(f"指標月份調整乘數 = {m1} , 成果月份調整乘數 = {m2}")
        st.write(f"<span style='font-size:25px'>**獎金參數值**</span>", unsafe_allow_html=True)
        st.write(
            f"職位份額 = {position_quota:,.0f} , 指標占比 = {indicator_per} , 成果占比 = {perform_per} , 指標倍數 = {indicator_multi} , 成果倍數 = {perform_multi}")

        # 判斷累積當區成果獎金(已調整)與當季前面月份已領的當區成果獎金差額與零大小，返回比較運算子
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
            f"<span style='font-size:16px'> = {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1) ] * {m1} = "
            f"**{indicator_bonus:,.0f}**</span>", unsafe_allow_html=True)
        # 註明當區成果獎金
        st.write(
            f"<span style='font-size:16px'>**累積當區成果獎金** = 職位份額 × 成果占比 × [ 1 + 成果倍數 × (累積當區成果達成率 - 1) ] × 成果月份調整乘數</span>",
            unsafe_allow_html=True)
        st.write(
            f"<span style='font-size:16px'> = {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = "
            f"**{perform_bonus:,.0f}**</span>", unsafe_allow_html=True)

        # 註明當區成果獎金
        st.write(
            f"**累積當區成果獎金 - 當季前面月份已領的當區成果獎金** = {perform_bonus:,.0f} - {accumulated_bonus} = **{perform_bonus_accumulated_bonus_diff:,.0f} {compare_differ(perform_bonus_accumulated_bonus_diff)} 0**")
        st.write(f"<span style='font-size:23px'>**當月獎金** = 指標獎金 + max(0, 累積當區成果獎金 - 當季前面月份已領的當區成果獎金) = "
                 f"{indicator_bonus:,.0f} + {max(0, perform_bonus_accumulated_bonus_diff):,.0f} = **{total_bonus:,.0f}**</span>", unsafe_allow_html=True)
with c3:
    st.empty()

#------------



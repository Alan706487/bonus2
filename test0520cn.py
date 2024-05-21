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

# 創建職位的獎金參數對照表 大陸無區域、職位份額
positions_df = pd.DataFrame({
    '職位': ['電訪專員', '產品顧問', '資深顧問', '高級顧問', '業務', '區域業務'],
    '指標占比': [1, 0.7, 0.7, 0.7, 0.3, 0.3],
    '成果占比': [0, 0.3, 0.3, 0.3, 0.7, 0.7],
    '指標倍數': [3, 3, 3, 3, 1, 1],
    '成果倍數': [0, 3, 3, 3, 3, 3]
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
    return bonus_data.iloc[0][['指標占比', '成果占比', '指標倍數', '成果倍數']]


# 定義獎金計算函式  大陸position_quota是自輸，涵式不用放
def calculate_total_bonus(indicator_per, perform_per, indicator_multi, perform_multi,
                          indicator_ach_rate, perform_ach_rate, accumulated_bonus, m1, m2):
    indicator_bonus = position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1
    perform_bonus = position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2
    total_bonus = indicator_bonus + max(0, perform_bonus - accumulated_bonus)
    return total_bonus, indicator_bonus, perform_bonus


# 整個網頁置中，但能自由設定比例布局
c1, c2, c3 = st.columns((1, 2.5, 1))
with c1:
    st.empty()
with c2:
    # 設定 Streamlit 的網頁標題
    st.title('獎金試算器')
    # 設定 Streamlit 的網頁副標題 說明計算器適用限制
    st.write('*大陸事業部、業管部電訪組(不考慮新人成果獎金保障階段)*')

    # 使用四列布局(年分、月份、區域、職位選擇欄)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        year = st.selectbox('選擇年份', adj_df['年'].unique(), index=adj_df['年'].tolist().index(current_year))  # 保證預設是目前年份
    with col2:
        month = st.selectbox('選擇月份', adj_df['月份'].unique(), index=current_month - 1)  # 保證預設是目前月份
    with col3:
        position = st.selectbox('選擇職位', positions_df['職位'].unique())
    with col4:
        position_quota = st.number_input('職位份額', min_value=0, value=0)  # 大陸讓使用者自訂

    # 獲取 m1 和 m2 值
    m1, m2 = get_m_values(year, month)

    # 獲取特定職位的各獎金參數 排除職位份額、區域
    indicator_per, perform_per, indicator_multi, perform_multi = get_bonus_values(position)

    # 讓selectbox跟inout之間、"指標獎金"跟selectbox之間不要太擠，
    c1, c2 = st.columns(2)
    with c1:
        # st.empty()
        st.write('<br>', unsafe_allow_html=True)
    with c2:
        # st.empty()
        st.write('<br>', unsafe_allow_html=True)

    # 使用兩列布局(指標、成果獎金計算過程在右邊)
    col1, col2 = st.columns((1, 2.2))
    # 第一列放使用者輸入(左邊)
    with col1:
        # #為了讓使用者可以輸入任意位數的小數，indicator_ach_rate、perform_ach_rate 改用text_input才能存所有位數，
        # number_input只能輸入小數點後兩位(調format也只能強制輸入固定位數)
        # 並用Decimal保留精度
        # 缺點是text_input沒有微調按鍵
        indicator_ach_rate = st.text_input('指標達成率(%)', value='100',
                                           help='請輸入百分比值,例如131.0781表示131.0781%')
        perform_ach_rate = st.text_input('累積成果達成率(%)', value='100',
                                         help='請輸入百分比值,例如131.0781表示131.0781%')
        accumulated_bonus = st.number_input('當季累積成果獎金(累積獎金)', min_value=0, value=0)

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
        if (1 + max((perform_multi - 1), 0) * (perform_ach_rate - 1)) < (1 + perform_multi * (perform_ach_rate - 1)):
            perform_multi -= 1

    # 第二列放計算結果(右邊)
    with col2:
        st.write('<br>', unsafe_allow_html=True)
        st.write(f"<span style='font-size:22px'>**指標獎金**:</span>", unsafe_allow_html=True)
        st.write(
            f"<span style='font-size:18px'>{position_quota:,.0f} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = **{position_quota * indicator_per * (1 + indicator_multi * (indicator_ach_rate - 1)) * m1:,.0f}**</span>",
            unsafe_allow_html=True)
        st.write(f"<span style='font-size:22px'>**累積成果獎金**:</span>", unsafe_allow_html=True)
        st.write(
            f"<span style='font-size:18px'>{position_quota:,.0f} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = **{position_quota * perform_per * (1 + perform_multi * (perform_ach_rate - 1)) * m2:,.0f}**</span>",
            unsafe_allow_html=True)


        # 獲取總獎金與其組成
        total_bonus, indicator_bonus, perform_bonus = calculate_total_bonus(indicator_per, perform_per, indicator_multi,
                                                                            perform_multi, indicator_ach_rate,
                                                                            perform_ach_rate, accumulated_bonus, m1,
                                                                            m2)
        st.write(f"""
                    <div style='text-align: center; font-size: 35px;'>
                        <strong>當月獎金: {total_bonus:,.0f}</strong>
                    </div>
                     """, unsafe_allow_html=True)  # 調整置中、大小、粗體


    # 使用expander隱藏詳細過程
    with st.expander("點擊查看詳細過程", expanded=False):  # 預設本就是 expanded=False
        st.write("")  # 在此添加一行空內容
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


        # 計算過程
        st.write(f"<span style='font-size:25px'>**計算過程**</span>", unsafe_allow_html=True)
        st.write(
            f"<span style='font-size:16px'>**指標獎金** = 職位份額×指標占比×[1+指標倍數×(指標達成率-1)]×指標月份調整乘數</span>",
            unsafe_allow_html=True)
        st.write(
            f"<span style='font-size:16px'> = {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = "
            f"**{indicator_bonus:,.0f}**</span>", unsafe_allow_html=True)
        st.write(
            f"<span style='font-size:16px'>**累積成果獎金** = 職位份額×成果占比×[1+成果倍數×(累積成果達成率-1)]×成果月份調整乘數</span>",
            unsafe_allow_html=True)
        st.write(
            f"<span style='font-size:16px'> = {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = "
            f"**{perform_bonus:,.0f}**</span>", unsafe_allow_html=True)
        st.write(
            f"**累積成果獎金 - 當季前面月份已領的成果獎金** = {perform_bonus:,.0f} - {accumulated_bonus} = **{perform_bonus_accumulated_bonus_diff:,.0f} {compare_differ(perform_bonus_accumulated_bonus_diff)} 0**")
        st.write(
            f"<span style='font-size:22px'>***當月獎金*** *= 指標獎金 + max(0, 累積成果獎金 - 當季前面月份已領的成果獎金) = "
            f"{indicator_bonus:,.0f} + {max(0, perform_bonus_accumulated_bonus_diff):,.0f} =* ***{total_bonus:,.0f}***</span>",
            unsafe_allow_html=True)
with c3:
    st.empty()

        # st.write(f"<span style='font-size:25px'>**計算過程**</span>", unsafe_allow_html=True)
        # st.write(
        #     f"<span style='font-size:16px'>指標獎金 = 職位份額×指標占比×[1+指標倍數×(指標達成率-1)]×指標月份調整乘數</span>",
        #     unsafe_allow_html=True)
        # st.write(
        #     f"<span style='font-size:16px'> = {position_quota} * {indicator_per} * [1 + {indicator_multi} * ({indicator_ach_rate} - 1)] * {m1} = "
        #     f"{indicator_bonus:.0f}</span>", unsafe_allow_html=True)
        # st.write(
        #     f"<span style='font-size:16px'>成果獎金 = 職位份額×成果占比×[1+成果倍數×(成果達成率-1)]×成果月份調整乘數</span>",
        #     unsafe_allow_html=True)
        # st.write(
        #     f"<span style='font-size:16px'> = {position_quota} * {perform_per} * [1 + {perform_multi} * ({perform_ach_rate} - 1)] * {m2} = "
        #     f"{perform_bonus:.0f}</span>", unsafe_allow_html=True)
        # st.write(
        #     f"成果獎金 - 累積獎金 = {perform_bonus:.0f} - {accumulated_bonus} = {perform_bonus_accumulated_bonus_diff:.0f} {compare_differ(perform_bonus_accumulated_bonus_diff)} 0")
        # st.write(f"<span style='font-size:18px'>***總獎金 = 指標獎金 + max(0, 成果獎金 - 累積獎金) = "
        #          f"{indicator_bonus:.0f} + {max(0, perform_bonus_accumulated_bonus_diff):.0f} = {total_bonus:.0f}***</span>", unsafe_allow_html=True)



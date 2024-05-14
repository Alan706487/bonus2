import pandas as pd
import streamlit as st

# 创建数据类
class BonusData:
    def __init__(self):
        # 创建年、月调整乘数对照表
        self.adj_data = {
            '年': [2024] * 12 + [2025] * 12,
            '月份': list(range(1, 13)) * 2,
            'm1': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'm2': [0, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3]
        }
        self.adj_df = pd.DataFrame(self.adj_data)

        # 创建职位的奖金参数对照表
        self.positions_data = {
            '区域': ['北', '中南', '北', '中南', '北', '中南', '北', '中南', '北', '中南', '北', '中南'],
            '职位': ['业务', '业务', '区域业务', '区域业务', '电访', '电访', '产品顾问', '产品顾问', '高级顾问', '高级顾问', '资深顾问', '资深顾问'],
            '职位份额': [22000, 21000, 24000, 23000, 14000, 13000, 16000, 15000, 20000, 19000, 18000, 17000],
            '指标占比': [0.3, 0.3, 0.3, 0.3, 1, 1, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
            '成果占比': [0.7, 0.7, 0.7, 0.7, 0, 0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
            '指标倍数': [1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3],
            '成果倍数': [3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3]
        }
        self.positions_df = pd.DataFrame(self.positions_data)

# 创建计算逻辑类
class BonusCalculator(BonusData):
    def __init__(self):
        super().__init__()

    def get_m_values(self, year, month):
        m_data = self.adj_df[(self.adj_df['年'] == year) & (self.adj_df['月份'] == month)]
        return m_data['m1'].values[0], m_data['m2'].values[0]

    def get_bonus_values(self, region, position):
        bonus_data = self.positions_df[(self.positions_df['区域'] == region) & (self.positions_df['职位'] == position)]
        return bonus_data.iloc[0]

    def calculate_bonus(self, year, month, region, position, ind_rate, perf_rate, accumulated_bonus):
        m1, m2 = self.get_m_values(year, month)
        position_data = self.get_bonus_values(region, position)

        ind_bonus = position_data['职位份额'] * position_data['指标占比'] * (1 + position_data['指标倍数'] * (ind_rate - 1)) * m1
        perf_bonus = position_data['职位份额'] * position_data['成果占比'] * (1 + position_data['成果倍数'] * (perf_rate - 1)) * m2
        total_bonus = ind_bonus + max(0, perf_bonus - accumulated_bonus)

        return total_bonus, ind_bonus, perf_bonus

# Streamlit 表现层
def main():
    st.title('当月奖金计算器')
    st.write('*台湾区非保障一般职员，排除海外部、定制部*')

    # 创建计算实例
    calculator = BonusCalculator()

    # 年、月份选择框
    year = st.selectbox('选择年份', calculator.adj_df['年'].unique())
    month = st.selectbox('选择月份', calculator.adj_df['月份'].unique())

    # 透过下拉选单让使用者选择职位
    region = st.selectbox("选择区域", calculator.positions_df['区域'].unique())
    position = st.selectbox('选择职位', calculator.positions_df['职位'].unique())

    # 使用者输入指标达成率、成果达成率和当季累积成果奖金
    ind_rate = st.number_input('指标达成率（输入百分比值，例如150表示150%）', min_value=0, value=100) / 100
    perf_rate = st.number_input('成果达成率（输入百分比值，例如150表示150%）', min_value=0, value=100) / 100
    accumulated_bonus = st.number_input('当季累积成果奖金(累积奖金)', min_value=0, value=0)

    # 计算总奖金与其组成
    total_bonus, ind_bonus, perf_bonus = calculator.calculate_bonus(year, month, region, position, ind_rate, perf_rate, accumulated_bonus)

    # 输出结果
    st.write(f'您选择的是：{year} 年 {month} 月')
    st.write(f"**月份调整乘数**")
    m1, m2 = calculator.get_m_values(year, month)
    st.write(f"指标月份调整乘数 = {m1} , 成果月份调整乘数 = {m2}")

    st.write(f"**奖金参数值**")
    position_data = calculator.get_bonus_values(region, position)
    st.write(f"职位份额 = {position_data['职位份额']} , 指标占比 = {position_data['指标占比']} , 成果占比 = {position_data['成果占比']} , 指标倍数 = {position_data['指标倍数']} , 成果倍数 = {position_data['成果倍数']}")

    st.write(f"**计算过程**")
    st.write(f"指标奖金: {position_data['职位份额']} * {position_data['指标占比']} * [1 + {position_data['指标倍数']} * ({ind_rate} - 1)] * {m1} = {ind_bonus:.0f}")
    st.write(f"成果奖金: {position_data['职位份额']} * {position_data['成果占比']} * [1 + {position_data['成果倍数']} * ({perf_rate} - 1)] * {m2} = {perf_bonus:.0f}")

    perf_bonus_accumulated_bonus_diff = perf_bonus - accumulated_bonus
    if perf_bonus_accumulated_bonus_diff > 0:
        perf_bonus_accumulated_bonus_diff = perf_bonus - accumulated_bonus
        if perf_bonus_accumulated_bonus_diff > 0:
            st.write(
                f"成果奖金 - 累积奖金 = {perf_bonus:.0f} - {accumulated_bonus} = {perf_bonus_accumulated_bonus_diff:.0f} > 0")
        elif perf_bonus_accumulated_bonus_diff < 0:
            st.write(
                f"成果奖金 - 累积奖金 = {perf_bonus:.0f} - {accumulated_bonus} = {perf_bonus_accumulated_bonus_diff:.0f} < 0")
        else:
            st.write(
                f"成果奖金 - 累积奖金 = {perf_bonus:.0f} - {accumulated_bonus} = {perf_bonus_accumulated_bonus_diff:.0f} = 0")

        st.write(f"**总奖金: {total_bonus:.0f}**")

    if __name__ == '__main__':
        main()
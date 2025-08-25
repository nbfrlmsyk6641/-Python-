import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# 加载您的数据
try:
    df = pd.read_csv('0823_wm_N_1.csv')
except FileNotFoundError:
    print("错误：未找到CSV文件。请将 '0823_wm_N_1.csv' 文件放置在正确目录下。")
    # 创建一个空的DataFrame以避免程序崩溃
    df = pd.DataFrame({'Time': [], 'Wm': [], 'Wr': []})

if not df.empty:
    # 定义滤波窗口大小
    window_size = 11

    # 应用移动平均滤波
    # center=True可以减少相位滞后，min_periods=1确保即使在数据开头也能有输出
    df['Wm_ma'] = df['Wm'].rolling(window=window_size, center=True, min_periods=1).mean()

    # 应用中位值滤波
    df['Wm_median'] = df['Wm'].rolling(window=window_size, center=True, min_periods=1).median()

    # --- 绘图部分 ---
    plt.figure(figsize=(15, 10))

    # 完整视图
    ax1 = plt.subplot(2, 1, 1)
    ax1.plot(df['Time'], df['Wm'], label='原始传感器信号 (Original)', color='lightblue', alpha=0.8)
    ax1.plot(df['Time'], df['Wm_ma'], label=f'移动平均滤波 (Moving Avg, N={window_size})', color='green', linewidth=2)
    ax1.plot(df['Time'], df['Wm_median'], label=f'中位值滤波 (Median, N={window_size})', color='red', linewidth=2)
    ax1.plot(df['Time'], df['Wr'], label='期望值 (Reference)', color='black', linestyle='--', linewidth=2)
    ax1.set_title('滤波算法效果对比 (完整视图)', fontsize=16)
    ax1.set_ylabel('电机转速 (r/min)', fontsize=12)
    ax1.legend(fontsize=12)
    ax1.grid(True)
    ax1.set_xlim(df['Time'].min(), df['Time'].max())
    ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    # 局部放大视图
    ax2 = plt.subplot(2, 1, 2)
    ax2.plot(df['Time'], df['Wm'], label='原始传感器信号', color='lightblue', marker='o', markersize=3, linestyle='-')
    ax2.plot(df['Time'], df['Wm_ma'], label=f'移动平均滤波 (N={window_size})', color='green', linewidth=2.5)
    ax2.plot(df['Time'], df['Wm_median'], label=f'中位值滤波 (N={window_size})', color='red', linewidth=2.5)
    ax2.plot(df['Time'], df['Wr'], label='期望值', color='black', linestyle='--', linewidth=2)
    ax2.set_title('滤波算法效果对比 (局部放大视图)', fontsize=16)
    ax2.set_xlabel('时间 (s)', fontsize=12)
    ax2.set_ylabel('电机转速 (r/min)', fontsize=12)
    ax2.legend(fontsize=12)
    ax2.grid(True)

    # 自动选择一个区域进行放大
    if len(df) > 200:
        start_index = 100
        end_index = 150
        start_time = df['Time'].iloc[start_index]
        end_time = df['Time'].iloc[end_index]
        y_min = df['Wm'].iloc[start_index:end_index].min() - 2
        y_max = df['Wm'].iloc[start_index:end_index].max() + 2
        ax2.set_xlim(start_time, end_time)
        ax2.set_ylim(y_min, y_max)
    
    plt.tight_layout()
    plt.savefig("filtering_comparison.png")
    print("绘图已保存为 filtering_comparison.png")
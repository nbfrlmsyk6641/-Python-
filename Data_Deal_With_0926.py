import pandas as pd
import numpy as np
import os

# --- 1. 配置区 ---
# 未来您只需要修改这个区域即可

# ⚠️ 请将此路径修改为您存放4个CSV文件的实际文件夹路径
data_folder = r'D:\SZU\Experiment\Experiment_Data\0921\Wm_Beta_Data\base'
# 建议将处理后的文件存放在一个新的输出文件夹中
output_folder = r'D:\SZU\Experiment\Experiment_Data\0921\Wm_Beta_Data\base\Combined' 

# ⚠️ 【非常重要】请在这里按【时间顺序】列出您的4个CSV文件名
files_to_combine = [
    '0921_Wm_0.1_0_1s.csv',
    '0921_Wm_0.1_1_2s.csv',
    '0921_Wm_0.1_2_3s.csv',
    '0921_Wm_0.1_3_5s.csv'
]

# 这是最终合并后要保存的文件名
output_filename = '0921_Wm_0.1_5s.csv'

# 已知的采样周期 (秒)
sampling_period = 0.001

# --- 2. 核心处理逻辑 (通常无需修改) ---

# 如果输出文件夹不存在，则自动创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"输出文件夹不存在，已自动创建: {output_folder}")

print("--- 开始合并文件并重建时间轴 ---")
print("-" * 50)

# 用于存放从每个文件中读取的数据（不含时间列）
list_of_data_dfs = []

try:
    # --- 步骤1: 循环读取文件，只提取数据列 ---
    for filename in files_to_combine:
        file_path = os.path.join(data_folder, filename)
        print(f"正在读取文件: {filename} ...")
        
        # 读取CSV文件
        df = pd.read_csv(file_path)
        
        # 只提取'Wm'和'Wr'这两列数据，丢弃原始的时间列
        data_only_df = df[['Wm', 'Wr']]
        
        # 将只包含数据的DataFrame添加到列表中
        list_of_data_dfs.append(data_only_df)

    # --- 步骤2: 拼接所有数据列 ---
    print("\n所有文件读取完毕，正在拼接数据...")
    # 将列表中的所有DataFrame垂直堆叠
    combined_data_df = pd.concat(list_of_data_dfs, ignore_index=True)
    total_rows = len(combined_data_df)
    print(f"数据拼接完成，总行数: {total_rows}")

    # --- 步骤3: 生成一个全新的、完美连续的时间列 ---
    print("正在生成新的时间列...")
    # 使用numpy的arange函数生成时间序列
    # np.arange(start, stop, step)
    # stop参数是 total_rows * sampling_period (5000 * 0.001 = 5.0)
    new_time_column = np.arange(0, total_rows * sampling_period, sampling_period)

    # --- 步骤4: 组合新的时间列和拼接好的数据 ---
    # 创建一个最终的DataFrame
    final_df = pd.DataFrame()
    final_df['Time'] = new_time_column
    # 将拼接好的数据列附加到新时间列的后面
    final_df[['Wm', 'Wr']] = combined_data_df

    # --- 步骤5: 保存最终的文件 ---
    output_path = os.path.join(output_folder, output_filename)
    final_df.to_csv(output_path, index=False)

    print("-" * 50)
    print(f"✅ 处理完成！")
    print(f"总数据行数: {len(final_df)}")
    print(f"时间范围: {final_df['Time'].min():.3f}s 至 {final_df['Time'].max():.3f}s")
    print(f"结果已保存至: {output_filename}")

except FileNotFoundError as e:
    print(f"❌ 错误：找不到文件 '{os.path.basename(e.filename)}'。请检查文件名和路径。")
except KeyError as e:
    print(f"❌ 错误：在文件中找不到指定的列名 {e}。请确保所有文件都包含 'Wm' 和 'Wr' 列。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")
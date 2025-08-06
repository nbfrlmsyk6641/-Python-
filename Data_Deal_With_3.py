# 

import pandas as pd
import os

# --- 1. 配置输入输出及文件列表 ---
# (这部分与之前完全相同，保持不变)
input_folder = r'C:\Users\23688\Desktop\实验数据\0805\非0开始\处理后的数据\u&&y'
output_folder = r'C:\Users\23688\Desktop\实验数据\0805\非0开始\处理后的数据\u&&y'
file_names = [
    '0_200_400_600_u_y.csv',
    '600_800_1000_u_y.csv',
    '1000_1_u_y.csv',
    '1000_2_u_y.csv',
    '1000_800_600_400_u_y.csv',
    '400_200_0_u_y.csv'
]
# 建议为最终文件换个新名字，以体现行数
output_filename = 'Raw_Training_data(195900).csv'
final_column_names = ['uk_1', 'uk_2', 'yk_1', 'yk_2', 'yk']

# --- 准备工作 ---
output_file_path = os.path.join(output_folder, output_filename)
list_of_processed_dfs = []

# --- 自动创建输出文件夹 ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"输出文件夹不存在，已自动创建: {output_folder}")

print("--- 开始批量提取并合并CSV文件 ---")

try:
    # --- 2. 循环处理文件列表中的每一个文件 ---
    # (这部分与之前完全相同，保持不变)
    for filename in file_names:
        file_path = os.path.join(input_folder, filename)
        print(f"正在处理文件: {filename} ...")
        df = pd.read_csv(file_path, usecols=[1, 2, 3, 4, 5])
        list_of_processed_dfs.append(df)
    
    if not list_of_processed_dfs:
        print("⚠️ 警告：未能读取任何数据文件。")
    else:
        # --- 4. 合并数据 ---
        # (这部分与之前完全相同，保持不变)
        print("\n所有文件处理完毕，正在合并...")
        combined_df = pd.concat(list_of_processed_dfs, ignore_index=True)

        # --- 5. 设置列名 ---
        # (这部分与之前完全相同，保持不变)
        combined_df.columns = final_column_names

        # --- 新增功能：按要求截取指定行数的数据 ---
        print("-" * 30)
        print(f"数据合并完成，原始总行数: {len(combined_df)}")

        rows_to_keep = 195900 # 定义需要保留的行数
        
        if len(combined_df) > rows_to_keep:
            print(f"按要求只保留前 {rows_to_keep} 行数据...")
            # .iloc[:N] 会选取从第0行到第N-1行的数据，即前N行
            trimmed_df = combined_df.iloc[:rows_to_keep]
            print(f"已丢弃末尾 {len(combined_df) - len(trimmed_df)} 行数据。")
        else:
            # 如果总行数不足，则保留所有数据
            print(f"总行数不足 {rows_to_keep}，保留所有数据。")
            trimmed_df = combined_df

        # --- 6. 保存最终截取好的文件 ---
        # 【已修改】注意这里保存的是截取后的 trimmed_df
        trimmed_df.to_csv(output_file_path, index=False)

        print("-" * 30)
        print(f"✅ 处理完成！")
        # 【已修改】报告最终保存的行数
        print(f"最终保存的数据总行数: {len(trimmed_df)}")
        print(f"结果已保存到文件: {output_filename}")

except FileNotFoundError as e:
    # (错误处理部分与之前完全相同，保持不变)
    print(f"❌ 错误：找不到文件。")
    print(f"请检查文件是否存在于指定路径: {e.filename}")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")
import pandas as pd
import os

# --- 1. 配置输入输出及文件列表 ---
# ⚠️ 请在这里配置你的文件夹路径
input_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据\处理后的数据\Train_Data'
output_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据\处理后的数据\Train_Data'

# ⚠️ 请在这里按【期望的合并顺序】列出你的7个CSV文件名
file_names = [
    '0_200_400_Trainingdata.csv',
    '400_600_800_Trainingdata.csv',
    '800_1000_Trainingdata.csv',
    '1000_900_800_Trainingdata.csv',
    '800_700_600_Trainingdata.csv',
    '600_500_400_Trainingdata.csv',
    '400_300_200_100_Trainingdata.csv'
]

# 这是最终合并后要保存的文件名
output_filename = 'Raw_Trainingdata(0-200-400-600-800-1000-900-800-700-600-500-400-300-200-100).csv'

# --- 准备工作 ---
output_file_path = os.path.join(output_folder, output_filename)
# 用于存放从每个文件中读取的数据（DataFrame）
list_of_dfs = []

# --- 自动创建输出文件夹 ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"输出文件夹不存在，已自动创建: {output_folder}")

print("--- 开始批量合并CSV文件 ---")

try:
    # --- 2. 循环读取文件列表中的每一个文件 ---
    for filename in file_names:
        file_path = os.path.join(input_folder, filename)
        print(f"正在读取文件: {filename} ...")
        
        # 读取CSV文件并将其添加到我们的列表中
        df = pd.read_csv(file_path)
        list_of_dfs.append(df)
    
    # --- 3. 检查是否成功读取了任何文件 ---
    if not list_of_dfs:
        print("⚠️ 警告：未能读取任何数据文件，请检查文件列表和输入文件夹路径。")
    else:
        # --- 4. 将列表中的所有数据（DataFrame）合并成一个 ---
        # pd.concat 会将列表中的DataFrame按顺序垂直堆叠
        # ignore_index=True 会创建一个新的、连续的行索引 (0, 1, 2, ...)，这非常重要
        print("\n所有文件读取完毕，正在合并...")
        combined_df = pd.concat(list_of_dfs, ignore_index=True)

        # --- 5. 确保最终的列名符合要求 ---
        # 这是一个好习惯，即使原始文件的列名已经是正确的，也再次设定以确保万无一失
        final_column_names = ['uk_1', 'uk_2', 'yk_1', 'yk_2', 'yk']
        combined_df.columns = final_column_names

        # --- 6. 保存最终合并好的文件 ---
        combined_df.to_csv(output_file_path, index=False)

        print("-" * 30)
        print(f"✅ 所有文件合并成功！")
        print(f"共处理了 {len(list_of_dfs)} 个文件。")
        print(f"总数据行数: {len(combined_df)}")
        print(f"结果已保存到文件: {output_filename}")

except FileNotFoundError as e:
    print(f"❌ 错误：找不到文件。")
    print(f"请检查文件是否存在于指定路径: {e.filename}")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")
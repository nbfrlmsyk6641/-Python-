# 将原始训练数据集划分为训练集、验证集和测试集

import pandas as pd
import os
import math

# --- 1. 配置输入输出文件及划分比例 ---
# ⚠️ 请在这里配置你的文件夹路径
input_folder = r'F:\实验数据\0905\负载-转速数据'
output_folder = r'F:\实验数据\0905\负载-转速数据'

# ⚠️ 请在这里确认你的输入文件名
input_filename = '0906_ALL.csv'

# 定义划分比例
train_ratio = 0.8
validation_ratio = 0.1
# 测试集比例会自动计算得出，确保总和为1

# --- 准备工作 ---
input_file_path = os.path.join(input_folder, input_filename)

# 定义输出文件名
train_filename = 'train_set.csv'
validation_filename = 'validation_set.csv'
test_filename = 'test_set.csv'

# --- 自动创建输出文件夹 ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"输出文件夹不存在，已自动创建: {output_folder}")

print(f"--- 开始划分数据集: {input_filename} ---")

try:
    # --- 2. 读取完整的数据集 ---
    print(f"正在读取源文件: {input_filename} ...")
    full_df = pd.read_csv(input_file_path)
    total_rows = len(full_df)
    print(f"文件读取成功，共 {total_rows} 行数据。")
    print("-" * 30)

    # --- 3. 计算切分点 ---
    # 使用math.floor确保我们得到整数的行数索引
    train_end_index = math.floor(total_rows * train_ratio)
    validation_end_index = math.floor(total_rows * (train_ratio + validation_ratio))

    print("根据比例计算切分点：")
    print(f"训练集 (前 {train_ratio:.0%}): {train_end_index} 行 (0 至 {train_end_index - 1})")
    print(f"验证集 (中 {validation_ratio:.0%}): {validation_end_index - train_end_index} 行 ({train_end_index} 至 {validation_end_index - 1})")
    print(f"测试集 (后 {total_rows - validation_end_index} 行 ({validation_end_index} 至 {total_rows - 1})")
    print("-" * 30)

    # --- 4. 执行切片操作 ---
    # 使用 .iloc 按整数位置进行切片
    train_df = full_df.iloc[0:train_end_index]
    validation_df = full_df.iloc[train_end_index:validation_end_index]
    test_df = full_df.iloc[validation_end_index:]

    # --- 5. 分别保存三个数据集文件 ---
    # 训练集
    train_output_path = os.path.join(output_folder, train_filename)
    train_df.to_csv(train_output_path, index=False)
    print(f"✅ 训练集已保存至 '{train_filename}' ({len(train_df)} 行)")

    # 验证集
    validation_output_path = os.path.join(output_folder, validation_filename)
    validation_df.to_csv(validation_output_path, index=False)
    print(f"✅ 验证集已保存至 '{validation_filename}' ({len(validation_df)} 行)")

    # 测试集
    test_output_path = os.path.join(output_folder, test_filename)
    test_df.to_csv(test_output_path, index=False)
    print(f"✅ 测试集已保存至 '{test_filename}' ({len(test_df)} 行)")

    print("\n数据集划分全部完成！")

except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{input_file_path}'。")
    print("请检查输入文件夹路径和文件名是否正确。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")

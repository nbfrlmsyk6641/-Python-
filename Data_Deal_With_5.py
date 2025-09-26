# import pandas as pd
# import os
# import numpy as np 

# # --- 1. 配置输入输出文件夹及文件名 ---
# # ⚠️ 请在这里配置你的文件夹路径
# input_folder = r'F:\实验数据\0905\负载-转速数据'
# output_folder = r'F:\实验数据\0905\负载-转速数据'

# # 定义输入文件名
# train_filename = 'train_set.csv'
# validation_filename = 'validation_set.csv'
# test_filename = 'test_set.csv'

# # 定义输出文件名
# scalers_filename = 'scalers_from_train_set.csv'
# train_norm_filename = 'train_set_normalized.csv'
# validation_norm_filename = 'validation_set_normalized.csv'
# test_norm_filename = 'test_set_normalized.csv'

# # --- 准备工作 ---
# # 自动创建输出文件夹
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"--- 开始对数据集进行最大-最小值归一化 ---")

# try:
#     # --- 2. 读取所有数据集 ---
#     train_path = os.path.join(input_folder, train_filename)
#     validation_path = os.path.join(input_folder, validation_filename)
#     test_path = os.path.join(input_folder, test_filename)

#     print(f"正在读取文件: {train_filename}, {validation_filename}, {test_filename}...")
#     train_df = pd.read_csv(train_path)
#     validation_df = pd.read_csv(validation_path)
#     test_df = pd.read_csv(test_path)
#     print("所有文件读取成功！")
#     print("-" * 30)

#     # --- 3. 从训练集中学习最大值和最小值 ---
#     print("正在从训练集中计算每列的最大值和最小值...")
#     train_min = train_df.min()
#     train_max = train_df.max()

#     # 将计算出的最大最小值保存到一个DataFrame中
#     scalers_df = pd.DataFrame({'min_value': train_min, 'max_value': train_max})
    
#     # 打印出来方便查看
#     print("计算得到的Scaler参数如下：")
#     print(scalers_df)
    
#     # 保存Scaler参数到CSV文件
#     scalers_output_path = os.path.join(output_folder, scalers_filename)
#     scalers_df.to_csv(scalers_output_path, index=True) # index=True会把列名(uk_1等)作为第一列保存
#     print(f"\n✅ Scaler参数已保存至: '{scalers_filename}'")
#     print("-" * 30)

#     # --- 4. 使用学习到的Scaler归一化所有数据集 ---
#     print("正在使用Scaler参数归一化所有数据集...")
    
#     # 计算分母 (X_max - X_min)
#     data_range = train_max - train_min
    
#     # 处理分母为0的特殊情况（即某列在训练集中所有值都相同）
#     # 如果分母为0，除法会产生无穷大(inf)或非数字(NaN)，我们将其替换为0
#     data_range.replace(0, 1, inplace=True) # 将0替换为1，这样(X-X_min)/1=0，结果正确

#     # 应用归一化公式: X_scaled = (X - X_min) / (X_max - X_min)
#     train_normalized_df = (train_df - train_min) / data_range
#     validation_normalized_df = (validation_df - train_min) / data_range
#     test_normalized_df = (test_df - train_min) / data_range
#     print("归一化计算完成。")

#     # --- 5. 保存归一化后的三个数据集 ---
#     # 保存归一化后的训练集
#     train_norm_output_path = os.path.join(output_folder, train_norm_filename)
#     train_normalized_df.to_csv(train_norm_output_path, index=False)
#     print(f"✅ 归一化训练集已保存至: '{train_norm_filename}'")

#     # 保存归一化后的验证集
#     validation_norm_output_path = os.path.join(output_folder, validation_norm_filename)
#     validation_normalized_df.to_csv(validation_norm_output_path, index=False)
#     print(f"✅ -----------------验证集已保存至: '{validation_norm_filename}'")

#     # 保存归一化后的测试集
#     test_norm_output_path = os.path.join(output_folder, test_norm_filename)
#     test_normalized_df.to_csv(test_norm_output_path, index=False)
#     print(f"✅ -----------------测试集已保存至: '{test_norm_filename}'")
    
#     print("\n所有数据归一化处理并保存完毕！")

# except FileNotFoundError as e:
#     print(f"❌ 错误：找不到文件。")
#     print(f"请检查文件是否存在于指定路径: {e.filename}")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")

import pandas as pd
import os

# --- 1. 请在这里配置您的文件路径 ---
# 文件夹路径
input_folder = r'D:\SZU\Experiment\Experiment_Data\0921'
output_folder = r'D:\SZU\Experiment\Experiment_Data\0921'

# 输入文件名
input_filename = '0921_Wmin_Wmax_beta.xlsx'

# 输出文件名
output_filename_normalized = '0921_Wmin_Wmax_beta_normalized.xlsx'
output_filename_scalers = 'scalers_pandas.csv' # 新增：用于保存最大最小值的文件

# --- 准备工作 ---
input_file_path = os.path.join(input_folder, input_filename)
output_path_normalized = os.path.join(output_folder, output_filename_normalized)
output_path_scalers = os.path.join(output_folder, output_filename_scalers) # 新增

# 如果输出文件夹不存在，则自动创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"输出文件夹不存在，已自动创建: {output_folder}")

print(f"--- 开始使用 Pandas 对文件进行归一化: {input_filename} ---")

try:
    # --- 2. 读取Excel文件 ---
    df = pd.read_excel(input_file_path)
    print("文件读取成功，原始数据预览 (前5行):")
    print(df.head())
    print("-" * 50)

    # --- 3. 手动计算归一化 ---
    df_min = df.min()
    df_max = df.max()
    data_range = df_max - df_min
    data_range.replace(0, 1, inplace=True)
    normalized_df = (df - df_min) / data_range
    
    # --- 4.【新增功能】保存Scaler（最大值和最小值） ---
    # 将计算出的min和max值组合成一个DataFrame
    scalers_df = pd.DataFrame({'Min_Value': df_min, 'Max_Value': df_max})
    
    # 将参数保存到CSV文件
    # index=True 会将列名(TL, beta等)作为第一列保存下来
    scalers_df.to_csv(output_path_scalers, index=True, index_label='Feature')
    print("Scaler参数已计算并保存！预览:")
    print(scalers_df)
    print(f"\n✅ Scaler参数已保存至: {output_filename_scalers}")
    print("-" * 50)
    
    # --- 5. 保存归一化后的文件 ---
    normalized_df.to_excel(output_path_normalized, index=False)

    print("数据归一化处理完成！")
    print("归一化后数据预览 (前5行):")
    print(normalized_df.head())
    print(f"\n✅ 归一化数据已保存至: {output_filename_normalized}")


except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{input_file_path}'。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")


    
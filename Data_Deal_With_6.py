# import pandas as pd
# import os

# # --- 1. 请在这里配置您的文件和参数 ---

# # 定义输入和输出文件夹的路径
# input_folder = r'F:\实验数据\0824\扰动模态\0.08倍\处理后的数据'
# output_folder = r'F:\实验数据\0824\扰动模态\0.08倍\处理后的数据'

# # 定义输入文件名
# input_filename = '0824_Feature_D_0.08.csv'

# # 定义输出文件名
# output_filename = '0824_Feature_D_0.08_0.14s_to_0.34s.csv'

# # 【非常重要】请在这里填写您的CSV文件中代表“时间”的列名
# # 您的文件第一列的列名是什么，就填什么。例如 'Time', '时间(s)', 'timestamp' 等
# time_column_name = 'Time' 

# # 定义需要提取的时间范围 (单位：秒)
# start_time = 0.14
# end_time = 0.34

# # --- 准备工作 ---
# input_file_path = os.path.join(input_folder, input_filename)
# output_file_path = os.path.join(output_folder, output_filename)

# # 如果输出文件夹不存在，则自动创建
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"--- 开始处理文件: {input_filename} ---")

# try:
#     # --- 2. 读取完整的CSV文件 ---
#     print("正在读取源文件...")
#     df = pd.read_csv(input_file_path)
#     print(f"文件读取成功，共 {len(df)} 行数据。")

#     # --- 3. 根据时间范围筛选数据 ---
#     print(f"正在根据时间列 '{time_column_name}' 筛选数据，范围: {start_time}s 至 {end_time}s...")
    
#     # 这是实现筛选的核心逻辑
#     # (df[time_column_name] >= start_time) 会判断每一行的时间是否大于等于开始时间
#     # (df[time_column_name] <= end_time) 会判断每一行的时间是否小于等于结束时间
#     # & 符号表示两个条件必须同时满足
#     condition = (df[time_column_name] >= start_time) & (df[time_column_name] <= end_time)
    
#     # 将满足条件的行提取出来
#     extracted_df = df[condition]

#     # --- 4. 检查结果并保存 ---
#     if extracted_df.empty:
#         print(f"⚠️ 警告：在指定的时间范围 {start_time}s - {end_time}s 内没有找到任何数据。")
#     else:
#         print(f"成功提取到 {len(extracted_df)} 行数据。")
        
#         # 将提取出的数据保存到新的CSV文件，index=False表示不保存行索引
#         extracted_df.to_csv(output_file_path, index=False)
        
#         print("-" * 30)
#         print(f"✅ 处理完成！")
#         print(f"提取的数据已保存至: {output_filename}")

# except FileNotFoundError:
#     print(f"❌ 错误：找不到文件 '{input_file_path}'。请检查输入文件夹路径和文件名是否正确。")
# except KeyError:
#     print(f"❌ 错误：在文件中找不到名为 '{time_column_name}' 的时间列。")
#     print("👉 请检查第18行的 `time_column_name` 变量是否与您CSV文件中的实际列名完全匹配（大小写敏感）。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")


# import pandas as pd
# import os

# # --- 1. 请在这里配置您的文件路径 ---

# # 文件夹路径，应与上一步的输出文件夹相同
# input_folder = r'F:\实验数据\0824\处理后的数据'
# output_folder = r'F:\实验数据\0824\处理后的数据'

# # 需要读取的输入文件名 (即上一步生成的文件)
# input_filename = '0824_Feature_D_0.08_0.14s_to_0.34s.csv'

# # 处理后要保存的新文件名
# output_filename = '0824_Feature_D_5.csv'


# # --- 准备工作 ---
# input_file_path = os.path.join(input_folder, input_filename)
# output_file_path = os.path.join(output_folder, output_filename)

# # 如果输出文件夹不存在，则自动创建
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"--- 开始处理文件: {input_filename} ---")

# try:
#     # --- 2. 读取已提取的数据文件 ---
#     print("正在读取源文件...")
#     df = pd.read_csv(input_file_path)
#     print(f"文件读取成功，原始数据包含 {df.shape[0]} 行 和 {df.shape[1]} 列。")

#     # --- 3. 添加四列新的数据，并全部填充为0 ---
#     print("正在添加新的 A1, A2, A3, A4 列...")
    
#     # 直接为DataFrame分配新列，并将其值设置为0
#     # Pandas会自动将这个0值“广播”到所有行
#     df['A1'] = 1
#     df['A2'] = 0
#     df['A3'] = 1
#     df['A4'] = 0

#     print("新列添加成功！")
#     # 打印前5行数据以供预览
#     print("数据预览 (前5行):")
#     print(df.head())
    
#     # --- 4. 将修改后的数据保存到新文件 ---
#     df.to_csv(output_file_path, index=False)

#     print("-" * 30)
#     print(f"✅ 处理完成！")
#     print(f"最终数据包含 {df.shape[0]} 行 和 {df.shape[1]} 列。")
#     print(f"结果已保存至: {output_filename}")

# except FileNotFoundError:
#     print(f"❌ 错误：找不到文件 '{input_file_path}'。请检查输入文件夹路径和文件名是否正确。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")




# import pandas as pd
# import os

# # --- 1. 请在这里配置您的文件和参数 ---

# # 文件夹路径
# input_folder = r'F:\实验数据\0824\处理后的数据' 
# output_folder = r'F:\实验数据\0824\处理后的数据' 

# # ⚠️ 请在这里按【期望的合并顺序】列出您的6个CSV文件名
# # 这些文件应该是您上一步添加完A1-A4列后得到的文件
# file_names = [
#     '0824_Feature_N_1.csv',
#     '0824_Feature_R_1.csv',
#     '0824_Feature_R_2.csv',
#     '0824_Feature_R_3.csv',
#     '0824_Feature_R_4.csv',
#     '0824_Feature_R_5.csv',
#     '0824_Feature_R_6.csv',
#     '0824_Feature_D_1.csv',
#     '0824_Feature_D_2.csv',
#     '0824_Feature_D_3.csv',
#     '0824_Feature_D_4.csv',
#     '0824_Feature_D_5.csv'
# ]

# # 这是最终合并后要保存的文件名
# output_filename = 'feature_dataset.csv'

# # 这是最终文件要求的10个列名
# final_column_names = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'A1', 'A2', 'A3', 'A4']

# # --- 准备工作 ---
# output_file_path = os.path.join(output_folder, output_filename)
# list_of_processed_dfs = []

# # 如果输出文件夹不存在，则自动创建
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print("--- 开始批量提取、合并并重命名CSV文件 ---")

# try:
#     # --- 2. 循环处理文件列表中的每一个文件 ---
#     for filename in file_names:
#         file_path = os.path.join(input_folder, filename)
#         print(f"正在处理文件: {filename} ...")
        
#         # 定义需要提取的列的索引 (B列到K列)
#         # B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8, J=9, K=10,L=11,M=12
#         # list(range(1, 11)) 会自动生成列表 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
#         columns_to_extract = list(range(1, 13))

#         # 读取CSV文件，并使用 usecols 只选择我们需要的列
#         df = pd.read_csv(file_path, usecols=columns_to_extract)
        
#         # 将处理好的DataFrame添加到我们的列表中
#         list_of_processed_dfs.append(df)
    
#     # --- 3. 检查是否成功读取了任何文件 ---
#     if not list_of_processed_dfs:
#         print("⚠️ 警告：未能读取任何数据文件，请检查文件列表和输入文件夹路径。")
#     else:
#         # --- 4. 将列表中的所有数据（DataFrame）合并成一个 ---
#         print("\n所有文件处理完毕，正在合并...")
#         combined_df = pd.concat(list_of_processed_dfs, ignore_index=True)

#         # --- 5. 为合并后的DataFrame设置最终的列名 ---
#         combined_df.columns = final_column_names

#         # --- 6. 保存最终合并好的文件 ---
#         combined_df.to_csv(output_file_path, index=False)

#         print("-" * 30)
#         print(f"✅ 所有文件合并成功！")
#         print(f"共处理了 {len(list_of_processed_dfs)} 个文件。")
#         print(f"最终合并的数据总行数: {len(combined_df)}")
#         print(f"结果已保存到文件: {output_filename}")

# except FileNotFoundError as e:
#     print(f"❌ 错误：找不到文件。")
#     print(f"请检查文件是否存在于指定路径: {e.filename}")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")






import pandas as pd
import os

# --- 1. 请在这里配置您的文件路径 ---

# 文件夹路径
input_folder = r'F:\实验数据\SVM_MATLAB' # 上一步的输出文件夹
output_folder = r'F:\实验数据\SVM_MATLAB' # 存放最终拆分文件的文件夹

# ⚠️ 请在这里确认您要处理的输入文件名
input_filename = 'Formatted_Train_Data.xlsx'


# --- 准备工作 ---
input_file_path = os.path.join(input_folder, input_filename)

# 如果输出文件夹不存在，则自动创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"输出文件夹不存在，已自动创建: {output_folder}")

print(f"--- 开始处理并拆分文件: {input_filename} ---")

try:
    # --- 2. 一次性读取完整的Excel文件 ---
    # 使用 pd.read_excel 读取xlsx文件
    print("正在读取源Excel文件...")
    source_df = pd.read_excel(input_file_path)
    print(f"文件读取成功，共 {len(source_df)} 行, {len(source_df.columns)} 列。")
    print("-" * 30)

    # --- 3. 按照需求逐一创建和保存新的Excel文件 ---

    # 任务1: 创建 A1_Train.xlsx
    print("正在创建 A1_Train.xlsx ...")
    cols_to_extract_a1 = ['F1', 'F3', 'F7', 'F8', 'A1']
    df_a1 = source_df[cols_to_extract_a1]
    # 注意：因为我们选取的列名和最终要求的列名一致，所以不需要重命名
    output_path_a1 = os.path.join(output_folder, 'A1_Train.xlsx')
    df_a1.to_excel(output_path_a1, index=False)
    print(f"✅ A1_Train.xlsx 创建成功 ({len(df_a1.columns)} 列)。")

    # # 任务2: 创建 A2_Test.xlsx
    # print("正在创建 A2_Test.xlsx ...")
    # cols_to_extract_a2 = ['F2', 'F3', 'F7', 'A2']
    # df_a2 = source_df[cols_to_extract_a2]
    # output_path_a2 = os.path.join(output_folder, 'A2_Test.xlsx')
    # df_a2.to_excel(output_path_a2, index=False)
    # print(f"✅ A2_Test.xlsx 创建成功 ({len(df_a2.columns)} 列)。")

    # # 任务3: 创建 A3_Test.xlsx
    # print("正在创建 A3_Test.xlsx ...")
    # cols_to_extract_a3 = ['F2', 'F4', 'F8', 'A3']
    # df_a3 = source_df[cols_to_extract_a3]
    # output_path_a3 = os.path.join(output_folder, 'A3_Test.xlsx')
    # df_a3.to_excel(output_path_a3, index=False)
    # print(f"✅ A3_Test.xlsx 创建成功 ({len(df_a3.columns)} 列)。")

    # # 任务4: 创建 A4_Test.xlsx
    # print("正在创建 A4_Test.xlsx ...")
    # cols_to_extract_a4 = ['F5', 'F6', 'F7', 'A4']
    # df_a4 = source_df[cols_to_extract_a4]
    # output_path_a4 = os.path.join(output_folder, 'A4_Test.xlsx')
    # df_a4.to_excel(output_path_a4, index=False)
    # print(f"✅ A4_Test.xlsx 创建成功 ({len(df_a4.columns)} 列)。")

    print("-" * 30)
    print("所有文件拆分任务已全部完成！")

except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{input_file_path}'。请检查输入文件夹路径和文件名是否正确。")
except ImportError:
    print(f"❌ 错误：缺少 `openpyxl` 库。")
    print("👉 请在您的终端或命令行中运行 `pip install openpyxl` 来安装它。")
except KeyError as e:
    print(f"❌ 错误：在源文件中找不到指定的列名 {e}。")
    print("👉 请检查您的Excel文件是否包含脚本中需要提取的所有列名 (F1, F2, F3等)。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")



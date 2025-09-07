# import pandas as pd
# import os

# # --- 1. 请在这里配置您的基本信息 ---

# # ⚠️ 请将此路径修改为您存放24个文件夹的根目录
# # 例如，如果您的文件夹是 F:\实验数据\0905\Alpha\1, F:\实验数据\0905\Alpha\2, ...
# # 那么根目录就是 F:\实验数据\0905\Alpha
# base_folder = r'F:\实验数据\0905\Alpha'

# # 总共要处理的文件夹（组）数量
# num_groups = 7

# # 第1组中，第一个文件的起始编号 (例如 sdd_629.csv 中的 629)
# start_file_number = 719

# print(f"--- 开始批量处理 {num_groups} 组实验数据 ---")
# print(f"根目录: {base_folder}")
# print("-" * 50)

# # --- 2. 使用循环遍历每一个文件夹（组） ---
# for i in range(1, num_groups + 1):
    
#     current_folder_path = os.path.join(base_folder, str(i))
#     print(f"正在处理第 {i} 组，文件夹: {current_folder_path}")
    
#     # 检查文件夹是否存在
#     if not os.path.exists(current_folder_path):
#         print(f"  ❌ 警告：文件夹不存在，跳过第 {i} 组。")
#         print("-" * 50)
#         continue # 跳过本次循环，继续处理下一组

#     try:
#         # --- 3. 根据组号动态计算三个输入文件的编号 ---
#         # 公式：起始编号 + (组号 - 1) * 3
#         folder_start_num = start_file_number + (i - 1) * 3
        
#         # 定义输入和输出文件名
#         # 输入文件名
#         input_wm_filename = f'sdd_{folder_start_num}.csv'
#         input_te_filename = f'sdd_{folder_start_num + 1}.csv'
#         input_alpha_filename = f'sdd_{folder_start_num + 2}.csv'
        
#         # 输出文件名
#         output_wm_filename = f'0905_Wm_{i}.csv'
#         output_te_filename = f'0905_Te_{i}.csv'
#         output_alpha_filename = f'0905_Alpha_{i}.csv'

#         # --- 任务1: 处理 Wm 数据 (sdd_***) ---
#         input_path = os.path.join(current_folder_path, input_wm_filename)
#         output_path = os.path.join(current_folder_path, output_wm_filename)
        
#         df_wm = pd.read_csv(input_path, skiprows=28, header=None, usecols=[1, 2, 3])
#         df_wm.columns = ['Time', 'Wm', 'Wr']
#         df_wm.to_csv(output_path, index=False)
#         print(f"  ✅ {input_wm_filename} -> {output_wm_filename}")
        
#         # --- 任务2: 处理 Te 数据 (sdd_***+1) ---
#         input_path = os.path.join(current_folder_path, input_te_filename)
#         output_path = os.path.join(current_folder_path, output_te_filename)

#         df_te = pd.read_csv(input_path, skiprows=28, header=None, usecols=[1, 2, 3])
#         df_te.columns = ['Time', 'Te', 'Ts']
#         df_te.to_csv(output_path, index=False)
#         print(f"  ✅ {input_te_filename} -> {output_te_filename}")
        
#         # --- 任务3: 处理 Alpha 数据 (sdd_***+2) ---
#         input_path = os.path.join(current_folder_path, input_alpha_filename)
#         output_path = os.path.join(current_folder_path, output_alpha_filename)

#         df_alpha = pd.read_csv(input_path, skiprows=28, header=None, usecols=[1, 2])
        
#         # 【关键步骤】对提取出的第二列 (原始C列) 的所有数据乘以10
#         # df_alpha.iloc[:, 1] 表示选取所有行的第2列 (索引为1)
#         df_alpha.iloc[:, 1] = df_alpha.iloc[:, 1] * 10
        
#         df_alpha.columns = ['Time', 'Alpha']
#         df_alpha.to_csv(output_path, index=False)
#         print(f"  ✅ {input_alpha_filename} -> {output_alpha_filename} (C列已乘以10)")

#         print(f"--- 第 {i} 组处理完成 ---")
#         print("-" * 50)

#     except FileNotFoundError as e:
#         print(f"  ❌ 错误: 在第 {i} 组中找不到文件 {e.filename}。请检查文件名是否正确。跳过此组。")
#         print("-" * 50)
#     except Exception as e:
#         print(f"  ❌ 在处理第 {i} 组时发生未知错误: {e}。跳过此组。")
#         print("-" * 50)

# print("所有组别处理完毕！")


# import pandas as pd
# import os

# # --- 1. 请在这里配置您的文件和参数 ---

# # 定义输入和输出文件夹的路径
# input_folder = r'F:\实验数据\0905\Alpha\5' # 存放源文件的文件夹
# output_folder = r'F:\实验数据\0905\Alpha\5' # 存放结果的文件夹

# # 定义输入文件名
# input_filename = '0905_Alpha_5.csv' # ⚠️ 请替换为您的文件名

# # 定义输出文件名
# output_filename = '0905_Alpha.csv'

# # 【非常重要】请在这里填写您的CSV文件中代表“时间”和“B列数据”的实际列名
# time_column_name = 'Time' 
# data_column_name_original = 'Alpha' 

# # 定义需要提取的时间范围 (单位：秒)
# start_time = 11.0
# end_time = 15.0

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
#     source_df = pd.read_csv(input_file_path)
#     print(f"文件读取成功，共 {len(source_df)} 行数据。")

#     # --- 3. 根据时间范围筛选数据 ---
#     print(f"正在根据时间列 '{time_column_name}' 筛选数据，范围: {start_time}s 至 {end_time}s...")
#     condition = (source_df[time_column_name] >= start_time) & (source_df[time_column_name] <= end_time)
    
#     # 使用.copy()可以避免后续操作中出现不必要的警告
#     time_slice_df = source_df[condition].copy()

#     # --- 4. 检查结果并进行处理 ---
#     if time_slice_df.empty:
#         print(f"⚠️ 警告：在指定的时间范围 {start_time}s - {end_time}s 内没有找到任何数据。")
#     else:
#         print(f"成功提取到 {len(time_slice_df)} 行数据。")
        
#         # --- 5. 创建新的DataFrame并重置时间 ---
#         print("正在重置时间序列起点为 0 ...")
        
#         # 创建一个新的DataFrame，包含两列：
#         # - 'Time': 将提取出的时间列整体减去起始时间 start_time (10.0)
#         # - 'Wm': 直接使用提取出的原始B列数据
#         final_df = pd.DataFrame({
#             'Time': time_slice_df[time_column_name] - start_time,
#             'Wm': time_slice_df[data_column_name_original]
#         })
        
#         # 可选：为了避免浮点数精度问题，可以将时间列进行四舍五入
#         # 如果采样周期是0.001s，保留3位小数是合适的
#         final_df['Time'] = final_df['Time'].round(decimals=3)

#         # --- 6. 将处理好的数据保存到新文件 ---
#         final_df.to_csv(output_file_path, index=False)
        
#         print("-" * 30)
#         print(f"✅ 处理完成！")
#         print("数据预览 (前5行):")
#         print(final_df.head())
#         print("\n数据预览 (后5行):")
#         print(final_df.tail())
#         print(f"\n结果已保存至: {output_filename}")


# except FileNotFoundError:
#     print(f"❌ 错误：找不到文件 '{input_file_path}'。请检查输入文件夹路径和文件名是否正确。")
# except KeyError as e:
#     print(f"❌ 错误：在文件中找不到指定的列名 {e}。")
#     print(f"👉 请检查第18行的 `time_column_name` ('{time_column_name}') 和第19行的 `data_column_name_original` ('{data_column_name_original}') 变量是否与您CSV文件中的实际列名完全匹配。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")


# import pandas as pd
# import os

# # --- 1. 请在这里配置您的文件路径 ---

# # ⚠️ 请将 'F:\实验数据\0831\1' 替换为存放您3个CSV文件的实际文件夹路径
# data_folder = r'F:\实验数据\0905\负载-转速数据\0.06'

# print(f"--- 开始处理文件夹中的数据: {data_folder} ---")
# print("-" * 50)

# try:
#     # --- 任务1: 处理 sdd_741.csv ---
#     print("正在处理文件: sdd_744.csv ...")
#     input_path_1 = os.path.join(data_folder, 'sdd_744.csv')
#     output_path_1 = os.path.join(data_folder, '0906_Wm_0.06.csv') # 根据今天日期建议命名

#     # 读取数据：跳过前28行，无表头，只取B,C,D列
#     df1 = pd.read_csv(
#         input_path_1,
#         skiprows=28,
#         header=None,
#         usecols=[1, 2, 3]  # B, C, D列的索引是 1, 2, 3
#     )
    
#     # 重命名列
#     df1.columns = ['Time', 'Wm', 'Wr']
    
#     # 保存新文件
#     df1.to_csv(output_path_1, index=False)
#     print(f"✅ 'sdd_744.csv' 处理完成，结果已保存至 '0906_Wm_0.06.csv'")
#     print("-" * 50)

#     # --- 任务2: 处理 sdd_745.csv ---
#     print("正在处理文件: sdd_745.csv ...")
#     input_path_2 = os.path.join(data_folder, 'sdd_745.csv')
#     output_path_2 = os.path.join(data_folder, '0906_Te_0.06.csv')

#     # 读取数据：跳过前28行，无表头，只取B,C,D列
#     df2 = pd.read_csv(
#         input_path_2,
#         skiprows=28,
#         header=None,
#         usecols=[1, 2, 3]  # B, C, D列
#     )

#     # 重命名列
#     df2.columns = ['Time', 'Te', 'Ts']

#     # 保存新文件
#     df2.to_csv(output_path_2, index=False)
#     print(f"✅ 'sdd_745.csv' 处理完成，结果已保存至 '0906_Te_0.06.csv'")
#     print("-" * 50)

#     # --- 任务3: 处理 sdd_743.csv ---
#     print("正在处理文件: sdd_743.csv ...")
#     input_path_3 = os.path.join(data_folder, 'sdd_743.csv')
#     output_path_3 = os.path.join(data_folder, '0906_TL_0.05.csv')

#     # 读取数据：跳过前28行，无表头，只取B,C,D列
#     df3 = pd.read_csv(
#         input_path_3,
#         skiprows=28,
#         header=None,
#         usecols=[1, 2, 3]  # B, C, D列
#     )

#     # 重命名列
#     df3.columns = ['Time', 'TL', 'TL^']

#     # 保存新文件
#     df3.to_csv(output_path_3, index=False)
#     print(f"✅ 'sdd_743.csv' 处理完成，结果已保存至 '0906_TL_0.05.csv'")
#     print("-" * 50)
    
#     print("所有文件处理任务已全部完成！")

# except FileNotFoundError as e:
#     print(f"❌ 错误：找不到文件。")
#     print(f"请检查文件 '{os.path.basename(e.filename)}' 是否存在于您指定的文件夹中。")
#     print(f"请确认您的文件夹路径 '{data_folder}' 设置正确。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")

# import pandas as pd
# import os

# data_folder = r'F:\实验数据\0905\负载-转速数据\0.05'


# processing_tasks = [
#     {
#         'input_filename': 'sdd_741.csv',
#         'output_filename': '0906_Wm_0.05.csv',
#         'columns_to_use': [1, 2, 3],  # B, C, D
#         'new_column_names': ['Time', 'Wm', 'Wr']
#     },
#     {
#         'input_filename': 'sdd_742.csv',
#         'output_filename': '0906_Te_0.05.csv',
#         'columns_to_use': [1, 2, 3],  # B, C, D
#         'new_column_names': ['Time', 'Te', 'Ts']
#     },
#     {
#         'input_filename': 'sdd_743.csv',
#         'output_filename': '0906_TL_0.05.csv',
#         'columns_to_use': [1, 2, 3],  # B, C, D
#         'new_column_names': ['Time', 'TL', 'TL^']
#     }
# ]


# print(f"--- 开始处理文件夹中的数据: {data_folder} ---")
# print("-" * 50)

# # 使用循环遍历任务列表中的每一个任务
# for task in processing_tasks:
#     # 从任务字典中获取所有配置信息
#     input_file = task['input_filename']
#     output_file = task['output_filename']
#     cols_to_use = task['columns_to_use']
#     new_cols = task['new_column_names']
    
#     print(f"正在处理: {input_file} -> {output_file} ...")
    
#     try:
#         # 组合完整的文件路径
#         input_path = os.path.join(data_folder, input_file)
#         output_path = os.path.join(data_folder, output_file)

#         # 读取数据：跳过前28行，无表头，只取指定列
#         df = pd.read_csv(
#             input_path,
#             skiprows=28,
#             header=None,
#             usecols=cols_to_use
#         )

#         # 重命名列
#         df.columns = new_cols

#         # 保存新文件
#         df.to_csv(output_path, index=False)
#         print(f"  ✅ 处理成功！")

#     except FileNotFoundError:
#         print(f"  ❌ 错误：找不到文件 '{input_file}'。请检查文件名是否正确。")
#     except Exception as e:
#         print(f"  ❌ 处理过程中发生未知错误: {e}")
    
#     print("-" * 50)

# print("所有文件处理任务已全部完成！")


import pandas as pd
import os

# --- 1. 请在这里配置您的文件和参数 ---

# ⚠️ 请将此路径修改为您存放CSV文件的实际文件夹路径
data_folder = r'F:\实验数据\0905\负载-转速数据\0.19'

# 定义输入文件名
wm_input_filename = '0906_Wm_0.19.csv'
tl_input_filename = '0906_TL_0.19.csv'

# 定义输出文件名
wm_output_filename = 'Wm_0906_0.19.csv'
tl_output_filename = 'TL_0906_0.19.csv'

# 定义搜索的起始时间 (单位：秒)
start_time = 9.994

# --- 准备工作 ---
wm_input_path = os.path.join(data_folder, wm_input_filename)
tl_input_path = os.path.join(data_folder, tl_input_filename)
wm_output_path = os.path.join(data_folder, wm_output_filename)
tl_output_path = os.path.join(data_folder, tl_output_filename)

print(f"--- 开始动态数据提取任务 ---")
print(f"数据文件夹: {data_folder}")
print("-" * 50)

try:
    # --- 2. 读取两个源文件 ---
    print(f"正在读取文件: {wm_input_filename}")
    wm_df = pd.read_csv(wm_input_path)
    
    print(f"正在读取文件: {tl_input_filename}")
    tl_df = pd.read_csv(tl_input_path)
    print("文件读取成功！")
    print("-" * 50)

    # --- 3. 核心步骤: 从Wm文件中确定动态的结束时间 ---
    print(f"步骤1: 在 '{wm_input_filename}' 中搜索 {start_time}s 之后的Wm最小值...")
    
    # 筛选出所有时间大于等于起始时间的数据
    search_range_df = wm_df[wm_df['Time'] >= start_time]
    
    if search_range_df.empty:
        print(f"  ❌ 错误：在 {start_time}s 之后没有找到任何数据，无法继续。")
    else:
        # 使用 .idxmin() 找到Wm列最小值的索引
        min_wm_index = search_range_df['Wm'].idxmin()
        
        # 使用该索引从原始DataFrame中获取对应的Wm值和时间
        min_wm_value = wm_df.loc[min_wm_index, 'Wm']
        end_time_dynamic = wm_df.loc[min_wm_index, 'Time']
        
        print(f"  ✅ 搜索完成：Wm的最小值为 {min_wm_value:.4f}，出现在 {end_time_dynamic}s。")
        print(f"  => 确定的数据提取时间范围为: {start_time}s 至 {end_time_dynamic}s")
        print("-" * 50)

        # --- 4. 使用确定的时间范围处理两个文件 ---
        
        # 任务1: 处理 Wm 文件
        print(f"步骤2: 正在截取 '{wm_input_filename}'...")
        wm_condition = (wm_df['Time'] >= start_time) & (wm_df['Time'] <= end_time_dynamic)
        wm_slice_df = wm_df.loc[wm_condition, ['Time', 'Wm']]
        wm_slice_df.to_csv(wm_output_path, index=False)
        print(f"  ✅ 成功截取 {len(wm_slice_df)} 行数据并保存至 '{wm_output_filename}'")

        # 任务2: 处理 TL 文件
        print(f"步骤3: 正在截取 '{tl_input_filename}'...")
        tl_condition = (tl_df['Time'] >= start_time) & (tl_df['Time'] <= end_time_dynamic)
        tl_slice_df = tl_df.loc[tl_condition, ['Time', 'TL1', 'TL2']]
        tl_slice_df.to_csv(tl_output_path, index=False)
        print(f"  ✅ 成功截取 {len(tl_slice_df)} 行数据并保存至 '{tl_output_filename}'")
        
        print("-" * 50)
        print("所有任务处理完毕！")

except FileNotFoundError as e:
    print(f"❌ 错误：找不到文件。")
    print(f"请检查文件 '{os.path.basename(e.filename)}' 是否存在于您指定的文件夹中。")
except KeyError as e:
    print(f"❌ 错误：在文件中找不到指定的列名 {e}。")
    print("👉 请检查您的CSV文件是否包含脚本中需要的所有列名 (例如 'Time', 'Wm', 'TL1', 'TL2')。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")



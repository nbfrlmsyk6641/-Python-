# import pandas as pd
# import os # 导入os模块，用于处理文件和目录

# # --- 1. 配置输入和输出文件路径 ---
# # ⚠️ 请在这里修改你的输入文件夹和文件名
# input_folder = r'F:\实验数据\0824\扰动模态\0.09倍'
# input_filename = 'sdd_588.csv'

# # ⚠️ 请在这里修改你希望保存结果的文件夹
# output_folder = r'F:\实验数据\0824\扰动模态\0.09倍\处理后的数据'
# output_filename = '0824_wm_D_0.09.csv'


# input_file_path = os.path.join(input_folder, input_filename)
# output_file_path = os.path.join(output_folder, output_filename)

# # --- 新增功能：自动创建输出文件夹 ---
# # 如果指定的输出文件夹不存在，代码会自动为你创建它
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"准备处理文件: {input_file_path}")
# print(f"处理结果将保存至: {output_file_path}")
# print("-" * 30)

# try:
#     # --- 2. 读取并处理数据 ---
#     df = pd.read_csv(
#         input_file_path,
#         skiprows=28,
#         header=None,
#         usecols=[1, 2, 3]
#     )

#     # --- 3. 重命名列名 ---
#     df.columns = ['Time', 'Wm', 'Wr']

#     # --- 4. 保存到新的CSV文件 ---
#     df.to_csv(output_file_path, index=False)

#     print("-" * 30)
#     print(f"✅ 处理成功！结果已保存。")

# except FileNotFoundError:
#     print(f"❌ 错误：找不到文件 '{input_file_path}'。")
#     print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")


# input_folder = r'F:\实验数据\0824\扰动模态\0.09倍'
# input_filename = 'sdd_589.csv'

# # ⚠️ 请在这里修改你希望保存结果的文件夹
# output_folder = r'F:\实验数据\0824\扰动模态\0.09倍\处理后的数据'
# output_filename = '0824_Te_Ts_D_0.09.csv'


# input_file_path = os.path.join(input_folder, input_filename)
# output_file_path = os.path.join(output_folder, output_filename)

# # --- 新增功能：自动创建输出文件夹 ---
# # 如果指定的输出文件夹不存在，代码会自动为你创建它
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"准备处理文件: {input_file_path}")
# print(f"处理结果将保存至: {output_file_path}")
# print("-" * 30)

# try:
#     # --- 2. 读取并处理数据 ---
#     df = pd.read_csv(
#         input_file_path,
#         skiprows=28,
#         header=None,
#         usecols=[1, 2, 3]
#     )

#     # --- 3. 重命名列名 ---
#     df.columns = ['Time', 'Te', 'Ts']

#     # --- 4. 保存到新的CSV文件 ---
#     df.to_csv(output_file_path, index=False)

#     print("-" * 30)
#     print(f"✅ 处理成功！结果已保存。")

# except FileNotFoundError:
#     print(f"❌ 错误：找不到文件 '{input_file_path}'。")
#     print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")


# input_folder = r'F:\实验数据\0824\扰动模态\0.09倍'
# input_filename = 'sdd_590.csv'

# # ⚠️ 请在这里修改你希望保存结果的文件夹
# output_folder = r'F:\实验数据\0824\扰动模态\0.09倍\处理后的数据'
# output_filename = '0824_ISE_D_0.09.csv'


# input_file_path = os.path.join(input_folder, input_filename)
# output_file_path = os.path.join(output_folder, output_filename)

# # --- 新增功能：自动创建输出文件夹 ---
# # 如果指定的输出文件夹不存在，代码会自动为你创建它
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"准备处理文件: {input_file_path}")
# print(f"处理结果将保存至: {output_file_path}")
# print("-" * 30)

# try:
#     # --- 2. 读取并处理数据 ---
#     df = pd.read_csv(
#         input_file_path,
#         skiprows=28,
#         header=None,
#         usecols=[1, 2]
#     )

#     # --- 3. 重命名列名 ---
#     df.columns = ['Time', 'ISE']

#     # --- 4. 保存到新的CSV文件 ---
#     df.to_csv(output_file_path, index=False)

#     print("-" * 30)
#     print(f"✅ 处理成功！结果已保存。")

# except FileNotFoundError:
#     print(f"❌ 错误：找不到文件 '{input_file_path}'。")
#     print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")


# input_folder = r'F:\实验数据\0824\扰动模态\0.09倍'
# input_filename = 'sdd_591.csv'

# # ⚠️ 请在这里修改你希望保存结果的文件夹
# output_folder = r'F:\实验数据\0824\扰动模态\0.09倍\处理后的数据'
# output_filename = '0824_Feature_D_0.09.csv'

# # 使用 os.path.join() 来智能地合并路径，这是最推荐的做法
# # 它会自动处理Windows(\)和Mac/Linux(/)下不同的路径分隔符
# input_file_path = os.path.join(input_folder, input_filename)
# output_file_path = os.path.join(output_folder, output_filename)

# # --- 新增功能：自动创建输出文件夹 ---
# # 如果指定的输出文件夹不存在，代码会自动为你创建它
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"准备处理文件: {input_file_path}")
# print(f"处理结果将保存至: {output_file_path}")
# print("-" * 30)

# try:
#     # --- 2. 读取并处理数据 ---
#     df = pd.read_csv(
#         input_file_path,
#         skiprows=28,
#         header=None,
#         usecols=[1, 2, 3, 4, 5, 6, 7]
#     )

#     # --- 3. 重命名列名 ---
#     df.columns = ['Time', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6']

#     # --- 4. 保存到新的CSV文件 ---
#     df.to_csv(output_file_path, index=False)

#     print("-" * 30)
#     print(f"✅ 处理成功！结果已保存。")

# except FileNotFoundError:
#     print(f"❌ 错误：找不到文件 '{input_file_path}'。")
#     print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")


# input_folder = r'F:\实验数据\0824\扰动模态\0.09倍'
# input_filename = 'sdd_592.csv'

# # ⚠️ 请在这里修改你希望保存结果的文件夹
# output_folder = r'F:\实验数据\0824\扰动模态\0.09倍\处理后的数据'
# output_filename = '0824_TL_D_0.09.csv'


# input_file_path = os.path.join(input_folder, input_filename)
# output_file_path = os.path.join(output_folder, output_filename)

# # --- 新增功能：自动创建输出文件夹 ---
# # 如果指定的输出文件夹不存在，代码会自动为你创建它
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"准备处理文件: {input_file_path}")
# print(f"处理结果将保存至: {output_file_path}")
# print("-" * 30)

# try:
#     # --- 2. 读取并处理数据 ---
#     df = pd.read_csv(
#         input_file_path,
#         skiprows=28,
#         header=None,
#         usecols=[1, 2, 3]
#     )

#     # --- 3. 重命名列名 ---
#     df.columns = ['Time', 'TL', 'TL_real']

#     # --- 4. 保存到新的CSV文件 ---
#     df.to_csv(output_file_path, index=False)

#     print("-" * 30)
#     print(f"✅ 处理成功！结果已保存。")

# except FileNotFoundError:
#     print(f"❌ 错误：找不到文件 '{input_file_path}'。")
#     print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")

import pandas as pd
import os

# --- 1. 请在这里配置您的文件路径 ---

# ⚠️ 请将 'C:\Users\YourName\Desktop\新实验数据' 替换为存放您3个CSV文件的实际文件夹路径
data_folder = r'F:\实验数据\0831\3'

print(f"--- 开始处理文件夹中的数据: {data_folder} ---")
print("-" * 40)

try:
    # --- 任务1: 处理 sdd_632.csv ---
    print("正在处理文件: sdd_632.csv ...")
    input_path_1 = os.path.join(data_folder, 'sdd_632.csv')
    output_path_1 = os.path.join(data_folder, '0831_Wm_2.csv')

    # 读取数据：跳过前28行，无表头，只取B,C,D列
    df1 = pd.read_csv(
        input_path_1,
        skiprows=28,
        header=None,
        usecols=[1, 2, 3]  # B, C, D列的索引是 1, 2, 3
    )
    
    # 重命名列
    df1.columns = ['Time', 'Wm', 'Wr']
    
    # 保存新文件
    df1.to_csv(output_path_1, index=False)
    print(f"✅ 'sdd_633.csv' 处理完成，结果已保存至 '0831_Wm_2.csv'")
    print("-" * 40)

    # --- 任务2: 处理 sdd_633.csv ---
    print("正在处理文件: sdd_633.csv ...")
    input_path_2 = os.path.join(data_folder, 'sdd_633.csv')
    output_path_2 = os.path.join(data_folder, '0831_Te_2.csv')

    # 读取数据：跳过前28行，无表头，只取B,C,D列
    df2 = pd.read_csv(
        input_path_2,
        skiprows=28,
        header=None,
        usecols=[1, 2, 3]  # B, C, D列
    )

    # 重命名列
    df2.columns = ['Time', 'Te', 'Ts']

    # 保存新文件
    df2.to_csv(output_path_2, index=False)
    print(f"✅ 'sdd_633.csv' 处理完成，结果已保存至 '0831_Te_2.csv'")
    print("-" * 40)

    # --- 任务3: 处理 sdd_634.csv ---
    print("正在处理文件: sdd_634.csv ...")
    input_path_3 = os.path.join(data_folder, 'sdd_634.csv')
    output_path_3 = os.path.join(data_folder, '0831_Alpha_2.csv')

    # 读取数据：跳过前28行，无表头，只取B,C列
    df3 = pd.read_csv(
        input_path_3,
        skiprows=28,
        header=None,
        usecols=[1, 2]  # B, C列的索引是 1, 2
    )

    # 重命名列
    df3.columns = ['Time', 'Alpha']

    # 保存新文件
    df3.to_csv(output_path_3, index=False)
    print(f"✅ 'sdd_634.csv' 处理完成，结果已保存至 '0831_Alpha_2.csv'")
    print("-" * 40)
    
    print("所有文件处理任务已全部完成！")

except FileNotFoundError as e:
    print(f"❌ 错误：找不到文件。")
    print(f"请检查文件 '{e.filename}' 是否存在于您指定的文件夹中。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")



# import pandas as pd
# import os

# # --- 1. 请在这里配置您的文件和参数 ---

# # 定义输入和输出文件夹的路径
# input_folder = r'F:\实验数据\0830\6' 
# output_folder = r'F:\实验数据\0830\6' 

# # 定义输入文件名 
# input_filename = '0830_Alpha_6.csv'

# # 定义输出文件名
# output_filename = 'Alpha_9s_to_11s.csv'

# time_column_name_original = 'Time' 
# data_column_name_original = 'Alpha'  

# # 定义需要提取的时间范围 (单位：秒)
# start_time = 9.0
# end_time = 11.0

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
#     print(f"正在根据时间列 '{time_column_name_original}' 筛选数据，范围: {start_time}s 至 {end_time}s...")
#     condition = (source_df[time_column_name_original] >= start_time) & (source_df[time_column_name_original] <= end_time)
    
#     # 使用.copy()可以避免后续操作中出现SettingWithCopyWarning
#     time_slice_df = source_df[condition].copy()

#     # --- 4. 检查结果并进行处理 ---
#     if time_slice_df.empty:
#         print(f"⚠️ 警告：在指定的时间范围 {start_time}s - {end_time}s 内没有找到任何数据。")
#     else:
#         print(f"成功提取到 {len(time_slice_df)} 行数据。")
        
#         # --- 5. 创建新的DataFrame并重置时间 ---
#         print("正在重置时间序列起点为 0 ...")
        
#         # 创建一个新的DataFrame，包含两列
#         # 第一列 'Time': 将提取出的时间列整体减去起始时间
#         # 第二列 'Te': 直接使用提取出的原始数据列
#         final_df = pd.DataFrame({
#             'Time': time_slice_df[time_column_name_original] - start_time,
#             'Alpha': time_slice_df[data_column_name_original]
#         })
        
#         # 可选：为了避免浮点数精度问题，可以将时间列四舍五入到毫秒
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
#     print("👉 请检查第17、18行的 `time_column_name_original` 和 `data_column_name_original` 变量是否与您CSV文件中的实际列名完全匹配。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")

# import pandas as pd
# import os

# # --- 1. 请在这里配置您的文件和参数 ---

# # 定义输入和输出文件夹的路径
# input_folder = r'F:\实验数据\0830\6' 
# output_folder = r'F:\实验数据\0830\6' 

# # 定义输入文件名
# input_filename = '0830_Te_6.csv' # ⚠️ 请替换为您的文件名

# # 定义输出文件名
# output_filename = 'Te_9.5s_to_11s.csv'

# # 【非常重要】请在这里填写您的CSV文件中代表“时间”和“数据”的实际列名
# time_column_name_original = 'Time' 
# data_column_name_original = 'Te' # ⚠️ 请替换为您的B列数据对应的列名

# # 定义需要提取的原始时间范围 (单位：秒)
# start_time_original = 9.5
# end_time_original = 11.0

# # 定义新的时间序列的起始点 (单位：秒)
# start_time_new = 0.5

# # 定义新文件中数据列的名称
# new_data_column_name = 'Te' 

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

#     # --- 3. 根据原始时间范围筛选数据 ---
#     print(f"正在根据时间列 '{time_column_name_original}' 筛选数据，范围: {start_time_original}s 至 {end_time_original}s...")
#     condition = (source_df[time_column_name_original] >= start_time_original) & (source_df[time_column_name_original] <= end_time_original)
#     time_slice_df = source_df[condition].copy()

#     # --- 4. 检查结果并进行处理 ---
#     if time_slice_df.empty:
#         print(f"⚠️ 警告：在指定的时间范围 {start_time_original}s - {end_time_original}s 内没有找到任何数据。")
#     else:
#         print(f"成功提取到 {len(time_slice_df)} 行数据。")
        
#         # --- 5. 创建新的DataFrame并平移时间轴 ---
#         print(f"正在平移时间序列，使其起点为 {start_time_new}s ...")

#         # 计算时间平移的偏移量
#         # 公式: NewTime = OldTime - OldStartTime + NewStartTime
#         # 整理后: NewTime = OldTime - (OldStartTime - NewStartTime)
#         time_offset = start_time_original - start_time_new
        
#         # 创建新的DataFrame
#         final_df = pd.DataFrame({
#             'Time': time_slice_df[time_column_name_original] - time_offset,
#             new_data_column_name: time_slice_df[data_column_name_original]
#         })
        
#         # 可选：为了避免浮点数精度问题，可以将时间列四舍五入到毫秒
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
#     print("👉 请检查第18、19行的 `time_column_name_original` 和 `data_column_name_original` 变量是否与您CSV文件中的实际列名完全匹配。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")

# import pandas as pd
# import os

# # --- 1. 请在这里配置您的文件和参数 ---

# # 存放您两个源文件的文件夹
# input_folder = r'F:\实验数据\0830\6'
# # 存放最终合并结果的文件夹
# output_folder = r'F:\实验数据\0830\6'

# # 第一个文件应该是包含 0s-0.499s 数据的文件
# # 第二个文件应该是包含 0.5s-1.999s 数据的文件
# files_to_combine = [
#     'Te_6.306s_to_6.806s.csv', 
#     'Te_9.5s_to_11s.csv'     
# ]

# # 这是最终合并后要保存的文件名
# output_filename = 'Te_Alpha_6.csv'

# # 这是最终文件要求的列名
# final_column_names = ['Time', 'Te']


# # --- 准备工作 ---
# output_file_path = os.path.join(output_folder, output_filename)
# list_of_dfs = []

# # 如果输出文件夹不存在，则自动创建
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print("--- 开始合并两个CSV文件 ---")

# try:
#     # --- 2. 循环读取并处理文件列表中的文件 ---
#     for filename in files_to_combine:
#         file_path = os.path.join(input_folder, filename)
#         print(f"正在读取文件: {filename} ...")
        
#         # 读取CSV文件
#         df = pd.read_csv(file_path)
        
#         # 【关键步骤】在合并前，统一所有文件的列名
#         # 这样做可以确保，即使第二个文件的列名是'Time', 'Data'，也能正确合并
#         df.columns = final_column_names
        
#         # 将处理好的DataFrame添加到我们的列表中
#         list_of_dfs.append(df)
    
#     # --- 3. 将列表中的两个DataFrame合并成一个 ---
#     if len(list_of_dfs) == 2:
#         print("\n两个文件读取完毕，正在合并...")
#         # pd.concat 会将列表中的DataFrame按顺序垂直堆叠
#         # ignore_index=True 会创建一个新的、连续的行索引 (0, 1, 2, ... 1999)
#         combined_df = pd.concat(list_of_dfs, ignore_index=True)

#         # --- 4. 保存最终合并好的文件 ---
#         combined_df.to_csv(output_file_path, index=False)

#         print("-" * 30)
#         print(f"✅ 文件合并成功！")
#         print(f"总数据行数: {len(combined_df)}") # 500 + 1500 = 2000
#         print(f"时间范围: {combined_df['Time'].min()}s 至 {combined_df['Time'].max()}s")
#         print(f"结果已保存到文件: {output_filename}")
#     else:
#         print("⚠️ 警告：未能成功读取两个文件，合并中止。")


# except FileNotFoundError as e:
#     print(f"❌ 错误：找不到文件。")
#     print(f"请检查文件是否存在于指定路径: {e.filename}")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")






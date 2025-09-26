# 提取文件
import pandas as pd
import os

data_folder = r'D:\SZU\Experiment\Experiment_Data\0921\BigJ_WT_0921\0921_1'

processing_tasks = [
    {
        'input_filename': 'sdd_1010.csv',
        'output_filename': '0921_Wm_1.csv',
        'columns_to_use': [1, 2, 3],  # B, C, D
        'new_column_names': ['Time', 'Wm', 'Wr']
    },
    {
        'input_filename': 'sdd_1011.csv',
        'output_filename': '0921_Te_1.csv',
        'columns_to_use': [1, 2],  # B, C, D
        'new_column_names': ['Time', 'Te']
    },
    {
        'input_filename': 'sdd_1012.csv',
        'output_filename': '0921_AB_1.csv',
        'columns_to_use': [1, 2, 3],  # B, C, D
        'new_column_names': ['Time', 'alpha', 'beta']
    }
]


print(f"--- 开始处理文件夹中的数据: {data_folder} ---")
print("-" * 50)

for task in processing_tasks:
    # 从任务字典中获取所有配置信息
    input_file = task['input_filename']
    output_file = task['output_filename']
    cols_to_use = task['columns_to_use']
    new_cols = task['new_column_names']
    
    print(f"正在处理: {input_file} -> {output_file} ...")
    
    try:
        # 组合完整的文件路径
        input_path = os.path.join(data_folder, input_file)
        output_path = os.path.join(data_folder, output_file)

        # 读取数据：跳过前28行，无表头，只取指定列
        df = pd.read_csv(
            input_path,
            skiprows=28,
            header=None,
            usecols=cols_to_use
        )

        # 重命名列
        df.columns = new_cols

        # 保存新文件
        df.to_csv(output_path, index=False)
        print(f"  ✅ 处理成功！")

    except FileNotFoundError:
        print(f"  ❌ 错误：找不到文件 '{input_file}'。请检查文件名是否正确。")
    except Exception as e:
        print(f"  ❌ 处理过程中发生未知错误: {e}")
    
    print("-" * 50)

print("所有文件处理任务已全部完成！")



# # 提取时间段
# import pandas as pd
# import os


# data_folder = r'D:\SZU\Experiment\Experiment_Data\0920\0920_10'

# output_folder = r'D:\SZU\Experiment\Experiment_Data\0920\0920_10' 

# start_time = 16.6524
# end_time = 21.6524

# processing_tasks = [
#     {
#         'input_filename': '0920_Wm_10.csv',
#         'output_filename': '0920_Wm_10_5s.csv'
#     },
#     {
#         'input_filename': '0920_Te_10.csv',
#         'output_filename': '0920_Te_10_5s.csv'
#     },
#     {
#         'input_filename': '0920_AB_10.csv',
#         'output_filename': '0920_AB_10_5s.csv'
#     }
# ]


# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"--- 开始批量处理文件，提取时间范围: {start_time}s - {end_time}s ---")
# print("-" * 50)

# for task in processing_tasks:
#     input_file = task['input_filename']
#     output_file = task['output_filename']
    
#     print(f"正在处理: {input_file} ...")
    
#     try:
#         # 组合完整的文件路径
#         input_path = os.path.join(data_folder, input_file)
#         output_path = os.path.join(output_folder, output_file)

#         # 读取源文件
#         df = pd.read_csv(input_path)

#         # 根据时间范围筛选数据
#         condition = (df['Time'] >= start_time) & (df['Time'] <= end_time)
#         time_slice_df = df[condition].copy() # 使用.copy()避免后续操作出现警告

#         # 检查是否提取到了数据
#         if time_slice_df.empty:
#             print(f"  ⚠️ 警告：在指定时间范围内没有找到数据，已跳过文件 '{input_file}'。")
#             print("-" * 50)
#             continue # 继续处理下一个文件

#         # 【关键步骤】重置时间列，使其从0开始
#         time_slice_df['Time'] = time_slice_df['Time'] - start_time
        
#         # 可选：为了避免浮点数精度问题，对时间列进行四舍五入
#         time_slice_df['Time'] = time_slice_df['Time'].round(decimals=3)

#         # 保存处理后的文件，列名将保持不变
#         time_slice_df.to_csv(output_path, index=False)
#         print(f"  ✅ 处理成功！提取了 {len(time_slice_df)} 行数据，已保存至 '{output_file}'")

#     except FileNotFoundError:
#         print(f"  ❌ 错误：找不到文件 '{input_file}'。请检查文件名和路径是否正确。")
#     except KeyError:
#         print(f"  ❌ 错误：在文件 '{input_file}' 中找不到名为 'Time' 的列。请检查文件内容。")
#     except Exception as e:
#         print(f"  ❌ 处理过程中发生未知错误: {e}")
    
#     print("-" * 50)

# print("所有文件处理任务已全部完成！")


# # 处理wm的数据
# import pandas as pd
# import os # 导入os模块，用于处理文件和目录

# # --- 1. 配置输入和输出文件路径 ---
# # ⚠️ 请在这里修改你的输入文件夹和文件名
# input_folder = r'D:\SZU\Experiment\Experiment_Data\0921\Wm_Beta_Data'
# input_filename = 'sdd_1036.csv'

# # ⚠️ 请在这里修改你希望保存结果的文件夹
# output_folder = r'D:\SZU\Experiment\Experiment_Data\0921\Wm_Beta_Data'
# output_filename = '0921_Wm_0.1_50.csv'

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

# import pandas as pd
# import os

# # --- 1. 配置区 ---
# # 未来您只需要修改这个区域即可

# # ⚠️ 请将此路径修改为您的CSV文件的完整路径
# # 使用 r'...' 可以避免Windows路径中的反斜杠问题
# file_path = r'D:\SZU\Experiment\Experiment_Data\0921\Wm_Beta_Data\0921_Wm_0.1_50.csv'

# # 定义要分析的列名
# time_column = 'Time'
# data_column = 'Wm'

# # 定义要搜索的时间范围 (单位：秒)
# start_time = 20.0
# end_time = 23.0


# # --- 2. 核心处理逻辑 (通常无需修改) ---

# print(f"--- 开始分析文件: {os.path.basename(file_path)} ---")
# print("-" * 50)

# try:
#     # 检查文件是否存在
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"错误：找不到文件 '{file_path}'。")

#     # 读取CSV文件
#     df = pd.read_csv(file_path)
    
#     # 筛选出在指定时间范围内的数据
#     print(f"正在筛选 {start_time}s 至 {end_time}s 之间的数据...")
#     time_slice_df = df[(df[time_column] >= start_time) & (df[time_column] <= end_time)]
    
#     # 检查筛选结果是否为空
#     if time_slice_df.empty:
#         print(f"⚠️ 警告：在 {start_time}s 至 {end_time}s 的时间范围内没有找到任何数据。")
#     else:
#         # 找到Wm列最小值的索引
#         # .idxmin() 会返回该列最小值的第一个匹配项的索引
#         min_index = time_slice_df[data_column].idxmin()
        
#         # 使用该索引从筛选后的数据中定位到整行数据
#         min_row = time_slice_df.loc[min_index]
        
#         # 从该行中提取最小值和对应的时间
#         min_value = min_row[data_column]
#         time_at_min = min_row[time_column]
        
#         # 打印最终结果
#         print("\n--- 分析结果 ---")
#         print(f"在 {start_time}s 至 {end_time}s 的时间范围内：")
#         print(f"  - {data_column} 的最小值为: {min_value}")
#         print(f"  - 该最小值出现的时刻为: {time_at_min}s")
#         print("-" * 50)

# except FileNotFoundError as e:
#     print(e)
# except KeyError as e:
#     print(f"❌ 错误：在文件中找不到指定的列名 {e}。")
#     print(f"👉 请检查第11行的 `time_column` ('{time_column}') 和第12行的 `data_column` ('{data_column}') 是否与您CSV文件中的实际列名完全匹配。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")


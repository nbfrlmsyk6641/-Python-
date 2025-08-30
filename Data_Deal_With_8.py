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
data_folder = r'F:\实验数据\0830\8'

print(f"--- 开始处理文件夹中的数据: {data_folder} ---")
print("-" * 40)

try:
    # --- 任务1: 处理 sdd_626.csv ---
    print("正在处理文件: sdd_626.csv ...")
    input_path_1 = os.path.join(data_folder, 'sdd_626.csv')
    output_path_1 = os.path.join(data_folder, '0830_Wm.csv')
    
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
    print(f"✅ 'sdd_626.csv' 处理完成，结果已保存至 '0830_Wm.csv'")
    print("-" * 40)

    # --- 任务2: 处理 sdd_627.csv ---
    print("正在处理文件: sdd_627.csv ...")
    input_path_2 = os.path.join(data_folder, 'sdd_627.csv')
    output_path_2 = os.path.join(data_folder, '0830_Te.csv')

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
    print(f"✅ 'sdd_627.csv' 处理完成，结果已保存至 '0830_Te.csv'")
    print("-" * 40)

    # --- 任务3: 处理 sdd_628.csv ---
    print("正在处理文件: sdd_628.csv ...")
    input_path_3 = os.path.join(data_folder, 'sdd_628.csv')
    output_path_3 = os.path.join(data_folder, '0830_Alpha.csv')

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
    print(f"✅ 'sdd_628.csv' 处理完成，结果已保存至 '0830_Alpha.csv'")
    print("-" * 40)
    
    print("所有文件处理任务已全部完成！")

except FileNotFoundError as e:
    print(f"❌ 错误：找不到文件。")
    print(f"请检查文件 '{e.filename}' 是否存在于您指定的文件夹中。")
    # print(f"请确认您的文件夹路径设置正确，且文件夹内包含 sdd_608.csv, sdd_609.csv, sdd_610.csv 这三个文件。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")




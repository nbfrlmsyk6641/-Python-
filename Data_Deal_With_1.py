# 从实验平台中导出的数据，用这个代码提取数据存成新的csv便于下一步处理

# # 处理wm的数据
# import pandas as pd
# import os # 导入os模块，用于处理文件和目录

# # --- 1. 配置输入和输出文件路径 ---
# # ⚠️ 请在这里修改你的输入文件夹和文件名
# input_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据'
# input_filename = 'sdd_166.csv'

# # ⚠️ 请在这里修改你希望保存结果的文件夹
# output_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据\处理后的数据'
# output_filename = '400_300_200_100wm.csv'

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

# # 处理Te的数据
# import pandas as pd
# import os # 导入os模块，用于处理文件和目录

# # --- 1. 配置输入和输出文件路径 ---
# # ⚠️ 请在这里修改你的输入文件夹和文件名
# input_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据'
# input_filename = 'sdd_167.csv'

# # ⚠️ 请在这里修改你希望保存结果的文件夹
# output_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据\处理后的数据'
# output_filename = '400_300_200_100Te.csv'  

# # 使用 os.path.join() 来智能地合并路径
# input_file_path = os.path.join(input_folder, input_filename)
# output_file_path = os.path.join(output_folder, output_filename)

# # --- 自动创建输出文件夹 ---
# # 如果指定的输出文件夹不存在，代码会自动为你创建它
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"准备处理文件: {input_file_path}")
# print(f"处理结果将保存至: {output_file_path}")
# print("-" * 30)

# try:
#     # --- 2. 读取并处理数据 ---
#     # 【已修改】usecols=[1, 2]: 指定只读取第B, C列（列索引B=1, C=2）
#     df = pd.read_csv(
#         input_file_path,
#         skiprows=28,
#         header=None,
#         usecols=[1, 2]
#     )

#     # --- 3. 重命名列名 ---
#     # 【已修改】将列名设置为 'Time' 和 'Te'
#     df.columns = ['Time', 'Te']

#     # --- 4. 保存到新的CSV文件 ---
#     df.to_csv(output_file_path, index=False)

#     print("-" * 30)
#     print(f"✅ 处理成功！")
#     print(f"已从第29行开始提取B, C列数据。")
#     print(f"重命名列为 'Time', 'Te'。")
#     print(f"结果已完整保存到文件: {output_file_path}")

# except FileNotFoundError:
#     print(f"❌ 错误：找不到文件 '{input_file_path}'。")
#     print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")


# # 处理u的数据（控制输入量）
# import pandas as pd
# import os # 导入os模块，用于处理文件和目录

# # --- 1. 配置输入和输出文件路径 ---
# # ⚠️ 请在这里修改你的输入文件夹和文件名
# input_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据'
# input_filename = 'sdd_169.csv'

# # ⚠️ 请在这里修改你希望保存结果的文件夹
# output_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据\处理后的数据'
# output_filename = '400_300_200_100u.csv' 

# # 使用 os.path.join() 来智能地合并路径
# input_file_path = os.path.join(input_folder, input_filename)
# output_file_path = os.path.join(output_folder, output_filename)

# # --- 自动创建输出文件夹 ---
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
#         usecols=[1, 2, 3, 4]
#     )

#     # --- 3. 重命名列名 ---
#     df.columns = ['Time', 'uk_1', 'uk_2', 'uk_3']

#     # --- 4. 保存到新的CSV文件 ---
#     df.to_csv(output_file_path, index=False)

#     print("-" * 30)
#     print(f"✅ 处理成功！")
#     print(f"已从第29行开始提取B, C, D, E列数据。")
#     print(f"重命名列为 'Time', 'uk_1', 'uk_2', 'uk_3'。")
#     print(f"结果已完整保存到文件: {output_file_path}")

# except FileNotFoundError:
#     print(f"❌ 错误：找不到文件 '{input_file_path}'。")
#     print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")

# 处理y的数据（系统输出量）
import pandas as pd
import os # 导入os模块，用于处理文件和目录

# --- 1. 配置输入和输出文件路径 ---
# ⚠️ 请在这里修改你的输入文件夹和文件名
input_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据'
input_filename = 'sdd_170.csv'

# ⚠️ 请在这里修改你希望保存结果的文件夹
output_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据\处理后的数据'
output_filename = '400_300_200_100y.csv'

# 使用 os.path.join() 来智能地合并路径
input_file_path = os.path.join(input_folder, input_filename)
output_file_path = os.path.join(output_folder, output_filename)

# --- 自动创建输出文件夹 ---
# 如果指定的输出文件夹不存在，代码会自动为你创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"输出文件夹不存在，已自动创建: {output_folder}")

print(f"准备处理文件: {input_file_path}")
print(f"处理结果将保存至: {output_file_path}")
print("-" * 30)

try:
    # --- 2. 读取并处理数据 ---
    df = pd.read_csv(
        input_file_path,
        skiprows=28,
        header=None,
        usecols=[1, 2, 3, 4, 5]
    )

    # --- 3. 重命名列名 ---
    df.columns = ['Time', 'yk', 'yk_1', 'yk_2', 'yk_3']

    # --- 4. 保存到新的CSV文件 ---
    df.to_csv(output_file_path, index=False)

    print("-" * 30)
    print(f"✅ 处理成功！")
    print(f"已从第29行开始提取B, C, D, E, F, G列数据。")
    print(f"重命名列为 'Time', 'yk', 'yk_1', 'yk_2', 'yk_3', 'yk_4'。")
    print(f"结果已完整保存到文件: {output_file_path}")

except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{input_file_path}'。")
    print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")



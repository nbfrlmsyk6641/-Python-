# # 按照网络输入向量的定义合并输入输出数据用于网络训练

# import pandas as pd
# import os

# # --- 1. 配置输入和输出文件路径 ---
# # ⚠️ 请在这里配置你的文件夹路径
# input_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据\处理后的数据\u_y_Data'
# output_folder = r'C:\Users\23688\Desktop\实验数据\0803Data\重新采集用于训练的原始数据\处理后的数据\Train_Data'

# # ⚠️ 请在这里确认你的输入文件名
# u_history_filename = '400_300_200_100u.csv'
# y_history_filename = '400_300_200_100y.csv'

# # 这是处理后要保存的文件名，可以自定义
# output_filename = '400_300_200_100_Trainingdata.csv'

# # --- 使用 os.path.join() 智能地组合完整路径 ---
# u_file_path = os.path.join(input_folder, u_history_filename)
# y_file_path = os.path.join(input_folder, y_history_filename)
# output_file_path = os.path.join(output_folder, output_filename)

# # --- 自动创建输出文件夹 ---
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#     print(f"输出文件夹不存在，已自动创建: {output_folder}")

# print(f"准备读取文件 1: {u_file_path}")
# print(f"准备读取文件 2: {y_file_path}")
# print(f"处理结果将保存至: {output_file_path}")
# print("-" * 30)

# try:
#     # --- 2. 分别读取两个CSV文件 ---
#     # 这次数据文件有列名，所以我们不需要 header=None 和 skiprows
#     u_df = pd.read_csv(u_file_path)
#     y_df = pd.read_csv(y_file_path)

#     # --- 3. 按指定顺序构建新的DataFrame ---
#     # 这是最关键的一步，我们创建一个字典，key是新的列名，value是对应的数据来源
#     # .iloc[:, index] 用于按位置精确提取列 (所有行, 指定索引的列)
#     # B列=索引1, C列=索引2, D列=索引3
#     final_df = pd.DataFrame({
#         'uk_1': u_df.iloc[:, 1],  # 来自 u_History 的 B列
#         'uk_2': u_df.iloc[:, 2],  # 来自 u_History 的 C列
#         'yk_1': y_df.iloc[:, 2],  # 来自 y_History 的 C列
#         'yk_2': y_df.iloc[:, 3],  # 来自 y_History 的 D列
#         'yk':   y_df.iloc[:, 1]   # 来自 y_History 的 B列 (注意这里的顺序调整)
#     })

#     # --- 4. 保存到新的CSV文件 ---
#     final_df.to_csv(output_file_path, index=False)

#     print("-" * 30)
#     print(f"✅ 处理成功！")
#     print(f"已从 '{u_history_filename}' 和 '{y_history_filename}' 中提取并合并数据。")
#     print(f"结果已保存到文件: {output_filename}")

# except FileNotFoundError as e:
#     print(f"❌ 错误：找不到文件。")
#     print(f"请检查文件是否存在于指定路径: {e.filename}")
# except IndexError:
#     print(f"❌ 错误：列索引超出范围。")
#     print(f"请检查 '{u_history_filename}' 文件是否至少有C列。")
#     print(f"请检查 '{y_history_filename}' 文件是否至少有D列。")
# except Exception as e:
#     print(f"❌ 处理过程中发生未知错误: {e}")
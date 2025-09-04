import pandas as pd
import os

# --- 1. 请在这里配置您的基本信息 ---

# ⚠️ 请将此路径修改为您存放24个文件夹的根目录
# 例如，如果您的文件夹是 F:\实验数据\0903\1, F:\实验数据\0903\2, ...
# 那么根目录就是 F:\实验数据\0903
base_folder = r'F:\实验数据\0903'

# 总共要处理的文件夹（组）数量
num_groups = 4

# 第1组中，第一个文件的起始编号 (例如 sdd_629.csv 中的 629)
start_file_number = 701

print(f"--- 开始批量处理 {num_groups} 组实验数据 ---")
print(f"根目录: {base_folder}")
print("-" * 50)

# --- 2. 使用循环遍历每一个文件夹（组） ---
for i in range(1, num_groups + 1):
    
    current_folder_path = os.path.join(base_folder, str(i))
    print(f"正在处理第 {i} 组，文件夹: {current_folder_path}")
    
    # 检查文件夹是否存在
    if not os.path.exists(current_folder_path):
        print(f"  ❌ 警告：文件夹不存在，跳过第 {i} 组。")
        print("-" * 50)
        continue # 跳过本次循环，继续处理下一组

    try:
        # --- 3. 根据组号动态计算三个输入文件的编号 ---
        # 公式：起始编号 + (组号 - 1) * 3
        folder_start_num = start_file_number + (i - 1) * 3
        
        # 定义输入和输出文件名
        # 输入文件名
        input_wm_filename = f'sdd_{folder_start_num}.csv'
        input_te_filename = f'sdd_{folder_start_num + 1}.csv'
        input_alpha_filename = f'sdd_{folder_start_num + 2}.csv'
        
        # 输出文件名
        output_wm_filename = f'0903_Wm_{i}.csv'
        output_te_filename = f'0903_Te_{i}.csv'
        output_alpha_filename = f'0903_Alpha_{i}.csv'

        # --- 任务1: 处理 Wm 数据 (sdd_***) ---
        input_path = os.path.join(current_folder_path, input_wm_filename)
        output_path = os.path.join(current_folder_path, output_wm_filename)
        
        df_wm = pd.read_csv(input_path, skiprows=28, header=None, usecols=[1, 2, 3])
        df_wm.columns = ['Time', 'Wm', 'Wr']
        df_wm.to_csv(output_path, index=False)
        print(f"  ✅ {input_wm_filename} -> {output_wm_filename}")
        
        # --- 任务2: 处理 Te 数据 (sdd_***+1) ---
        input_path = os.path.join(current_folder_path, input_te_filename)
        output_path = os.path.join(current_folder_path, output_te_filename)

        df_te = pd.read_csv(input_path, skiprows=28, header=None, usecols=[1, 2, 3])
        df_te.columns = ['Time', 'Te', 'Ts']
        df_te.to_csv(output_path, index=False)
        print(f"  ✅ {input_te_filename} -> {output_te_filename}")
        
        # --- 任务3: 处理 Alpha 数据 (sdd_***+2) ---
        input_path = os.path.join(current_folder_path, input_alpha_filename)
        output_path = os.path.join(current_folder_path, output_alpha_filename)

        df_alpha = pd.read_csv(input_path, skiprows=28, header=None, usecols=[1, 2])
        
        # 【关键步骤】对提取出的第二列 (原始C列) 的所有数据乘以10
        # df_alpha.iloc[:, 1] 表示选取所有行的第2列 (索引为1)
        df_alpha.iloc[:, 1] = df_alpha.iloc[:, 1] * 10
        
        df_alpha.columns = ['Time', 'Alpha']
        df_alpha.to_csv(output_path, index=False)
        print(f"  ✅ {input_alpha_filename} -> {output_alpha_filename} (C列已乘以10)")

        print(f"--- 第 {i} 组处理完成 ---")
        print("-" * 50)

    except FileNotFoundError as e:
        print(f"  ❌ 错误: 在第 {i} 组中找不到文件 {e.filename}。请检查文件名是否正确。跳过此组。")
        print("-" * 50)
    except Exception as e:
        print(f"  ❌ 在处理第 {i} 组时发生未知错误: {e}。跳过此组。")
        print("-" * 50)

print("所有组别处理完毕！")
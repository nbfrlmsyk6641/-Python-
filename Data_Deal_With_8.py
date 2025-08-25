import pandas as pd
import os # 导入os模块，用于处理文件和目录

# --- 1. 配置输入和输出文件路径 ---
# ⚠️ 请在这里修改你的输入文件夹和文件名
input_folder = r'F:\实验数据\0824\扰动模态\0.09倍'
input_filename = 'sdd_588.csv'

# ⚠️ 请在这里修改你希望保存结果的文件夹
output_folder = r'F:\实验数据\0824\扰动模态\0.09倍\处理后的数据'
output_filename = '0824_wm_D_0.09.csv'


input_file_path = os.path.join(input_folder, input_filename)
output_file_path = os.path.join(output_folder, output_filename)

# --- 新增功能：自动创建输出文件夹 ---
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
        usecols=[1, 2, 3]
    )

    # --- 3. 重命名列名 ---
    df.columns = ['Time', 'Wm', 'Wr']

    # --- 4. 保存到新的CSV文件 ---
    df.to_csv(output_file_path, index=False)

    print("-" * 30)
    print(f"✅ 处理成功！结果已保存。")

except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{input_file_path}'。")
    print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")


input_folder = r'F:\实验数据\0824\扰动模态\0.09倍'
input_filename = 'sdd_589.csv'

# ⚠️ 请在这里修改你希望保存结果的文件夹
output_folder = r'F:\实验数据\0824\扰动模态\0.09倍\处理后的数据'
output_filename = '0824_Te_Ts_D_0.09.csv'


input_file_path = os.path.join(input_folder, input_filename)
output_file_path = os.path.join(output_folder, output_filename)

# --- 新增功能：自动创建输出文件夹 ---
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
        usecols=[1, 2, 3]
    )

    # --- 3. 重命名列名 ---
    df.columns = ['Time', 'Te', 'Ts']

    # --- 4. 保存到新的CSV文件 ---
    df.to_csv(output_file_path, index=False)

    print("-" * 30)
    print(f"✅ 处理成功！结果已保存。")

except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{input_file_path}'。")
    print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")


input_folder = r'F:\实验数据\0824\扰动模态\0.09倍'
input_filename = 'sdd_590.csv'

# ⚠️ 请在这里修改你希望保存结果的文件夹
output_folder = r'F:\实验数据\0824\扰动模态\0.09倍\处理后的数据'
output_filename = '0824_ISE_D_0.09.csv'


input_file_path = os.path.join(input_folder, input_filename)
output_file_path = os.path.join(output_folder, output_filename)

# --- 新增功能：自动创建输出文件夹 ---
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
        usecols=[1, 2]
    )

    # --- 3. 重命名列名 ---
    df.columns = ['Time', 'ISE']

    # --- 4. 保存到新的CSV文件 ---
    df.to_csv(output_file_path, index=False)

    print("-" * 30)
    print(f"✅ 处理成功！结果已保存。")

except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{input_file_path}'。")
    print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")


input_folder = r'F:\实验数据\0824\扰动模态\0.09倍'
input_filename = 'sdd_591.csv'

# ⚠️ 请在这里修改你希望保存结果的文件夹
output_folder = r'F:\实验数据\0824\扰动模态\0.09倍\处理后的数据'
output_filename = '0824_Feature_D_0.09.csv'

# 使用 os.path.join() 来智能地合并路径，这是最推荐的做法
# 它会自动处理Windows(\)和Mac/Linux(/)下不同的路径分隔符
input_file_path = os.path.join(input_folder, input_filename)
output_file_path = os.path.join(output_folder, output_filename)

# --- 新增功能：自动创建输出文件夹 ---
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
        usecols=[1, 2, 3, 4, 5, 6, 7]
    )

    # --- 3. 重命名列名 ---
    df.columns = ['Time', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6']

    # --- 4. 保存到新的CSV文件 ---
    df.to_csv(output_file_path, index=False)

    print("-" * 30)
    print(f"✅ 处理成功！结果已保存。")

except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{input_file_path}'。")
    print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")


input_folder = r'F:\实验数据\0824\扰动模态\0.09倍'
input_filename = 'sdd_592.csv'

# ⚠️ 请在这里修改你希望保存结果的文件夹
output_folder = r'F:\实验数据\0824\扰动模态\0.09倍\处理后的数据'
output_filename = '0824_TL_D_0.09.csv'


input_file_path = os.path.join(input_folder, input_filename)
output_file_path = os.path.join(output_folder, output_filename)

# --- 新增功能：自动创建输出文件夹 ---
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
        usecols=[1, 2, 3]
    )

    # --- 3. 重命名列名 ---
    df.columns = ['Time', 'TL', 'TL_real']

    # --- 4. 保存到新的CSV文件 ---
    df.to_csv(output_file_path, index=False)

    print("-" * 30)
    print(f"✅ 处理成功！结果已保存。")

except FileNotFoundError:
    print(f"❌ 错误：找不到文件 '{input_file_path}'。")
    print("请仔细检查你的输入文件夹路径和文件名是否完全正确。")
except Exception as e:
    print(f"❌ 处理过程中发生未知错误: {e}")


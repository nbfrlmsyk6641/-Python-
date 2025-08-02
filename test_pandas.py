# test_pandas.py
try:
    import pandas as pd
    print("✅ 成功导入 pandas 库！")
    print(f"   Pandas 版本号: {pd.__version__}")
    print("你的数据处理环境已准备就绪。")

except ImportError:
    print("❌ 错误：未能导入 pandas 库。")
    print("请在你的终端或命令行中运行以下命令来安装它：")
    print("pip install pandas")
import os
import google.generativeai as genai

print("开始测试与Google的直接连接...")

# 1. 尝试从环境变量加载API Key
try:
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("错误：无法在环境变量中找到 GEMINI_API_KEY。")
        print("请确认您在运行此脚本的终端里正确设置了环境变量。")
        exit() # 退出程序

    print("API Key 已成功加载。")
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"配置API Key时出错: {e}")
    exit()

# 2. 尝试连接Google并获取回复
try:
    print("正在连接Google服务器，请稍候...")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("请用一个词形容宇宙。")

    print("\n--- 测试成功！---")
    print("收到的回复:", response.text)
    print("--------------------")

except Exception as e:
    print("\n--- 测试失败！---")
    print(f"在连接Google或生成内容时发生错误: {e}")
    print("--------------------")
    print("提示：请检查您的网络连接、防火墙或代理设置。")

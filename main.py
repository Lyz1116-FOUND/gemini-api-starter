"""
Google Gemini API 入门项目
使用 Gemini 3 Flash 模型进行文本对话
适合人工智能专业大二学生学习
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def initialize_gemini():
    """初始化 Gemini API"""
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "未找到 Google API Key！\n"
            "请执行以下步骤：\n"
            "1. 在项目根目录创建 .env 文件\n"
            "2. 添加以下内容：GOOGLE_API_KEY=你的API密钥\n"
            "3. 获取API密钥：https://makersuite.google.com/app/apikey"
        )

    genai.configure(api_key=api_key)
    # 使用 Gemini 3 Flash 模型（如果不可用，会自动回退到 gemini-1.5-flash）
    # 优先尝试最新的 Flash 模型
    models_to_try = [
        'gemini-2.0-flash-exp',      # Gemini 3 Flash 实验版
        'gemini-1.5-flash-latest',   # 最新稳定版
        'gemini-1.5-flash'           # 稳定版
    ]

    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            print(f"使用模型: {model_name}")
            return model
        except Exception as e:
            continue

    # 如果所有模型都失败，抛出异常
    raise ValueError(f"无法初始化 Gemini 模型，请检查 API 密钥是否正确")

def chat_with_gemini(model, prompt):
    """与 Gemini 模型对话"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"错误：{str(e)}"

def main():
    """主函数"""
    print("=" * 50)
    print("Google Gemini API 入门项目")
    print("使用 Gemini 3 Flash 模型")
    print("=" * 50)
    print()

    try:
        # 初始化模型
        print("正在初始化 Gemini 模型...")
        model = initialize_gemini()
        print("✓模型初始化成功！\n")

        # 示例对话
        examples = [
            "你好，请介绍一下自己",
            "什么是人工智能？",
            "用Python写一个简单的排序算法"
        ]

        print("开始对话（输入 'quit' 退出）\n")

        # 交互式对话
        while True:
            user_input = input("你: ")

            if user_input.lower() in ['quit', 'exit', '退出', 'q']:
                print("\n再见！")
                break

            if not user_input.strip():
                print("请输入有效的问题...\n")
                continue

            print("Gemini: ", end="")
            response = chat_with_gemini(model, user_input)
            print(response)
            print()

    except KeyboardInterrupt:
        print("\n\n程序已中断")
    except Exception as e:
        print(f"\n错误：{str(e)}")

if __name__ == "__main__":
    main()

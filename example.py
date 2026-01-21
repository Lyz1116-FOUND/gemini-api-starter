"""
Google Gemini API 使用示例
使用 Gemini 3 Flash 模型展示不同的API调用方式
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def example_1_simple_chat():
    """示例1：简单的单次对话"""
    print("=" * 50)
    print("示例1：简单的单次对话")
    print("=" * 50)

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    # 使用 Gemini 3 Flash 模型（自动选择可用版本）
    models_to_try = [
        'gemini-2.0-flash-exp',
        'gemini-1.5-flash-latest',
        'gemini-1.5-flash'
    ]
    model = None
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            break
        except Exception:
            continue
    if model is None:
        raise ValueError("无法初始化 Gemini 模型")

    prompt = "用一句话介绍Python编程语言"
    response = model.generate_content(prompt)
    print(f"问题: {prompt}")
    print(f"回答: {response.text}\n")

def example_2_multiturn_chat():
    """示例2：多轮对话"""
    print("=" * 50)
    print("示例2：多轮对话")
    print("=" * 50)

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    # 使用 Gemini 3 Flash 模型（自动选择可用版本）
    models_to_try = [
        'gemini-2.0-flash-exp',
        'gemini-1.5-flash-latest',
        'gemini-1.5-flash'
    ]
    model = None
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            break
        except Exception:
            continue
    if model is None:
        raise ValueError("无法初始化 Gemini 模型")

    chat = model.start_chat(history=[])

    # 第一轮对话
    response1 = chat.send_message("我叫小明，我喜欢编程")
    print(f"用户: 我叫小明，我喜欢编程")
    print(f"AI: {response1.text}\n")

    # 第二轮对话（有上下文）
    response2 = chat.send_message("你还记得我的名字吗？")
    print(f"用户: 你还记得我的名字吗？")
    print(f"AI: {response2.text}\n")

def example_3_batch_questions():
    """示例3：批量问题处理"""
    print("=" * 50)
    print("示例3：批量问题处理")
    print("=" * 50)

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    # 使用 Gemini 3 Flash 模型（自动选择可用版本）
    models_to_try = [
        'gemini-2.0-flash-exp',
        'gemini-1.5-flash-latest',
        'gemini-1.5-flash'
    ]
    model = None
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            break
        except Exception:
            continue
    if model is None:
        raise ValueError("无法初始化 Gemini 模型")

    questions = [
        "什么是机器学习？",
        "什么是深度学习？",
        "什么是自然语言处理？"
    ]

    for i, question in enumerate(questions, 1):
        response = model.generate_content(question)
        print(f"问题{i}: {question}")
        print(f"回答: {response.text[:100]}...\n")  # 只显示前100个字符

def example_4_streaming():
    """示例4：流式输出（打字机效果）"""
    print("=" * 50)
    print("示例4：流式输出")
    print("=" * 50)

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    # 使用 Gemini 3 Flash 模型（自动选择可用版本）
    models_to_try = [
        'gemini-2.0-flash-exp',
        'gemini-1.5-flash-latest',
        'gemini-1.5-flash'
    ]
    model = None
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            break
        except Exception:
            continue
    if model is None:
        raise ValueError("无法初始化 Gemini 模型")

    prompt = "介绍一下人工智能的发展历史"
    print(f"问题: {prompt}")
    print("回答: ", end="", flush=True)

    response = model.generate_content(prompt, stream=True)
    for chunk in response:
        print(chunk.text, end="", flush=True)
    print("\n")

def main():
    """运行所有示例"""
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("错误：未找到 GOOGLE_API_KEY")
            print("请在 .env 文件中设置 API 密钥")
            return

        # 运行示例
        example_1_simple_chat()
        example_2_multiturn_chat()
        example_3_batch_questions()
        example_4_streaming()

    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main()

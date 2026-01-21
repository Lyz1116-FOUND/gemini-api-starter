"""
Google Gemini API 入门项目
使用 Gemini 3 Flash 模型进行文本对话
适合人工智能专业大二学生学习
"""

import os
import re
import sys
import time
import argparse

def _check_interpreter_mismatch() -> None:
    conda_prefix = os.getenv("CONDA_PREFIX")
    virtual_env = os.getenv("VIRTUAL_ENV")
    expected_prefix = conda_prefix or virtual_env
    if not expected_prefix:
        return

    exe = sys.executable or ""
    if exe and not exe.startswith(expected_prefix):
        env_hint = os.getenv("CONDA_DEFAULT_ENV") or os.path.basename(expected_prefix)
        raise SystemExit(
            "检测到你已激活虚拟环境，但当前运行的不是该环境的 Python。\n\n"
            f"- 当前解释器：{exe}\n"
            f"- 环境前缀：{expected_prefix}\n\n"
            "请不要用 /bin/python3 或 /usr/bin/python3 这种绝对路径运行。\n"
            "改用以下任一方式：\n"
            f"1) 直接用当前环境：python main.py\n"
            f"2) 不激活也能跑：conda run -n {env_hint} python main.py\n"
        )


_check_interpreter_mismatch()


from google import genai
from dotenv import load_dotenv


# 加载环境变量
load_dotenv()

def initialize_gemini():
    """初始化 Gemini API"""
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "未找到 Google API Key！\n"
            "请执行以下步骤：\n"
            "1. 在项目根目录创建 .env 文件\n"
            "2. 添加以下内容：GOOGLE_API_KEY=你的API密钥（或 GEMINI_API_KEY=你的API密钥）\n"
            "3. 获取API密钥：https://aistudio.google.com/app/apikey"
        )

    client = genai.Client(api_key=api_key)
    model_name = (
        os.getenv("GEMINI_MODEL")
        or os.getenv("GOOGLE_GEMINI_MODEL")
        or "gemini-2.5-flash-lite"
    )
    print(f"使用模型: {model_name}")
    return client, model_name


def _extract_text(response) -> str:
    text = getattr(response, "text", None)
    if isinstance(text, str) and text.strip():
        return text
    candidates = getattr(response, "candidates", None)
    if not candidates:
        return str(response)
    content = getattr(candidates[0], "content", None)
    parts = getattr(content, "parts", None) if content is not None else None
    if parts:
        part_text = getattr(parts[0], "text", None)
        if isinstance(part_text, str):
            return part_text
    return str(response)


def _extract_retry_delay_seconds(error: Exception) -> float | None:
    message = str(error)
    # Common formats:
    # - "Please retry in 58.9s."
    # - "'retryDelay': '58s'"
    match = re.search(r"retry in\s+([0-9]+(?:\.[0-9]+)?)s", message, re.IGNORECASE)
    if match:
        return float(match.group(1))
    match = re.search(r"retryDelay'\s*:\s*'([0-9]+)s'", message)
    if match:
        return float(match.group(1))
    return None

def chat_with_gemini(client, model_name, prompt):
    """与 Gemini 模型对话"""
    last_error: Exception | None = None
    for attempt in range(2):
        try:
            response = client.models.generate_content(model=model_name, contents=prompt)
            return _extract_text(response)
        except Exception as e:
            last_error = e
            delay = _extract_retry_delay_seconds(e)
            if delay is not None and delay > 0 and attempt == 0:
                wait_seconds = min(delay, 60.0)
                print(f"\n（触发限流/额度限制，等待 {wait_seconds:.0f}s 后自动重试一次…）")
                time.sleep(wait_seconds)
                continue
            break

    message = str(last_error) if last_error is not None else "未知错误"
    if "RESOURCE_EXHAUSTED" in message or "exceeded your current quota" in message:
        return (
            "错误：429 RESOURCE_EXHAUSTED（配额/额度不足或触发限流）\n"
            "建议：\n"
            "1) 等待 1 分钟后再试（如果是每分钟限流）\n"
            "2) 到 https://ai.dev/rate-limit 查看当前额度\n"
            "3) 检查 AI Studio / Google Cloud 项目是否已开通计费与配额（有些账号免费额度可能为 0）\n"
            "4) 也可在 .env 设置 GEMINI_MODEL=gemini-2.5-flash-lite（或你在 AI Studio 页面选择的模型）\n"
            f"\n原始信息：{message}"
        )
    return f"错误：{message}"


def _run_examples(client, model_name) -> None:
    examples = [
        "你好，请介绍一下自己",
        "什么是人工智能？",
        "用Python写一个简单的排序算法",
    ]
    for prompt in examples:
        print(f"\n你: {prompt}")
        print("Gemini: ", end="")
        print(chat_with_gemini(client, model_name, prompt))


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Google Gemini API 入门项目")
    parser.add_argument(
        "--prompt",
        type=str,
        default=None,
        help="单次提问内容（提供后将不会进入交互模式）",
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="运行内置示例问题后退出",
    )
    return parser.parse_args()

def main():
    """主函数"""
    args = _parse_args()

    print("=" * 50)
    print("Google Gemini API 入门项目")
    print("使用 Gemini 3 Flash 模型")
    print("=" * 50)
    print()

    try:
        # 初始化模型
        print("正在初始化 Gemini 模型...")
        client, model_name = initialize_gemini()
        print("✓ 模型初始化成功！\n")

        if args.prompt is not None:
            print(f"你: {args.prompt}")
            print("Gemini: ", end="")
            print(chat_with_gemini(client, model_name, args.prompt))
            return

        # VS Code Task 等非交互环境里 stdin 可能被关闭，会导致 input() 直接 EOF。
        if args.examples or not sys.stdin.isatty():
            if not sys.stdin.isatty() and not args.examples:
                print("检测到当前是非交互运行（无法读取输入），将自动运行示例问题。")
                print("想交互聊天请在终端运行：conda activate pytorch-cu128 && python main.py")
            _run_examples(client, model_name)
            return

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
            response = chat_with_gemini(client, model_name, user_input)
            print(response)
            print()

    except KeyboardInterrupt:
        print("\n\n程序已中断")
    except Exception as e:
        print(f"\n错误：{str(e)}")

if __name__ == "__main__":
    main()

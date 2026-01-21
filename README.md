# Google Gemini API 入门项目

这是一个使用 Google Gemini 3 Flash 模型的简单聊天机器人项目，适合人工智能专业大二学生学习和实践。

## 功能特点

- ✅ 使用 Google Gemini 3 Flash API 进行文本对话
- ✅ 简单的命令行交互界面
- ✅ 清晰的代码注释，易于理解
- ✅ 错误处理和用户友好的提示信息

## 项目结构

```
.
├── main.py              # 主程序文件（交互式对话）
├── example.py           # API使用示例文件
├── requirements.txt     # Python依赖包
├── config.example.py    # 配置文件示例
├── .env.example        # 环境变量示例文件
├── .gitignore          # Git忽略文件
└── README.md           # 项目说明文档
```

## 快速开始

### 1. 克隆项目

```bash
git clone <repository-url>
cd gemini-api-starter
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 获取 Google API 密钥

1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 登录你的 Google 账号
3. 创建新的 API 密钥
4. 复制你的 API 密钥

### 4. 配置 API 密钥

创建 `.env` 文件（推荐方式）：

```bash
# 在项目根目录创建 .env 文件
echo "GOOGLE_API_KEY=你的API密钥" > .env
```

或者修改 `config.example.py` 为 `config.py` 并填入密钥。

### 5. 运行项目

**运行交互式对话程序：**
```bash
python main.py
```

**运行示例代码（学习不同的API用法）：**
```bash
python example.py
```

## 使用示例

```
==================================================
Google Gemini API 入门项目
使用 Gemini 3 Flash 模型
==================================================

正在初始化 Gemini 模型...
使用模型: gemini-2.0-flash-exp
✓ 模型初始化成功！

开始对话（输入 'quit' 退出）

你: 你好，请介绍一下自己
Gemini: 你好！我是 Gemini，一个由 Google 开发的大型语言模型...

你: 什么是人工智能？
Gemini: 人工智能（AI）是计算机科学的一个分支...

你: quit
再见！
```

## 学习要点

### 1. API 调用基础
- 如何使用 Google Generative AI SDK
- 如何进行 API 认证和配置

### 2. 环境变量管理
- 使用 `.env` 文件保护敏感信息
- 使用 `python-dotenv` 加载环境变量

### 3. 错误处理
- 处理 API 调用异常
- 用户友好的错误提示

### 4. 交互式程序设计
- 命令行交互循环
- 用户输入处理

## 扩展练习

1. **添加对话历史**：保存多轮对话上下文
2. **支持多模态**：添加图片输入功能
3. **流式输出**：实现打字机效果
4. **Web界面**：使用 Flask/FastAPI 创建 Web 应用
5. **批量处理**：从文件读取多个问题进行批量问答

## 技术栈

- Python 3.7+
- google-generativeai: Google Gemini API SDK
- python-dotenv: 环境变量管理

## 注意事项

- 🔒 **不要将 API 密钥提交到 Git 仓库**
- 💰 API 调用可能需要付费（请查看 Google 定价）
- ⚠️ 注意 API 的调用频率限制

## 参考资料

- [Google Gemini API 文档](https://ai.google.dev/docs)
- [Python SDK 文档](https://ai.google.dev/api/python)
- [获取 API 密钥](https://makersuite.google.com/app/apikey)

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

---

**适合人群**：人工智能专业大二学生
**难度等级**：⭐⭐ (入门级)
**预计学习时间**：1-2 小时

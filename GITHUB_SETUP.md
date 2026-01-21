# GitHub 发布指南

本指南将帮助你将这个项目发布到 GitHub 上。

## 准备工作

### 1. 确保已安装 Git

检查 Git 是否已安装：
```bash
git --version
```

如果未安装，请安装 Git：
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install git -y

# 或访问 https://git-scm.com/downloads 下载
```

### 2. 配置 Git（如果第一次使用）

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

## 发布步骤

### 步骤 1：初始化 Git 仓库

在项目目录中执行：

```bash
cd /home/lyz/gemini-api-starter
git init
```

### 步骤 2：添加所有文件到暂存区

```bash
git add .
```

### 步骤 3：提交更改

```bash
git commit -m "Initial commit: Gemini 3 Flash API 入门项目"
```

### 步骤 4：在 GitHub 上创建新仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角的 `+` 号，选择 `New repository`
3. 填写仓库信息：
   - **Repository name**: `gemini-api-starter` (或你喜欢的名称)
   - **Description**: `Google Gemini 3 Flash API 入门项目 - 适合AI专业大二学生`
   - **Visibility**: 选择 `Public` (公开) 或 `Private` (私有)
   - ⚠️ **不要**勾选 "Initialize this repository with a README"（因为我们已经有了）
4. 点击 `Create repository`

### 步骤 5：连接本地仓库到 GitHub

GitHub 创建仓库后会显示命令，或者手动执行：

```bash
git remote add origin https://github.com/你的用户名/gemini-api-starter.git
```

**注意**：将 `你的用户名` 替换为你的 GitHub 用户名。

### 步骤 6：推送代码到 GitHub

```bash
git branch -M main
git push -u origin main
```

如果要求输入用户名和密码，请使用：
- **用户名**: 你的 GitHub 用户名
- **密码**: 使用 Personal Access Token（不是 GitHub 密码）

#### 如何创建 Personal Access Token

如果遇到密码认证问题，需要创建 Token：

1. 访问 [GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)](https://github.com/settings/tokens)
2. 点击 `Generate new token` > `Generate new token (classic)`
3. 设置：
   - **Note**: `gemini-api-starter`
   - **Expiration**: 选择过期时间（建议 90 天或更长）
   - **Scopes**: 勾选 `repo`（完整仓库访问权限）
4. 点击 `Generate token`
5. **复制生成的 token**（只显示一次，请保存好）
6. 在推送时使用这个 token 作为密码

### 步骤 7：验证

访问你的 GitHub 仓库页面，应该能看到所有文件已上传：
```
https://github.com/你的用户名/gemini-api-starter
```

## 后续更新

当你修改代码后，使用以下命令更新 GitHub：

```bash
# 1. 查看更改
git status

# 2. 添加更改的文件
git add .

# 3. 提交更改
git commit -m "描述你的更改内容"

# 4. 推送到 GitHub
git push
```

## 常见问题

### Q: 推送时提示 "Permission denied"
**A**: 检查是否使用了正确的用户名和 Personal Access Token。

### Q: 推送时提示 "remote origin already exists"
**A**: 删除旧的远程仓库配置：
```bash
git remote remove origin
git remote add origin https://github.com/你的用户名/gemini-api-starter.git
```

### Q: 如何更改仓库地址？
**A**:
```bash
git remote set-url origin https://github.com/新用户名/新仓库名.git
```

### Q: 如何忽略某些文件？
**A**: 编辑 `.gitignore` 文件，添加要忽略的文件或目录名称。

## 安全提示

⚠️ **重要**:
- ✅ `.env` 文件已在 `.gitignore` 中，不会被上传
- ✅ `config.py` 已在 `.gitignore` 中，不会被上传
- ❌ **永远不要**将 API 密钥提交到 GitHub
- ❌ **永远不要**将密码、token 等敏感信息提交到仓库

## 完成！

项目已成功发布到 GitHub！🎉

现在你可以：
- 分享仓库链接给他人
- 在 README 中添加项目说明
- 继续开发并推送更新
- 创建 Issues 和 Pull Requests

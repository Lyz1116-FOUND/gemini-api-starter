# GitHub 仓库创建指南

## 快速创建步骤

### 方法一：通过网页创建（推荐）

1. **访问 GitHub 创建页面**
   - 直接访问：https://github.com/new
   - 或点击你的 GitHub 主页右上角的 `+` → `New repository`

2. **填写仓库信息**
   ```
   Owner: Lyz1116-FOUND
   Repository name: gemini-api-starter
   Description: Google Gemini 3 Flash API 入门项目 - 适合AI专业大二学生学习
   ```

3. **选择可见性**
   - Public（公开）- 任何人都可以看到
   - Private（私有）- 只有你可以看到

4. **重要：不要初始化**
   - ❌ 不要勾选 "Add a README file"
   - ❌ 不要勾选 "Add .gitignore"
   - ❌ 不要勾选 "Choose a license"
   - 因为我们已经有了这些文件！

5. **点击 "Create repository"**

6. **创建完成后，回到项目目录运行推送脚本**
   ```bash
   cd /home/lyz/gemini-api-starter
   ./complete_setup.sh
   ```

### 方法二：使用 GitHub CLI（如果已安装）

```bash
# 安装 GitHub CLI（如果未安装）
# Ubuntu/Debian: sudo apt install gh
# 或访问: https://cli.github.com/

# 登录
gh auth login

# 创建仓库并推送
cd /home/lyz/gemini-api-starter
gh repo create gemini-api-starter --public --source=. --remote=origin --push
```

## 创建后的推送步骤

创建仓库后，执行以下命令：

```bash
cd /home/lyz/gemini-api-starter

# 配置 Git（如果未配置）
git config user.name "Lyz1116-FOUND"
git config user.email "lyz1116@users.noreply.github.com"

# 提交文件
git add .
git commit -m "Initial commit: Google Gemini 3 Flash API 入门项目"

# 设置分支
git branch -M main

# 推送
git push -u origin main
```

## 认证设置

如果推送时提示输入密码，需要：

1. **创建 Personal Access Token**
   - 访问：https://github.com/settings/tokens
   - 点击 "Generate new token (classic)"
   - Token名称：`gemini-api-starter`
   - 过期时间：选择 90 天或更长
   - 权限：勾选 `repo`（完整仓库访问权限）
   - 点击 "Generate token"
   - **复制 Token**（只显示一次！）

2. **使用 Token 推送**
   - 用户名：`Lyz1116-FOUND`
   - 密码：**使用刚才复制的 Token**（不是 GitHub 密码）

## 验证

推送成功后，访问以下地址查看仓库：
```
https://github.com/Lyz1116-FOUND/gemini-api-starter
```

## 需要帮助？

如果遇到问题，查看：
- `fix_push_error.md` - 错误解决指南
- `GITHUB_SETUP.md` - 详细的 GitHub 设置指南

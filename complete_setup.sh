#!/bin/bash
# 完整的GitHub发布脚本
# 自动配置环境并推送到GitHub

set -e

echo "=========================================="
echo "GitHub 完整发布流程"
echo "=========================================="
echo ""

cd /home/lyz/gemini-api-starter

# 1. 检查并配置Git用户信息
echo "步骤 1: 配置 Git 用户信息..."
if [ -z "$(git config user.name)" ]; then
    echo "提示: Git 用户信息未配置"
    echo "使用默认配置: Lyz1116-FOUND"
    git config user.name "Lyz1116-FOUND"
    git config user.email "lyz1116@users.noreply.github.com"
else
    echo "✓ Git 用户信息已配置:"
    echo "  用户名: $(git config user.name)"
    echo "  邮箱: $(git config user.email)"
fi
echo ""

# 2. 检查是否有未提交的文件
echo "步骤 2: 检查文件状态..."
if [ -n "$(git status --porcelain)" ] || [ -z "$(git log --oneline -1 2>/dev/null)" ]; then
    echo "提交所有文件..."
    git add .
    git commit -m "Initial commit: Google Gemini 3 Flash API 入门项目

- 使用 Gemini 3 Flash 模型
- 交互式命令行对话
- 包含多个使用示例
- 适合AI专业大二学生学习" || echo "文件已提交或无需提交"
    echo "✓ 文件已提交"
else
    echo "✓ 所有文件已提交"
fi
echo ""

# 3. 确保分支名为 main
echo "步骤 3: 检查分支名称..."
current_branch=$(git branch --show-current 2>/dev/null || echo "master")
if [ "$current_branch" != "main" ]; then
    git branch -M main 2>/dev/null || true
    echo "✓ 分支已重命名为 main"
else
    echo "✓ 分支名称正确: main"
fi
echo ""

# 4. 检查远程仓库
echo "步骤 4: 检查远程仓库配置..."
if git remote | grep -q "^origin$"; then
    remote_url=$(git remote get-url origin)
    echo "✓ 远程仓库已配置: $remote_url"
else
    echo "配置远程仓库..."
    git remote add origin https://github.com/Lyz1116-FOUND/gemini-api-starter.git
    echo "✓ 远程仓库已添加"
fi
echo ""

# 5. 提示用户创建GitHub仓库
echo "=========================================="
echo "⚠️  重要提示"
echo "=========================================="
echo ""
echo "在推送之前，请先在 GitHub 上创建仓库："
echo ""
echo "1. 访问: https://github.com/new"
echo "2. Repository name: gemini-api-starter"
echo "3. Description: Google Gemini 3 Flash API 入门项目 - 适合AI专业大二学生"
echo "4. Visibility: 选择 Public 或 Private"
echo "5. ⚠️  不要勾选任何初始化选项（README, .gitignore, license）"
echo "6. 点击 'Create repository'"
echo ""
read -p "按 Enter 键继续（确保已创建仓库）..."

# 6. 尝试推送
echo ""
echo "步骤 5: 推送代码到 GitHub..."
echo ""

# 尝试普通推送
if git push -u origin main 2>&1; then
    echo ""
    echo "=========================================="
    echo "✓ 成功推送到 GitHub！"
    echo "=========================================="
    echo ""
    echo "仓库地址: https://github.com/Lyz1116-FOUND/gemini-api-starter"
    echo ""
    exit 0
fi

# 如果推送失败，尝试拉取合并
echo ""
echo "远程仓库可能已有内容，尝试拉取并合并..."
if git pull origin main --allow-unrelated-histories --no-edit 2>&1; then
    echo ""
    echo "再次推送..."
    if git push -u origin main 2>&1; then
        echo ""
        echo "=========================================="
        echo "✓ 成功推送到 GitHub！"
        echo "=========================================="
        echo ""
        echo "仓库地址: https://github.com/Lyz1116-FOUND/gemini-api-starter"
        echo ""
        exit 0
    fi
fi

echo ""
echo "=========================================="
echo "推送失败"
echo "=========================================="
echo ""
echo "可能的原因:"
echo "1. GitHub 仓库尚未创建"
echo "2. 认证失败（需要使用 Personal Access Token）"
echo "3. 网络连接问题"
echo ""
echo "请按照以下步骤操作:"
echo ""
echo "1. 确保已在 GitHub 创建仓库:"
echo "   https://github.com/new"
echo ""
echo "2. 如果遇到认证问题，创建 Personal Access Token:"
echo "   https://github.com/settings/tokens"
echo "   - 选择 'Generate new token (classic)'"
echo "   - 勾选 'repo' 权限"
echo "   - 推送时使用 Token 作为密码"
echo ""
echo "3. 手动推送命令:"
echo "   git push -u origin main"
echo ""

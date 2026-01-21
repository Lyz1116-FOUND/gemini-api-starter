#!/bin/bash
# GitHub 发布脚本
# 使用方法: ./publish_to_github.sh

echo "=========================================="
echo "GitHub 发布助手"
echo "=========================================="
echo ""

# 检查是否在项目目录
if [ ! -f "main.py" ]; then
    echo "错误: 请在项目根目录运行此脚本"
    exit 1
fi

# 步骤 1: 初始化 Git 仓库
if [ ! -d ".git" ]; then
    echo "步骤 1: 初始化 Git 仓库..."
    git init
    echo "✓ Git 仓库初始化完成"
else
    echo "✓ Git 仓库已存在"
fi

# 步骤 2: 添加文件
echo ""
echo "步骤 2: 添加文件到暂存区..."
git add .
echo "✓ 文件已添加"

# 步骤 3: 检查是否有未提交的更改
if git diff --cached --quiet; then
    echo "提示: 没有新的更改需要提交"
else
    echo ""
    echo "步骤 3: 提交更改..."
    read -p "请输入提交信息 (默认: Initial commit): " commit_msg
    commit_msg=${commit_msg:-"Initial commit: Gemini 3 Flash API 入门项目"}
    git commit -m "$commit_msg"
    echo "✓ 更改已提交"
fi

# 步骤 4: 检查远程仓库
echo ""
echo "步骤 4: 检查远程仓库配置..."
if git remote | grep -q "^origin$"; then
    echo "✓ 远程仓库已配置:"
    git remote -v
else
    echo "提示: 尚未配置远程仓库"
    echo ""
    read -p "请输入你的 GitHub 用户名: " github_username
    read -p "请输入仓库名称 (默认: gemini-api-starter): " repo_name
    repo_name=${repo_name:-"gemini-api-starter"}

    echo ""
    echo "配置远程仓库..."
    git remote add origin "https://github.com/$github_username/$repo_name.git"
    echo "✓ 远程仓库已配置"
fi

# 步骤 5: 检查分支
current_branch=$(git branch --show-current 2>/dev/null || echo "main")
if [ -z "$current_branch" ]; then
    git branch -M main
    current_branch="main"
fi

# 步骤 6: 推送到 GitHub
echo ""
echo "步骤 5: 推送到 GitHub..."
echo "分支: $current_branch"
echo ""
echo "⚠️  如果这是第一次推送，请确保:"
echo "   1. 已在 GitHub 上创建了仓库"
echo "   2. 已准备好 Personal Access Token"
echo ""
read -p "是否现在推送？(y/n): " confirm
if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
    git push -u origin $current_branch
    echo ""
    echo "=========================================="
    echo "✓ 推送完成！"
    echo "=========================================="
else
    echo ""
    echo "可以稍后使用以下命令推送:"
    echo "  git push -u origin $current_branch"
fi

echo ""
echo "完成！查看详细指南: cat GITHUB_SETUP.md"

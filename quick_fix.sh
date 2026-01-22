#!/bin/bash
echo "=========================================="
echo "Git 推送错误修复脚本"
echo "=========================================="
echo ""

# 检查 Git 配置
if [ -z "$(git config user.name)" ]; then
    echo "提示: Git 用户信息未配置"
    read -p "请输入你的名字: " git_name
    read -p "请输入你的邮箱: " git_email
    git config user.name "$git_name"
    git config user.email "$git_email"
    echo "✓ Git 用户信息已配置"
fi

# 提交更改
if [ -n "$(git status --porcelain)" ] || [ -z "$(git log --oneline -1 2>/dev/null)" ]; then
    echo ""
    echo "提交本地更改..."
    git commit -m "Initial commit: Gemini 3 Flash API 入门项目"
    echo "✓ 更改已提交"
fi

# 重命名分支为 main
current_branch=$(git branch --show-current)
if [ "$current_branch" != "main" ]; then
    echo ""
    echo "将分支从 $current_branch 重命名为 main..."
    git branch -M main
    echo "✓ 分支已重命名"
fi

echo ""
echo "=========================================="
echo "准备推送..."
echo "=========================================="
echo ""
echo "请选择推送方式:"
echo "1. 普通推送（如果远程仓库为空）"
echo "2. 先拉取再推送（如果远程仓库有内容）"
echo "3. 强制推送（会覆盖远程内容）"
echo ""
read -p "请选择 (1/2/3): " choice

case $choice in
    1)
        echo ""
        echo "推送中..."
        git push -u origin main
        ;;
    2)
        echo ""
        echo "拉取远程更改..."
        git pull origin main --allow-unrelated-histories
        echo ""
        echo "推送中..."
        git push -u origin main
        ;;
    3)
        echo ""
        read -p "⚠️  确定要强制推送吗？这会覆盖远程内容 (y/n): " confirm
        if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
            git push -u origin main --force
        else
            echo "已取消"
        fi
        ;;
    *)
        echo "无效选择"
        ;;
esac

echo ""
echo "完成！"

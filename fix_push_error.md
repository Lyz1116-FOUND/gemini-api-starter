# 解决 Git 推送错误

## 错误原因
`error: failed to push some refs to 'https://github.com/...'`

这个错误通常是因为：
1. 远程仓库有本地没有的提交（比如创建仓库时初始化了 README）
2. 分支名称不匹配（远程是 main，本地是 master）
3. Git 用户信息未配置

## 解决步骤

### 步骤 1: 配置 Git 用户信息

```bash
cd /home/lyz/gemini-api-starter

# 配置全局用户信息（推荐）
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"

# 或者仅配置当前仓库
git config user.name "你的名字"
git config user.email "你的邮箱@example.com"
```

### 步骤 2: 提交本地更改

```bash
# 提交所有文件
git commit -m "Initial commit: Gemini 3 Flash API 入门项目"
```

### 步骤 3: 处理分支名称问题

**方案 A: 将本地分支重命名为 main（推荐）**

```bash
# 重命名当前分支为 main
git branch -M main

# 推送
git push -u origin main
```

**方案 B: 如果远程仓库已经有内容，先拉取再合并**

```bash
# 允许不相关的历史合并
git pull origin main --allow-unrelated-histories

# 如果有冲突，解决冲突后
git add .
git commit -m "Merge remote-tracking branch 'origin/main'"

# 推送
git push -u origin main
```

**方案 C: 强制推送（仅当远程仓库是空的或你可以覆盖时使用）**

```bash
git branch -M main
git push -u origin main --force
```

⚠️ **警告**: `--force` 会覆盖远程仓库的内容，只在确定安全时使用！

### 步骤 4: 如果遇到认证问题

如果提示需要用户名和密码：

1. **使用 Personal Access Token 代替密码**
   - 创建 Token: https://github.com/settings/tokens
   - 权限：勾选 `repo`
   - 推送时：
     - 用户名：你的 GitHub 用户名
     - 密码：使用生成的 Token（不是 GitHub 密码）

2. **或使用 SSH 方式**（推荐）

```bash
# 移除 HTTPS 远程地址
git remote remove origin

# 添加 SSH 地址
git remote add origin git@github.com:Lyz1116-FOUND/gemini-api-starter.git

# 推送
git push -u origin main
```

## 完整操作示例

```bash
# 1. 配置 Git（只需要第一次）
git config --global user.name "你的名字"
git config --global user.email "your.email@example.com"

# 2. 提交更改
cd /home/lyz/gemini-api-starter
git commit -m "Initial commit: Gemini 3 Flash API 入门项目"

# 3. 重命名分支
git branch -M main

# 4. 推送（使用 Personal Access Token 作为密码）
git push -u origin main
```

## 常见错误及解决

### 错误: "Updates were rejected"
**原因**: 远程仓库有本地没有的提交
**解决**:
```bash
git pull origin main --allow-unrelated-histories
# 解决冲突后
git push -u origin main
```

### 错误: "Permission denied"
**原因**: 认证失败
**解决**: 使用 Personal Access Token 代替密码

### 错误: "remote origin already exists"
**原因**: 远程仓库已配置
**解决**:
```bash
git remote remove origin
git remote add origin https://github.com/Lyz1116-FOUND/gemini-api-starter.git
```

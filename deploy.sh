#!/bin/bash

# 获取当前时间作为默认提交信息
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
COMMIT_MSG="Update: $TIMESTAMP"

# 如果用户提供了提交信息，则使用用户提供的
if [ ! -z "$1" ]; then
  COMMIT_MSG="$1"
fi

echo "🚀 开始同步代码到 GitHub..."
echo "📝 提交信息: $COMMIT_MSG"

# 执行 git 命令
git add .
git commit -m "$COMMIT_MSG"
git push origin main

echo "✅ 代码已推送到 GitHub！"
echo "⚡️ Vercel 将在几秒钟内自动触发部署，请稍候刷新您的网站。"

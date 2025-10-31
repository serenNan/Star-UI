#!/bin/bash
# Star-UI 本地开发服务器启动脚本

echo "🚀 Star-UI 开发服务器启动中..."
echo ""
echo "📂 工作目录: $(pwd)"
echo "🌐 访问地址: http://localhost:8000"
echo ""
echo "按 Ctrl+C 停止服务器"
echo "----------------------------------------"
echo ""

# 启动 Python HTTP 服务器
python3 -m http.server 8000 || python -m http.server 8000

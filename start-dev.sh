#!/bin/bash
# Star-UI Development Server

echo "🚀 Star-UI Development Mode"
echo "=========================================="
echo ""

# Build the project
echo "🔨 Building index.html..."
python3 build.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Build failed! Please check the errors above."
    exit 1
fi

echo ""
echo "=========================================="
echo ""
echo "🌐 Starting development server..."
echo "📂 Working directory: $(pwd)"
echo "🔗 Visit: http://localhost:8000"
echo ""
echo "💡 Tip: Edit files in sections/ then run 'python3 build.py' to rebuild"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=========================================="
echo ""

# Start Python HTTP server
python3 -m http.server 8000 || python -m http.server 8000

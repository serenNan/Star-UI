#!/usr/bin/env python3
"""
Build all pages (index.html and solutions.html)
"""
import sys
from pathlib import Path

# 添加 tools 目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from build import build


def build_all():
    """构建所有页面"""
    print("=" * 60)
    print("🔨 Building All Pages...")
    print("=" * 60)
    print("")

    # 构建 Solutions 页面
    print("📄 Building Solutions Page (solutions.html)...")
    print("-" * 60)
    success2 = build("tools/build.solutions.config.json")
    print("")

    # 总结
    print("=" * 60)
    if success2:
        print("✅ All pages built successfully!")
        print("   • solutions.html (Solutions page)")
    else:
        print("⚠️  Some pages failed to build:")
        if not success2:
            print("   ❌ solutions.html")
    print("=" * 60)

    return success2


if __name__ == "__main__":
    success = build_all()
    exit(0 if success else 1)

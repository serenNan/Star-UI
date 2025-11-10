#!/usr/bin/env python3
"""
Build Create page (create.html)
"""
import sys
from pathlib import Path

# 添加 tools 目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from build import build


def build_create():
    """构建 Create 页面"""
    print("=" * 60)
    print("🔨 Building Create Page...")
    print("=" * 60)
    print("")

    # 构建 Create 页面
    print("📄 Building Create Page (create.html)...")
    print("-" * 60)
    success = build("tools/build.create.config.json")
    print("")

    # 总结
    print("=" * 60)
    if success:
        print("✅ Create page built successfully!")
        print("   • create.html (Create page)")
    else:
        print("❌ Create page failed to build")
    print("=" * 60)

    return success


if __name__ == "__main__":
    success = build_create()
    exit(0 if success else 1)


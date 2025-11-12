#!/usr/bin/env python3
"""
Build Explore page (explore.html)
"""
import sys
from pathlib import Path

# 添加 tools 目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from build import build


def build_explore():
    """构建 Explore 页面"""
    print("=" * 60)
    print("🔨 Building Explore Page...")
    print("=" * 60)
    print("")

    # 构建 Explore 页面
    print("📄 Building Explore Page (explore.html)...")
    print("-" * 60)
    success = build("tools/build.explore.config.json")
    print("")

    # 总结
    print("=" * 60)
    if success:
        print("✅ Explore page built successfully!")
        print("   • explore.html (Explore page)")
    else:
        print("❌ Explore page failed to build")
    print("=" * 60)

    return success


if __name__ == "__main__":
    success = build_explore()
    exit(0 if success else 1)

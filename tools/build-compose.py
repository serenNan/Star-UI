#!/usr/bin/env python3
"""
Build Compose page (compose.html)
"""
import sys
from pathlib import Path

# 添加 tools 目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from build import build


def build_compose():
    """构建 Compose 页面"""
    print("=" * 60)
    print("🔨 Building Compose Page...")
    print("=" * 60)
    print("")

    # 构建 Compose 页面
    print("📄 Building Compose Page (compose.html)...")
    print("-" * 60)
    success = build("tools/build.compose.config.json")
    print("")

    # 总结
    print("=" * 60)
    if success:
        print("✅ Compose page built successfully!")
        print("   • compose.html (Compose page)")
    else:
        print("❌ Compose page failed to build")
    print("=" * 60)

    return success


if __name__ == "__main__":
    success = build_compose()
    exit(0 if success else 1)


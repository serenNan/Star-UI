#!/usr/bin/env python3
"""
Build all pages (index.html, solutions.html, compose.html, create.html)
统一构建脚本，可以构建所有页面
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

    # 定义所有需要构建的页面配置
    pages = [
        {
            "name": "Index",
            "config": "tools/build.config.json",
            "output": "index.html",
            "description": "Main page"
        },
        {
            "name": "Solutions",
            "config": "tools/build.solutions.config.json",
            "output": "solutions.html",
            "description": "Solutions page"
        },
        {
            "name": "Compose",
            "config": "tools/build.compose.config.json",
            "output": "compose.html",
            "description": "Compose page"
        },
        {
            "name": "Create",
            "config": "tools/build.create.config.json",
            "output": "create.html",
            "description": "Create page"
        }
    ]

    results = []
    
    # 构建每个页面
    for page in pages:
        print(f"📄 Building {page['name']} Page ({page['output']})...")
        print("-" * 60)
        success = build(page['config'])
        results.append({
            "name": page['name'],
            "output": page['output'],
            "success": success
        })
        print("")

    # 总结
    print("=" * 60)
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]
    
    if successful:
        print("✅ Successfully built pages:")
        for r in successful:
            print(f"   • {r['output']} ({r['name']} page)")
    
    if failed:
        print("")
        print("❌ Failed to build pages:")
        for r in failed:
            print(f"   • {r['output']} ({r['name']} page)")
    
    print("=" * 60)
    print(f"📊 Summary: {len(successful)}/{len(results)} pages built successfully")
    print("=" * 60)
    
    return len(failed) == 0


if __name__ == "__main__":
    success = build_all()
    exit(0 if success else 1)


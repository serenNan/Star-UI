#!/usr/bin/env python3
"""
Star-UI Build Script
Assembles modular sections into a single index.html file
"""
import json
import os
import subprocess
import sys
from pathlib import Path

def generate_dynamic_sections():
    """在构建前生成动态生成的区块"""
    print("🔧 Generating dynamic sections...")

    # 生成社交媒体链接
    try:
        script_path = Path(__file__).parent / 'generate-social-links.py'
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Warning: Failed to generate social links: {e.stderr}")
    except Exception as e:
        print(f"⚠️  Warning: Failed to generate social links: {str(e)}")

    print("")

def build(config_path='tools/build.config.json'):
    print("🔨 Building Star-UI...")
    print("")

    # 首先生成动态区块
    generate_dynamic_sections()

    # Read configuration
    config_file = Path(config_path)
    if not config_file.exists():
        print(f"❌ Error: {config_path} not found!")
        return False

    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # Read global head
    head_file = Path('global/head.html')
    if not head_file.exists():
        print("❌ Error: global/head.html not found!")
        return False

    with open(head_file, 'r', encoding='utf-8') as f:
        head = f.read()

    # Read global footer scripts
    footer_file = Path('global/footer-scripts.html')
    if not footer_file.exists():
        print("❌ Error: global/footer-scripts.html not found!")
        return False

    with open(footer_file, 'r', encoding='utf-8') as f:
        footer_scripts = f.read()

    # Start assembling body content
    body_parts = ['<body>\n']

    # Process each section
    sections_processed = []
    sections_missing = []

    for section in config['sections']:
        # Look for HTML file in module folder
        section_file = Path(f'sections/{section}/{section}.html')

        if section_file.exists():
            with open(section_file, 'r', encoding='utf-8') as f:
                content = f.read()
                body_parts.append(f'\n  <!-- ===== {section.upper()} SECTION ===== -->\n')
                body_parts.append(content)
                body_parts.append('\n')
            sections_processed.append(section)
            print(f"  ✅ {section}")
        else:
            sections_missing.append(section)
            print(f"  ⚠️  {section} (file not found at {section_file}, skipping)")

    # Add footer scripts
    body_parts.append('\n  <!-- ===== GLOBAL SCRIPTS ===== -->\n')
    body_parts.append(footer_scripts)

    # Combine everything
    final_html = head + ''.join(body_parts)

    # Write output file
    output_file = config['output']
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)

    # Print summary
    print("")
    print("=" * 50)
    print(f"✅ Build complete!")
    print(f"📄 Output: {output_file}")
    print(f"📦 Sections included: {len(sections_processed)}/{len(config['sections'])}")
    print("")

    if sections_processed:
        print("Included sections:")
        for s in sections_processed:
            print(f"  • {s}")

    if sections_missing:
        print("")
        print("⚠️  Missing sections (will be added later):")
        for s in sections_missing:
            print(f"  • {s}")

    print("=" * 50)
    return True

def build_all():
    """构建所有页面（主页 + Solutions 页）"""
    print("=" * 60)
    print("🔨 Building All Pages...")
    print("=" * 60)
    print("")

    # 先生成一次动态区块（避免重复生成）
    generate_dynamic_sections()

    all_success = True

    # 构建主页
    print("📄 Building Main Page (index.html)...")
    print("-" * 60)
    success1 = build_single('tools/build.config.json', skip_dynamic=True)
    print("")

    # 构建 Solutions 页面
    print("📄 Building Solutions Page (solutions.html)...")
    print("-" * 60)
    success2 = build_single('tools/build.solutions.config.json', skip_dynamic=True)
    print("")

    # 总结
    print("=" * 60)
    if success1 and success2:
        print("✅ All pages built successfully!")
        print("   • index.html (Main page)")
        print("   • solutions.html (Solutions page)")
    else:
        print("⚠️  Some pages failed to build:")
        if not success1:
            print("   ❌ index.html")
        if not success2:
            print("   ❌ solutions.html")
        all_success = False
    print("=" * 60)

    return all_success

def build_single(config_path, skip_dynamic=False):
    """构建单个页面"""
    # Read configuration
    config_file = Path(config_path)
    if not config_file.exists():
        print(f"❌ Error: {config_path} not found!")
        return False

    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # Read global head
    head_file = Path('global/head.html')
    if not head_file.exists():
        print("❌ Error: global/head.html not found!")
        return False

    with open(head_file, 'r', encoding='utf-8') as f:
        head = f.read()

    # Read global footer scripts
    footer_file = Path('global/footer-scripts.html')
    if not footer_file.exists():
        print("❌ Error: global/footer-scripts.html not found!")
        return False

    with open(footer_file, 'r', encoding='utf-8') as f:
        footer_scripts = f.read()

    # Start assembling body content
    body_parts = ['<body>\n']

    # Process each section
    sections_processed = []
    sections_missing = []

    for section in config['sections']:
        # Look for HTML file in module folder
        section_file = Path(f'sections/{section}/{section}.html')

        if section_file.exists():
            with open(section_file, 'r', encoding='utf-8') as f:
                content = f.read()
                body_parts.append(f'\n  <!-- ===== {section.upper()} SECTION ===== -->\n')
                body_parts.append(content)
                body_parts.append('\n')
            sections_processed.append(section)
            print(f"  ✅ {section}")
        else:
            sections_missing.append(section)
            print(f"  ⚠️  {section} (file not found at {section_file}, skipping)")

    # Add footer scripts
    body_parts.append('\n  <!-- ===== GLOBAL SCRIPTS ===== -->\n')
    body_parts.append(footer_scripts)

    # Combine everything
    final_html = head + ''.join(body_parts)

    # Write output file
    output_file = config['output']
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_html)

    # Print summary
    print("")
    print("=" * 50)
    print(f"✅ Build complete!")
    print(f"📄 Output: {output_file}")
    print(f"📦 Sections included: {len(sections_processed)}/{len(config['sections'])}")
    print("")

    if sections_processed:
        print("Included sections:")
        for s in sections_processed:
            print(f"  • {s}")

    if sections_missing:
        print("")
        print("⚠️  Missing sections (will be added later):")
        for s in sections_missing:
            print(f"  • {s}")

    print("=" * 50)
    return True

if __name__ == '__main__':
    success = build_all()
    exit(0 if success else 1)

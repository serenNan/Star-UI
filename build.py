#!/usr/bin/env python3
"""
Star-UI Build Script
Assembles modular sections into a single index.html file
"""
import json
import os
from pathlib import Path

def build():
    print("🔨 Building Star-UI...")
    print("")

    # Read configuration
    config_file = Path('build.config.json')
    if not config_file.exists():
        print("❌ Error: build.config.json not found!")
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
    success = build()
    exit(0 if success else 1)

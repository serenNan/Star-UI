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

PAGES = [
    {
        "key": "index",
        "name": "Index",
        "config": "tools/build.config.json",
        "output": "index.html",
        "description": "Main page",
    },
    {
        "key": "explore",
        "name": "Explore",
        "config": "tools/build.explore.config.json",
        "output": "explore.html",
        "description": "Explore page",
    },
    {
        "key": "solutions",
        "name": "Solutions",
        "config": "tools/build.solutions.config.json",
        "output": "solutions.html",
        "description": "Solutions page",
    },
    {
        "key": "compose",
        "name": "Compose",
        "config": "tools/build.compose.config.json",
        "output": "compose.html",
        "description": "Compose page",
    },
    {
        "key": "create",
        "name": "Create",
        "config": "tools/build.create.config.json",
        "output": "create.html",
        "description": "Create page",
    },
]


def generate_dynamic_sections():
    """在构建前生成动态生成的区块"""
    print("[gen] Generating dynamic sections...")

    # 生成社交媒体链接
    try:
        script_path = Path(__file__).parent / "generate-social-links.py"
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            check=True,
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"[warn] Failed to generate social links: {e.stderr}")
    except Exception as e:
        print(f"[warn] Failed to generate social links: {str(e)}")

    print("")


def build(config_file_path=None, *, run_dynamic=True):
    print("[build] Building Star-UI...")
    print("")

    # 首先生成动态区块
    if run_dynamic:
        generate_dynamic_sections()
    else:
        print(
            "[build] Skipping dynamic section generation (already run in this session).\n"
        )

    # Read configuration
    if config_file_path is None:
        config_file = Path("tools/build.config.json")
    else:
        config_file = Path(config_file_path)
    if not config_file.exists():
        print(f"[error] {config_file} not found!")
        return False

    with open(config_file, "r", encoding="utf-8") as f:
        config = json.load(f)

    # Read global head
    head_file = Path("global/head.html")
    if not head_file.exists():
        print("[error] global/head.html not found!")
        return False

    with open(head_file, "r", encoding="utf-8") as f:
        head = f.read()

    # Read global footer scripts
    footer_file = Path("global/footer-scripts.html")
    if not footer_file.exists():
        print("[error] global/footer-scripts.html not found!")
        return False

    with open(footer_file, "r", encoding="utf-8") as f:
        footer_scripts = f.read()

    # Start assembling body content
    body_class = config.get("bodyClass", "").strip()
    body_attr = f' class="{body_class}"' if body_class else ""
    body_parts = [f"<body{body_attr}>\n"]

    # Process each section
    sections_processed = []
    sections_missing = []

    for section in config["sections"]:
        # Look for HTML file in module folder
        section_file = Path(f"sections/{section}/{section}.html")

        if section_file.exists():
            with open(section_file, "r", encoding="utf-8") as f:
                content = f.read()
                body_parts.append(
                    f"\n  <!-- ===== {section.upper()} SECTION ===== -->\n"
                )
                body_parts.append(content)
                body_parts.append("\n")
            sections_processed.append(section)
            print(f"  [ok] {section}")
        else:
            sections_missing.append(section)
            print(f"  [skip] {section} (file not found at {section_file}, skipping)")

    # Add footer scripts
    body_parts.append("\n  <!-- ===== GLOBAL SCRIPTS ===== -->\n")
    body_parts.append(footer_scripts)

    # Combine everything
    final_html = head + "".join(body_parts)

    # Write output file
    output_file = config["output"]
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    # Print summary
    print("")
    print("=" * 50)
    print("[done] Build complete!")
    print(f"[out] {output_file}")
    print(f"[sections] {len(sections_processed)}/{len(config['sections'])}")
    print("")

    if sections_processed:
        print("Included sections:")
        for s in sections_processed:
            print(f"  - {s}")

    if sections_missing:
        print("")
        print("[warn] Missing sections (will be added later):")
        for s in sections_missing:
            print(f"  - {s}")

    print("=" * 50)
    return True


def build_all(page_keys=None):
    """构建预设的多个页面。"""
    if page_keys:
        key_set = {k.lower() for k in page_keys}
        pages = [p for p in PAGES if p["key"] in key_set]
        missing = key_set - {p["key"] for p in pages}
        if missing:
            print("[error] Unknown page keys:", ", ".join(sorted(missing)))
            return False
    else:
        pages = PAGES

    if not pages:
        print("[warn] No pages selected for build.")
        return True

    print("=" * 60)
    print("[build] Building Selected Pages...")
    print("=" * 60)
    print("")

    results = []
    for idx, page in enumerate(pages):
        print(f"[build] {page['name']} -> {page['output']} ...")
        print("-" * 60)
        success = build(page["config"], run_dynamic=(idx == 0))
        results.append(
            {"name": page["name"], "output": page["output"], "success": success}
        )
        print("")

    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]

    print("=" * 60)
    if successful:
        print("[done] Successfully built pages:")
        for r in successful:
            print(f"   - {r['output']} ({r['name']} page)")
    if failed:
        print("\n[error] Failed to build pages:")
        for r in failed:
            print(f"   - {r['output']} ({r['name']} page)")
    print("=" * 60)
    print(f"[summary] {len(successful)}/{len(results)} pages built successfully")
    print("=" * 60)

    return len(failed) == 0


if __name__ == "__main__":
    success = build_all()
    sys.exit(0 if success else 1)

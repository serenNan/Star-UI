#!/usr/bin/env python3
"""
Update resource paths in module HTML files
Changes: assets/images/file.ext -> sections/module/file.ext
         assets/videos/file.ext -> sections/module/file.ext
"""
import re
from pathlib import Path

# Resource mappings for each module (flat structure, no subdirectories)
RESOURCE_MAPPINGS = {
    'navigation': {
        'assets/images/logo.svg': 'sections/navigation/logo.svg'
    },
    'hero': {
        'assets/images/hero-1.jpg': 'sections/hero/hero-1.svg',
        'assets/images/hero-2.jpg': 'sections/hero/hero-2.svg',
        'assets/images/featured-video.jpg': 'sections/hero/featured-video.svg',
        'assets/videos/hero-1.mp4': 'sections/hero/hero-1.mp4',
        'assets/videos/hero-2.mp4': 'sections/hero/hero-2.mp4',
        'assets/videos/featured.mp4': 'sections/hero/featured.mp4'
    },
    'gallery': {
        'assets/images/gallery-1.jpg': 'sections/gallery/gallery-1.svg',
        'assets/images/gallery-2.jpg': 'sections/gallery/gallery-2.svg',
        'assets/images/gallery-3.jpg': 'sections/gallery/gallery-3.svg',
        'assets/images/gallery-4.jpg': 'sections/gallery/gallery-4.svg',
        'assets/images/gallery-5.jpg': 'sections/gallery/gallery-5.svg',
        'assets/images/gallery-6.jpg': 'sections/gallery/gallery-6.svg',
        'assets/videos/gallery-1.mp4': 'sections/gallery/gallery-1.mp4',
        'assets/videos/gallery-2.mp4': 'sections/gallery/gallery-2.mp4',
        'assets/videos/gallery-3.mp4': 'sections/gallery/gallery-3.mp4',
        'assets/videos/gallery-4.mp4': 'sections/gallery/gallery-4.mp4',
        'assets/videos/gallery-5.mp4': 'sections/gallery/gallery-5.mp4',
        'assets/videos/gallery-6.mp4': 'sections/gallery/gallery-6.mp4'
    },
    'features': {
        'assets/images/feature-1.jpg': 'sections/features/feature-1.svg',
        'assets/images/feature-2.jpg': 'sections/features/feature-2.svg',
        'assets/images/feature-3.jpg': 'sections/features/feature-3.svg',
        'assets/images/feature-4.jpg': 'sections/features/feature-4.svg'
    },
    'footer': {
        'assets/images/logo.svg': 'sections/footer/logo.svg'
    }
}

def update_module_paths(module_name):
    """Update resource paths in a module's HTML file"""
    html_file = Path(f'sections/{module_name}/{module_name}.html')

    if not html_file.exists():
        print(f"⚠️  {module_name}.html not found, skipping")
        return False

    # Read file content
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get mappings for this module
    mappings = RESOURCE_MAPPINGS.get(module_name, {})

    if not mappings:
        print(f"  ℹ️  {module_name} has no resource mappings")
        return True

    # Replace all paths
    updated = False
    changes_made = 0
    for old_path, new_path in mappings.items():
        if old_path in content:
            content = content.replace(old_path, new_path)
            changes_made += 1
            updated = True

    if updated:
        # Write updated content
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {module_name} - updated {changes_made} paths")
    else:
        print(f"  ℹ️  {module_name} - no paths needed updating")

    return True

def main():
    print("🔄 Updating resource paths in module files...")
    print("")

    modules = ['navigation', 'hero', 'gallery', 'stats', 'features', 'cta', 'footer']

    total_changes = 0
    for module in modules:
        result = update_module_paths(module)
        if result:
            total_changes += 1

    print("")
    print("=" * 50)
    print("✅ Resource path updates complete!")
    print("")
    print("Next steps:")
    print("1. Run: python3 build.py")
    print("2. Open index.html in browser to verify")
    print("=" * 50)

if __name__ == '__main__':
    main()

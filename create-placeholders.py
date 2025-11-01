#!/usr/bin/env python3
"""
创建占位符图片和视频文件
为每个模块生成所需的占位符资源
"""
import os
from pathlib import Path

# 定义每个模块需要的资源
RESOURCES = {
    'navigation': {
        'images': ['logo.svg']
    },
    'hero': {
        'images': ['hero-1.jpg', 'hero-2.jpg', 'featured-video.jpg'],
        'videos': ['hero-1.mp4', 'hero-2.mp4', 'featured.mp4']
    },
    'gallery': {
        'images': ['gallery-1.jpg', 'gallery-2.jpg', 'gallery-3.jpg',
                   'gallery-4.jpg', 'gallery-5.jpg', 'gallery-6.jpg'],
        'videos': ['gallery-1.mp4', 'gallery-2.mp4', 'gallery-3.mp4',
                   'gallery-4.mp4', 'gallery-5.mp4', 'gallery-6.mp4']
    },
    'features': {
        'images': ['feature-1.jpg', 'feature-2.jpg', 'feature-3.jpg', 'feature-4.jpg']
    },
    'footer': {
        'images': ['logo.svg']
    }
}

def create_placeholder_image(filepath):
    """创建占位符图片（SVG格式）"""
    filename = Path(filepath).stem
    svg_content = f'''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="600" fill="#1a1a1a"/>
  <text x="50%" y="50%" font-family="Arial" font-size="24" fill="#666" text-anchor="middle">
    {filename}
  </text>
  <text x="50%" y="55%" font-family="Arial" font-size="14" fill="#444" text-anchor="middle">
    Placeholder Image
  </text>
</svg>'''

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"  ✅ Created placeholder: {filepath}")

def create_placeholder_video(filepath):
    """创建占位符视频的说明文件"""
    filename = Path(filepath).stem
    placeholder_path = filepath.replace('.mp4', '.placeholder.txt')

    content = f"""This is a placeholder for: {filename}.mp4

To add the actual video:
1. Place your video file at: {filepath}
2. Recommended specs:
   - Format: MP4 (H.264)
   - Duration: 5-10 seconds
   - Resolution: 1000x1000 or similar
   - Bitrate: 5-8 Mbps
   - Audio: Muted (not required)

The video will auto-play on hover (desktop) or be visible on mobile.
"""

    with open(placeholder_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  📝 Created video placeholder note: {placeholder_path}")

def main():
    print("🎨 Creating placeholder resources for each module...")
    print()

    for module, resources in RESOURCES.items():
        print(f"📦 Module: {module}")

        # Create images
        if 'images' in resources:
            for image in resources['images']:
                image_path = f"sections/{module}/images/{image}"
                os.makedirs(os.path.dirname(image_path), exist_ok=True)

                if image.endswith('.svg'):
                    create_placeholder_image(image_path)
                else:
                    # For JPG, create SVG placeholder with JPG extension
                    create_placeholder_image(image_path.replace('.jpg', '.svg'))
                    print(f"  ℹ️  Note: Created SVG placeholder for {image}")

        # Create video placeholders
        if 'videos' in resources:
            for video in resources['videos']:
                video_path = f"sections/{module}/videos/{video}"
                os.makedirs(os.path.dirname(video_path), exist_ok=True)
                create_placeholder_video(video_path)

        print()

    print("=" * 60)
    print("✅ Placeholder creation complete!")
    print()
    print("📝 Next steps:")
    print("1. Replace placeholder images/videos with actual files")
    print("2. Update module HTML files to use new paths")
    print("3. Run build.py to regenerate index.html")
    print("=" * 60)

if __name__ == '__main__':
    main()

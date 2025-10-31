# Assets Checklist for TreClip

This checklist helps you track which assets you've added to the project.

## 📁 Directory Setup

- [ ] `assets/images/` folder exists
- [ ] `assets/videos/` folder exists
- [ ] `assets/fonts/` folder exists (optional)

## 🖼️ Images Required

### Brand Assets
- [ ] `assets/images/logo.svg` - Site logo (SVG format)
- [ ] `assets/images/favicon.png` - Browser favicon (32x32 or 64x64)

### Hero Section (400x600 portrait)
- [ ] `assets/images/hero-1.jpg` - Hero gallery image 1
- [ ] `assets/images/hero-2.jpg` - Hero gallery image 2
- [ ] `assets/images/hero-3.jpg` - Hero gallery image 3
- [ ] `assets/images/panel-video.jpg` - Right panel video thumbnail (800x450)

### Product Gallery (1000x1000 square)
- [ ] `assets/images/gallery-1.jpg` - Product showcase 1
- [ ] `assets/images/gallery-2.jpg` - Product showcase 2
- [ ] `assets/images/gallery-3.jpg` - Product showcase 3
- [ ] `assets/images/gallery-4.jpg` - Product showcase 4
- [ ] `assets/images/gallery-5.jpg` - Product showcase 5
- [ ] `assets/images/gallery-6.jpg` - Product showcase 6

### Features Section (800x450 landscape)
- [ ] `assets/images/feature-1.jpg` - AI-Powered Generation
- [ ] `assets/images/feature-2.jpg` - Smart Editing Tools
- [ ] `assets/images/feature-3.jpg` - Brand Consistency
- [ ] `assets/images/feature-4.jpg` - Premium Templates
- [ ] `assets/images/feature-5.jpg` - Performance Analytics
- [ ] `assets/images/feature-6.jpg` - One-Click Export

## 🎬 Videos Required

### Hero Section (5-10 second loops)
- [ ] `assets/videos/hero-1.mp4` - Hero gallery video 1
- [ ] `assets/videos/hero-2.mp4` - Hero gallery video 2
- [ ] `assets/videos/hero-3.mp4` - Hero gallery video 3
- [ ] `assets/videos/panel-video.mp4` - Right panel featured video (10-15 sec)

### Product Gallery (5-10 second loops)
- [ ] `assets/videos/gallery-1.mp4` - Product video 1
- [ ] `assets/videos/gallery-2.mp4` - Product video 2
- [ ] `assets/videos/gallery-3.mp4` - Product video 3
- [ ] `assets/videos/gallery-4.mp4` - Product video 4
- [ ] `assets/videos/gallery-5.mp4` - Product video 5
- [ ] `assets/videos/gallery-6.mp4` - Product video 6

## 📊 Asset Summary

**Total Images Needed**: 18
- Brand: 2
- Hero: 4
- Gallery: 6
- Features: 6

**Total Videos Needed**: 10
- Hero: 4
- Gallery: 6

## 🎨 Quick Asset Generation Tips

### Using Placeholder Images

If you don't have assets yet, use these placeholder services:

1. **Unsplash Source**
   ```html
   <img src="https://source.unsplash.com/400x600/?space,astronaut" alt="Hero 1">
   ```

2. **Placeholder.com**
   ```html
   <img src="https://via.placeholder.com/1000x1000/0D0D0D/FFFFFF?text=Gallery+1" alt="Gallery 1">
   ```

### Creating Simple Placeholder Videos

```bash
# Create a 5-second black video with text (requires ffmpeg)
ffmpeg -f lavfi -i color=c=black:s=1000x1000:d=5 \
  -vf "drawtext=text='Video Placeholder':fontsize=60:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2" \
  -pix_fmt yuv420p placeholder.mp4
```

## ✅ Verification

Once all assets are in place, verify:

```bash
# Check images
ls -lh assets/images/

# Check videos
ls -lh assets/videos/

# Start server and test
python -m http.server 8000
```

Then open http://localhost:8000 and check:
- [ ] Logo displays correctly
- [ ] All images load
- [ ] Videos play on hover
- [ ] No broken image icons
- [ ] No 404 errors in console

## 🔧 Optimization

Before going live, optimize your assets:

### Images
```bash
# Using ImageMagick
mogrify -strip -quality 85 assets/images/*.jpg

# Using OptiPNG
optipng -o7 assets/images/*.png
```

### Videos
```bash
# Using FFmpeg
ffmpeg -i input.mp4 -vcodec h264 -b:v 6M -an output.mp4
```

## 📝 Notes

- Keep source files in a separate folder (not in assets)
- Commit optimized versions only
- Update this checklist as you add assets
- Test on mobile devices after adding all assets

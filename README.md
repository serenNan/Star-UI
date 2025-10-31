# TreClip - AI Video Creation Platform

A modern, clean landing page for an AI-powered short-form video creation platform. Design based on professional mockup with dark theme and minimalist aesthetic.

## 📁 Project Structure

```
Star-UI/
├── index.html           # Main landing page
├── css/
│   ├── normalize.css    # CSS reset
│   ├── webflow.css      # Webflow base styles
│   └── treclip.css      # Custom TreClip styles ⭐
├── js/
│   ├── webflow.js       # Webflow interactions
│   └── star-ui.js       # Custom interactions
├── assets/              # Media assets folder
│   ├── videos/          # Video files
│   ├── images/          # Image files
│   └── fonts/           # Font files (optional)
├── README.md            # This file
└── CLAUDE.md            # Development guide
```

## 🎨 Page Sections

1. **Navigation** - Fixed header with logo and menu
2. **Hero Section** - Large title "AI SHORT-FORM VIDEOS, DESIGNED LIKE ART" with image gallery
3. **Hero Right Panel** - Featured video and creation tools
4. **Product Gallery** - Masonry grid showcasing video examples
5. **Stats** - Key metrics (300K users, 5M+ videos, etc.)
6. **Features** - 6 feature cards with visuals
7. **CTA** - Call-to-action section
8. **Footer** - Complete site map and links

## 🎯 Design Features

### Modern Dark Theme
- Background: `#0D0D0D` (near black)
- Secondary: `#1A1A1A` (dark gray)
- Text: White with various opacity levels
- Minimal use of color accent

### Typography
- Font: Inter (Google Fonts)
- Large, bold headings
- Clean, readable body text
- Letter-spacing for emphasis

### Interactions
- Hover effects on all videos (image → video transition)
- Smooth animations on scroll
- Card hover elevations
- Button transformations

## 🚀 Quick Start

### Local Development

```bash
# Navigate to project
cd /home/serennan/work/Star-UI

# Start local server (Option 1)
python -m http.server 8000

# Or use npx (Option 2)
npx serve

# Or use the start script
./start-server.sh

# Open in browser
http://localhost:8000
```

### Deploy

The site is static HTML/CSS/JS and can be deployed to:
- **Netlify** - Drag and drop folder
- **Vercel** - Connect GitHub repo
- **GitHub Pages** - Push to gh-pages branch
- **Cloudflare Pages** - One-click deployment

## 🎬 Asset Requirements

### Images Needed

Place in `assets/images/`:

| Filename | Purpose | Dimensions | Format |
|----------|---------|------------|--------|
| `logo.svg` | Site logo | Scalable | SVG |
| `favicon.png` | Browser icon | 32x32 or 64x64 | PNG |
| `hero-1.jpg` | Hero gallery item 1 | 400x600 | JPG/PNG |
| `hero-2.jpg` | Hero gallery item 2 | 400x600 | JPG/PNG |
| `hero-3.jpg` | Hero gallery item 3 | 400x600 | JPG/PNG |
| `panel-video.jpg` | Right panel video thumbnail | 800x450 | JPG/PNG |
| `gallery-1.jpg` to `gallery-6.jpg` | Product showcase | 1000x1000 | JPG/PNG |
| `feature-1.jpg` to `feature-6.jpg` | Feature visuals | 800x450 | JPG/PNG |

### Videos Needed

Place in `assets/videos/`:

| Filename | Purpose | Recommended Length |
|----------|---------|-------------------|
| `hero-1.mp4` to `hero-3.mp4` | Hero gallery videos | 5-10 sec loop |
| `panel-video.mp4` | Featured video | 10-15 sec |
| `gallery-1.mp4` to `gallery-6.mp4` | Product videos | 5-10 sec loop |

### Video Specifications

- **Format**: MP4 (H.264)
- **Bitrate**: 5-8 Mbps
- **FPS**: 24-30
- **Audio**: Muted (not required)
- **Optimization**: Use HandBrake or FFmpeg to compress

#### FFmpeg Compression Example

```bash
ffmpeg -i input.mp4 -vcodec h264 -b:v 6M -s 1000x1000 -an output.mp4
```

## 🎨 Customization

### Change Colors

Edit `css/treclip.css` `:root` variables:

```css
:root {
  --color-bg: #0D0D0D;           /* Main background */
  --color-bg-secondary: #1A1A1A; /* Cards/sections */
  --color-text: #FFFFFF;         /* Primary text */
  --color-text-secondary: #A0A0A0; /* Secondary text */
  --color-accent: #FF3366;       /* Accent color */
}
```

### Update Content

All text is in `index.html`. Search for the section you want to edit:

```html
<!-- Example: Change hero title -->
<h1 class="hero-title">
  YOUR NEW TITLE HERE
</h1>
```

### Add/Remove Sections

Each section is clearly marked:

```html
<!-- ===== Section Name ===== -->
...content...
<!-- End of section -->
```

Simply copy/paste/delete entire sections as needed.

## 📱 Responsive Breakpoints

- **Desktop**: ≥ 1200px (3-column hero, full features)
- **Tablet**: 992px - 1199px (2-column layouts)
- **Mobile Large**: 768px - 991px (simplified nav)
- **Mobile**: < 768px (single column, stacked)

## 🔧 Technical Stack

- **HTML5** - Semantic markup
- **CSS3** - Grid, Flexbox, CSS Variables
- **JavaScript (ES6+)** - Interactions and animations
- **Lenis** - Smooth scrolling library
- **Inter Font** - Google Fonts typography

## 🌐 Browser Support

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)
- ❌ Internet Explorer (not supported)

## 🐛 Troubleshooting

### Videos Don't Auto-play?

- Ensure videos are muted (`muted` attribute)
- Use local server (not `file://` protocol)
- Check browser autoplay policies

### Layout Looks Broken?

- Clear browser cache (Ctrl+Shift+R)
- Check that CSS file is loading (Network tab)
- Verify container widths in DevTools

### Images Not Loading?

- Check file paths are correct
- Verify files exist in `assets/images/`
- Check file permissions

### Mobile Menu Not Working?

- Ensure JavaScript is enabled
- Check browser console for errors
- Verify `star-ui.js` is loading

## 📝 Content Guidelines

### Hero Section
- Title: 3-4 words, bold and impactful
- Subtitle: One sentence explaining value proposition
- CTA: Clear action verb ("Start creating", "Explore now")

### Features
- Title: 3-5 words
- Description: 1-2 sentences
- Include visual for each feature

### Gallery
- Use high-quality images
- Consistent aspect ratios
- Include overlay titles

## 🔄 Updates from Original Version

This is a **complete rewrite** based on the PDF mockup:

**Changed:**
- ✅ English language (was Chinese)
- ✅ Dark modern theme (was cosmic purple theme)
- ✅ TreClip branding (was Star-UI)
- ✅ PDF-accurate layout
- ✅ Minimalist aesthetic
- ✅ Professional copywriting

**Kept:**
- ✅ Video hover-to-play functionality
- ✅ Smooth scroll animations
- ✅ Responsive design
- ✅ Modular code structure

## 📄 License

For demonstration and learning purposes.

---

**Version**: 2.0.0
**Last Updated**: 2025-10-31
**Design Based On**: TreClip PDF Mockup

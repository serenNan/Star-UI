# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

Star-UI 是一个现代化的 AI 视频创作平台落地页（TreClip），采用静态 HTML + CSS + JavaScript 架构。主题为宇宙、太空和未来科技，设计风格简洁专业。

**设计理念**：简洁为主，不要过于花哨。参考网站：
- https://www.florafauna.ai/
- https://www.freepik.com/

**核心特性**：
- 暗色主题设计（近黑背景 + 宇宙配色）
- 视频悬浮自动播放（无控制按钮）
- 平滑滚动动画（Lenis 库）
- 完全响应式（桌面端/平板/移动端）
- 模块化代码组织（HTML/CSS/JS 就近放置）

## 项目结构

```
Star-UI/
├── index.html               # 主落地页
├── css/
│   ├── normalize.css        # CSS 重置
│   ├── webflow.css          # Webflow 基础样式
│   ├── treclip.css          # TreClip 原始样式（参考）
│   └── star-ui.css          # ⭐ 主要样式文件（宇宙主题）
├── js/
│   ├── webflow.js           # Webflow 交互库
│   └── star-ui.js           # ⭐ 主要交互逻辑
├── assets/
│   ├── images/              # 图片资源（logo、缩略图等）
│   ├── videos/              # 视频资源（悬浮播放）
│   └── fonts/               # 字体文件（如需自定义）
├── 要求/
│   └── 要求.md              # 原始需求文档
├── README.md                # 项目说明和资源清单
├── ASSETS-CHECKLIST.md      # 资源准备检查清单
└── start-server.sh          # 本地服务器启动脚本
```

**注意**：`要求/TreClip/` 目录包含旧版代码（含 Supabase 集成），当前实际使用的是根目录文件。

## 核心技术栈

- **前端**：原生 HTML5/CSS3/ES6+ JavaScript
- **动画库**：Lenis (平滑滚动) - CDN 加载
- **字体**：Inter (Google Fonts)
- **视频**：HTML5 `<video>` 标签，悬浮触发播放
- **响应式**：CSS Grid/Flexbox + Media Queries

## 开发工作流

### 本地开发服务器

```bash
# 方式 1：使用启动脚本（推荐）
./start-server.sh

# 方式 2：Python HTTP 服务器
python3 -m http.server 8000

# 方式 3：npx serve
npx serve

# 访问地址
http://localhost:8000
```

**重要**：必须使用 HTTP 服务器，不要直接用 `file://` 打开 HTML，否则视频自动播放会失效。

### 修改样式

主要样式文件：`css/star-ui.css`

```css
/* 修改配色 */
:root {
  --space-black: #0a0e27;      /* 主背景色 */
  --cosmic-purple: #6366f1;    /* 主题紫色 */
  --cosmic-pink: #ec4899;      /* 强调粉色 */
  --star-white: #ffffff;       /* 白色文字 */
}
```

### 修改交互逻辑

主要脚本文件：`js/star-ui.js`

核心功能：
- `initSmoothScroll()` - Lenis 平滑滚动
- `initScrollAnimations()` - 滚动触发动画
- `initVideoHoverEffects()` - 视频悬浮播放
- `initMobileMenu()` - 移动端菜单

### 测试响应式

```bash
# Chrome DevTools 快捷键
F12 → Toggle Device Toolbar (Ctrl+Shift+M)

# 测试断点
- Desktop: 1200px+
- Tablet: 992px - 1199px
- Mobile: < 768px
```

## 代码组织原则

### 模块化开发（严格遵守）

**每个功能模块的 HTML、CSS、JavaScript 必须就近放置**，便于后续移动和维护。

**推荐结构示例**：

```html
<!-- ===== 导航栏模块 ===== -->
<nav class="navbar">
  <!-- HTML 结构 -->
  <div class="navbar-content">...</div>
</nav>

<style>
  /* 导航栏专用样式 */
  .navbar { ... }
  .navbar-content { ... }
</style>

<script>
  // 导航栏交互逻辑
  document.querySelector('.navbar')...
</script>
```

**当前实现**：
- HTML 结构：`index.html` 中按模块注释分隔
- CSS 样式：统一在 `css/star-ui.css`（可考虑模块化拆分）
- JavaScript：统一在 `js/star-ui.js`（已按功能函数分离）

### 视频处理规范

1. **悬浮自动播放**：
   - 使用 `data-hover-video` 属性标记容器
   - 鼠标进入 → `video.play()`
   - 鼠标离开 → `video.pause()` + 重置到开头

2. **视频要求**：
   - 必须包含 `muted` 属性（浏览器自动播放策略）
   - 必须包含 `loop` 属性（循环播放）
   - 不显示控制按钮（无 `controls` 属性）
   - 格式：MP4 (H.264)，5-10 秒短视频

3. **示例代码**：
```html
<div class="gallery-item" data-hover-video>
  <img src="assets/images/thumbnail.jpg" alt="预览图">
  <video muted loop>
    <source src="assets/videos/video.mp4" type="video/mp4">
  </video>
</div>
```

### 响应式设计原则

**移动端优先**：所有新功能必须测试移动端兼容性。

**断点策略**：
- `@media (max-width: 991px)` - 隐藏桌面菜单，显示汉堡按钮
- `@media (max-width: 767px)` - 单列布局，增大按钮尺寸
- `@media (max-width: 479px)` - 进一步缩小间距和字体

**移动端优化**：
- 增大可点击区域（最小 48x48px）
- 禁用某些悬浮效果（使用 `@media (hover: none)`）
- 触摸友好的交互设计

## 页面结构说明

### 当前页面

| 文件名 | 用途 | 状态 |
|--------|------|------|
| `index.html` | 主落地页 | ✅ 活跃 |

### 页面组成部分（index.html）

1. **Navigation** - 固定顶部导航栏
2. **Hero Section** - 主横幅区（标题 + 图片画廊）
3. **Hero Right Panel** - 右侧信息面板（特色视频）
4. **Product Gallery** - 产品展示画廊（6 个视频卡片）
5. **Stats Section** - 数据统计区（300K 用户等）
6. **Features Section** - 功能特性区（6 个功能卡片）
7. **CTA Section** - 行动号召区
8. **Footer** - 页脚（品牌/链接/社交媒体）

## 资源管理

### 图片命名规范

```
assets/images/
├── logo.svg              # 网站 Logo
├── favicon.png           # 浏览器图标
├── hero-1.jpg            # Hero 区域图片 1-3
├── panel-video.jpg       # 右侧面板视频缩略图
├── gallery-1.jpg         # 画廊图片 1-6
└── feature-1.jpg         # 功能特性图片 1-6
```

### 视频命名规范

```
assets/videos/
├── hero-1.mp4            # Hero 区域视频 1-3
├── panel-video.mp4       # 右侧面板特色视频
└── gallery-1.mp4         # 画廊视频 1-6
```

### 视频压缩建议

```bash
# 使用 FFmpeg 压缩视频
ffmpeg -i input.mp4 \
  -vcodec h264 \
  -b:v 6M \
  -s 1000x1000 \
  -an \
  output.mp4
```

参数说明：
- `-b:v 6M` - 比特率 6 Mbps
- `-s 1000x1000` - 分辨率调整
- `-an` - 移除音频（不需要）

## 常见开发任务

### 添加新区块

1. 在 `index.html` 中找到合适位置
2. 复制相似区块作为模板
3. 修改内容和类名
4. 在 `css/star-ui.css` 添加样式（如需要）
5. 在 `js/star-ui.js` 添加交互（如需要）

### 修改配色方案

编辑 `css/star-ui.css:6-18`：

```css
:root {
  /* 修改这些变量 */
  --space-black: #0a0e27;
  --cosmic-purple: #6366f1;
  --cosmic-pink: #ec4899;
  /* ...其他变量 */
}
```

### 调整滚动动画

编辑 `js/star-ui.js:46-66` 的 `initScrollAnimations()` 函数：

```javascript
const observerOptions = {
  threshold: 0.1,              // 触发阈值（0-1）
  rootMargin: '0px 0px -100px 0px'  // 触发偏移
};
```

### 调试视频播放问题

1. **检查浏览器控制台**是否有自动播放错误
2. **确认视频包含 `muted` 属性**
3. **使用 HTTP 服务器**而非 file:// 协议
4. **测试视频文件**是否可直接播放
5. **查看网络请求**是否成功加载视频

## 重要注意事项

1. **不要随意创建新文件** - 优先在现有文件基础上修改
2. **视频自动播放** - 悬停触发，无控制按钮，必须静音
3. **模块化组织** - HTML/CSS/JS 尽量就近放置
4. **移动端优先** - 所有新功能必须测试移动端兼容性
5. **简洁设计** - 避免过度装饰，保持太空主题的专业感
6. **性能优化** - 压缩视频，优化图片，减少不必要的动画

## 浏览器兼容性

**支持的浏览器**：
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ 移动浏览器（iOS Safari, Chrome Mobile）

**不支持**：
- ❌ Internet Explorer 11 及以下

## 故障排查

### 问题：视频不自动播放

**解决方案**：
1. 确保视频包含 `muted` 属性
2. 使用本地服务器而非 file:// 协议
3. 检查浏览器自动播放策略
4. 查看控制台是否有 JavaScript 错误

### 问题：布局在移动端显示异常

**解决方案**：
1. 检查 viewport meta 标签是否正确
2. 使用 Chrome DevTools 模拟移动设备
3. 检查 CSS Media Queries 断点
4. 验证容器宽度和间距设置

### 问题：平滑滚动不工作

**解决方案**：
1. 确认 Lenis CDN 链接可访问
2. 检查浏览器控制台错误
3. 验证 `initSmoothScroll()` 是否被调用
4. 测试 `requestAnimationFrame` 兼容性

### 问题：图片/视频加载失败

**解决方案**：
1. 检查文件路径是否正确（相对路径）
2. 确认文件存在于 `assets/` 目录
3. 检查文件名大小写（Linux 区分大小写）
4. 查看浏览器 Network 面板的 404 错误

## 性能优化建议

1. **图片优化**：
   - 使用 WebP 格式（fallback 到 JPG/PNG）
   - 压缩图片质量到 80-85%
   - 使用响应式图片（`<picture>` 或 `srcset`）

2. **视频优化**：
   - 压缩视频比特率（5-8 Mbps）
   - 使用短视频（5-10 秒循环）
   - 考虑懒加载（视口外的视频）

3. **CSS 优化**：
   - 移除未使用的样式
   - 合并重复的 CSS 规则
   - 使用 CSS 变量减少代码重复

4. **JavaScript 优化**：
   - 使用事件委托（减少监听器）
   - 节流/防抖滚动事件
   - 延迟加载非关键脚本

## 部署建议

### 静态托管平台

**推荐平台**：
- **Netlify** - 拖拽部署，自动 HTTPS
- **Vercel** - Git 集成，全球 CDN
- **GitHub Pages** - 免费，简单
- **Cloudflare Pages** - 高性能，免费 CDN

### 部署前检查清单

- [ ] 所有资源路径使用相对路径
- [ ] 测试所有视频能正常播放
- [ ] 验证移动端响应式布局
- [ ] 检查控制台无 JavaScript 错误
- [ ] 压缩优化图片和视频
- [ ] 测试多个浏览器兼容性
- [ ] 设置正确的 favicon.ico

### 快速部署命令

```bash
# Netlify CLI
netlify deploy --prod

# Vercel CLI
vercel --prod

# GitHub Pages
git push origin main
```

## 未来扩展方向

1. **认证系统**：集成 Supabase（参考 `要求/TreClip/` 旧代码）
2. **多页面**：添加 About、Pricing、Dashboard 等页面
3. **CMS 集成**：使用 Headless CMS 管理内容
4. **国际化**：支持多语言切换（中文/英文）
5. **深色/浅色模式切换**：添加主题切换器
6. **分析追踪**：集成 Google Analytics 或 Plausible
- 本项目的界面语言要全英
- 本项目的界面语言要全英
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
├── index.html               # ✨ 自动生成的完整页面（不要手动编辑！）
├── index.old.html           # 旧版备份文件
├── sections/                # 📦 模块化组件
│   ├── navigation.html      # 导航栏（HTML + CSS + JS）
│   ├── hero.html            # 主横幅（HTML + CSS + JS）
│   ├── gallery.html         # 产品画廊（HTML + CSS + JS）
│   ├── stats.html           # 数据统计（HTML + CSS）
│   ├── features.html        # 功能特性（HTML + CSS + JS）
│   ├── cta.html             # 行动号召（HTML + CSS）
│   └── footer.html          # 页脚（HTML + CSS）
├── global/                  # 🌍 全局资源
│   ├── head.html            # 全局头部（meta、CSS 引用）
│   ├── footer-scripts.html  # 全局脚本（Lenis、工具函数）
│   └── global.css           # 全局样式（变量、重置、工具类）
├── css/
│   ├── normalize.css        # CSS 重置
│   ├── webflow.css          # Webflow 基础样式
│   ├── treclip.css          # ✅ 主要样式文件
│   └── star-ui.css.backup   # 已废弃（旧版样式）
├── js/
│   ├── webflow.js           # Webflow 交互库
│   └── star-ui.js.backup    # 已废弃（逻辑已拆分到各模块）
├── assets/
│   ├── images/              # 图片资源
│   ├── videos/              # 视频资源
│   └── fonts/               # 字体文件
├── build.py                 # 🔨 构建脚本
├── build.config.json        # ⚙️ 构建配置
├── start-dev.sh             # 🚀 开发启动脚本
├── 要求/                    # 原始需求文档
├── README.md                # 项目说明
└── ASSETS-CHECKLIST.md      # 资源清单
```

**重要说明**：
- ✨ `index.html` 是自动生成的，修改它没有意义！
- 📦 开发时编辑 `sections/` 目录下的模块文件
- 🔨 修改后运行 `python3 build.py` 重新生成 `index.html`

## 核心技术栈

- **前端**：原生 HTML5/CSS3/ES6+ JavaScript
- **动画库**：Lenis (平滑滚动) - CDN 加载
- **字体**：Inter (Google Fonts)
- **视频**：HTML5 `<video>` 标签，悬浮触发播放
- **响应式**：CSS Grid/Flexbox + Media Queries

## 开发工作流

### 模块化开发（⭐ 重要）

**项目采用模块化架构**：每个展示区的 HTML、CSS、JavaScript 都在同一个文件中。

#### 快速开发流程

```bash
# 1. 启动开发服务器（自动构建 + 启动服务器）
./start-dev.sh

# 2. 编辑某个模块（例如修改 Hero 区域）
vim sections/hero.html

# 3. 重新构建
python3 build.py

# 4. 刷新浏览器查看效果
# 访问 http://localhost:8000
```

#### 构建系统说明

**build.py** - 自动将模块文件合并成完整的 `index.html`

```bash
# 运行构建
python3 build.py

# 构建输出示例：
# 🔨 Building Star-UI...
#   ✅ navigation
#   ✅ hero
#   ✅ gallery
#   ... (其他模块)
# ✅ Build complete!
```

**build.config.json** - 定义模块加载顺序

```json
{
  "sections": [
    "navigation",  // 导航栏
    "hero",        // 主横幅
    "gallery",     // 产品画廊
    "stats",       // 统计数据
    "features",    // 功能特性
    "cta",         // 行动号召
    "footer"       // 页脚
  ]
}
```

### 修改现有模块

每个模块文件包含 3 部分：

```html
<!-- sections/hero.html 示例 -->

<!-- 1. CSS 样式 -->
<style>
.hero { ... }
.hero-container { ... }
</style>

<!-- 2. HTML 结构 -->
<section class="hero">
  ...
</section>

<!-- 3. JavaScript 逻辑（如需要）-->
<script>
(function() {
  // 模块独立的 JS 代码
})();
</script>
```

**修改步骤**：
1. 编辑 `sections/模块名.html`
2. 运行 `python3 build.py`
3. 刷新浏览器

### 添加新模块

```bash
# 1. 创建新模块文件
cat > sections/new-section.html << 'EOF'
<style>
.new-section { ... }
</style>

<section class="new-section">
  <!-- HTML 结构 -->
</section>

<script>
// JavaScript（如需要）
</script>
EOF

# 2. 添加到构建配置
# 编辑 build.config.json，在 sections 数组中添加 "new-section"

# 3. 重新构建
python3 build.py
```

### 调整模块顺序

只需编辑 `build.config.json`，调整 `sections` 数组的顺序：

```json
{
  "sections": [
    "navigation",
    "stats",      // 移到前面
    "hero",
    "gallery",
    "features",
    "cta",
    "footer"
  ]
}
```

### 修改全局样式

**全局 CSS 变量**：编辑 `global/global.css`

```css
:root {
  --color-bg: #0D0D0D;           /* 主背景色 */
  --color-text: #FFFFFF;         /* 文字颜色 */
  --color-accent: #FF3366;       /* 强调色 */
  --container-width: 1400px;     /* 容器宽度 */
  --nav-height: 80px;            /* 导航栏高度 */
}
```

**通用工具类**：也在 `global/global.css` 中添加

```css
.container {
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 0 var(--spacing-lg);
}
```

### 本地开发服务器

```bash
# 方式 1：使用开发脚本（推荐，自动构建）
./start-dev.sh

# 方式 2：手动构建 + 启动服务器
python3 build.py && python3 -m http.server 8000

# 访问地址
http://localhost:8000
```

**重要**：必须使用 HTTP 服务器，不要直接用 `file://` 打开 HTML。

### 测试响应式

```bash
# Chrome DevTools 快捷键
F12 → Toggle Device Toolbar (Ctrl+Shift+M)

# 测试断点
- Desktop: ≥ 992px
- Tablet: 768px - 991px
- Mobile: < 768px
```

## 代码组织原则

### 模块化架构（✅ 已实现）

**每个展示区的 HTML、CSS、JavaScript 都放在同一个文件中**，实现了真正的模块化。

**实际结构**：

```
sections/
├── navigation.html    # 导航栏（所有代码在此）
├── hero.html          # Hero 区（所有代码在此）
├── gallery.html       # 画廊区（所有代码在此）
...
```

**模块文件格式**：

```html
<!-- sections/hero.html -->
<style>
/* 仅包含 Hero 区的样式 */
.hero { ... }
.hero-container { ... }
/* 响应式样式 */
@media (max-width: 991px) { ... }
</style>

<section class="hero">
  <!-- Hero 区的 HTML 结构 -->
  <div class="hero-container">...</div>
</section>

<script>
// Hero 区的交互逻辑（用 IIFE 包裹）
(function() {
  'use strict';
  // 视频悬浮播放等逻辑
})();
</script>
```

**优势**：
- ✅ **完全独立**：每个模块包含所有相关代码
- ✅ **易于移动**：调整 `build.config.json` 即可改变顺序
- ✅ **便于维护**：修改某个区块不影响其他部分
- ✅ **无需工具**：使用简单的 Python 脚本即可构建

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

## 模块列表

### 7 个核心模块

| 模块 | 文件 | 功能说明 | 交互 |
|------|------|---------|------|
| **Navigation** | `sections/navigation.html` | 固定顶部导航栏，包含 Logo、菜单、登录/注册按钮 | ✅ 移动菜单、滚动效果 |
| **Hero** | `sections/hero.html` | 主横幅区，包含大标题、画廊、右侧特色面板 | ✅ 视频悬浮播放 |
| **Gallery** | `sections/gallery.html` | 产品展示画廊（6 个视频卡片，网格布局） | ✅ 视频悬浮播放 |
| **Stats** | `sections/stats.html` | 数据统计展示（4 个统计项：300K 用户等） | 无 |
| **Features** | `sections/features.html` | 功能特性介绍（6 个功能卡片） | ✅ 滚动动画 |
| **CTA** | `sections/cta.html` | 行动号召区（标题 + 按钮） | 无 |
| **Footer** | `sections/footer.html` | 页脚（品牌信息 + 5 列链接 + 版权） | 无 |

### 模块详细说明

#### 1. Navigation（导航栏）
- **位置**：固定在页面顶部
- **内容**：Logo、5 个菜单项、Sign in/Sign up 按钮
- **交互**：
  - 移动端显示汉堡菜单
  - 滚动超过 100px 后背景加深
- **响应式**：991px 以下隐藏菜单，显示汉堡按钮

#### 2. Hero（主横幅）
- **布局**：三栏（左侧内容 + 中间画廊 + 右侧面板）
- **内容**：
  - 左侧：标题"AI SHORT-FORM VIDEOS, DESIGNED LIKE ART"、副标题、CTA 按钮
  - 中间：3 个视频卡片（垂直排列）
  - 右侧：特色视频、创作工具标签
- **交互**：所有视频支持悬浮播放
- **响应式**：991px 以下单列布局

#### 3. Gallery（产品画廊）
- **布局**：CSS Grid 3 列，支持跨行/跨列
- **内容**：6 个视频卡片，包含标题和副标题叠加层
- **交互**：悬浮显示叠加层，视频自动播放
- **响应式**：991px 以下 2 列，767px 以下 1 列

#### 4. Stats（统计数据）
- **布局**：4 列网格
- **内容**：4 个统计项（用户数、视频数、满意度、国家数）
- **样式**：大号数字 + 灰色标签
- **响应式**：991px 以下 2 列，767px 以下 1 列

#### 5. Features（功能特性）
- **布局**：2 列网格
- **内容**：6 个功能卡片，每个包含图片、标题、描述、链接
- **交互**：滚动进入视口时触发淡入动画
- **响应式**：767px 以下 1 列

#### 6. CTA（行动号召）
- **内容**：标题、副标题、2 个按钮（主按钮 + 次按钮）
- **样式**：居中对齐，渐变边框背景
- **响应式**：按钮在移动端堆叠

#### 7. Footer（页脚）
- **布局**：5 列（品牌 + 4 个链接列）
- **内容**：
  - 品牌信息、社交链接
  - Product、Resources、Company、Legal 链接列
  - 底部版权和法律链接
- **响应式**：991px 以下 2 列，767px 以下 1 列

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
- 本项目的界面语言要全英，注释可中文
- 回答我请使用中文回答，只是网站展示界面是英文，注释也使用中文
- 构建的脚本文件在tools文件夹下
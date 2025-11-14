# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 快速开始

```bash
# 启动开发服务器（自动构建 + 启动 HTTP 服务器）
./start-dev.sh

# 或手动构建
python3 tools/build.py

# 访问网站
# http://localhost:8000 - 主页
# http://localhost:8000/explore.html - 探索页
# http://localhost:8000/solutions.html - 解决方案页
```

**⚠️ 重要提示**:
- ✨ 不要手动编辑生成的 HTML 文件（index.html, explore.html 等）
- 📝 所有修改都应在 `sections/` 目录下的模块文件中进行
- 🔨 修改后必须运行 `python3 tools/build.py` 重新构建

## 项目概述

Star-UI 是一个现代化的 AI 视频创作平台落地页（TreClip），采用静态 HTML + CSS + JavaScript 架构，使用**模块化构建系统**。主题为宇宙、太空和未来科技，设计风格简洁专业。

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
│   ├── navigation/          # 导航栏模块
│   ├── banner/              # 主横幅模块
│   ├── links/               # 🆕 社交媒体链接（自动生成）
│   ├── gallery/             # 产品画廊模块
│   ├── stats/               # 数据统计模块
│   ├── features/            # 功能特性模块
│   ├── cta/                 # 行动号召模块
│   └── footer/              # 页脚模块
├── global/                  # 🌍 全局资源
│   ├── head.html            # 全局头部（meta、CSS 引用）
│   ├── footer-scripts.html  # 全局脚本（Lenis、工具函数）
│   └── global.css           # 全局样式（变量、重置、工具类）
├── tools/                   # 🛠️ 构建工具
│   ├── build.py             # 构建脚本
│   ├── build.config.json    # 构建配置
│   ├── generate-social-links.py  # 社交链接生成器
│   ├── social-links.config.json  # 🆕 社交链接配置
│   └── README-SOCIAL-LINKS.md    # 🆕 使用说明
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

# 2. 编辑某个模块（例如修改 Banner 区域）
vim sections/banner/banner.html

# 3. 重新构建（脚本在 tools 文件夹下）
python3 tools/build.py

# 4. 刷新浏览器查看效果
# 访问 http://localhost:8000
```

#### 构建系统说明

**tools/build.py** - 自动将模块文件合并成完整的页面文件

```bash
# 构建所有页面（index.html, explore.html, solutions.html, compose.html, create.html）
python3 tools/build.py

# 构建输出示例：
# 🔨 Building Star-UI...
#   ✅ navigation
#   ✅ banner
#   ✅ links
#   ... (其他模块)
# ✅ Build complete!
```

**多页面支持**：项目支持构建多个独立页面，每个页面有自己的配置文件：
- `tools/build.config.json` → `index.html` (主页)
- `tools/build.explore.config.json` → `explore.html` (探索页)
- `tools/build.solutions.config.json` → `solutions.html` (解决方案页)
- `tools/build.compose.config.json` → `compose.html` (创作页)
- `tools/build.create.config.json` → `create.html` (制作页)

**build.config.json** - 主页模块加载顺序

```json
{
  "sections": [
    "navigation",      // 导航栏
    "banner",          // 主横幅（全屏视频背景）
    "links",           // 社交媒体链接
    "eclipses-engine", // 引擎介绍
    "compare",         // 对比区块
    "use-cases",       // 用例展示
    "workflow",        // 工作流程
    "assistant",       // AI 助手
    "styles",          // 风格展示
    "adaptation",      // 适配说明
    "APIs",            // API 介绍
    "explore_more",    // 更多探索
    "question",        // 常见问题
    "footer"           // 页脚
  ],
  "bodyClass": "page-index",
  "output": "index.html"
}
```

### 🆕 社交媒体链接配置系统

项目支持通过配置文件管理社交媒体链接,无需手动编辑 HTML。

**快速使用**:

1. 编辑 `tools/social-links.config.json`:

```json
{
  "links": [
    {
      "name": "LinkedIn",
      "url": "https://linkedin.com/company/yourcompany",
      "icon": "linkedin",
      "enabled": true
    }
  ]
}
```

2. 运行构建:

```bash
python3 tools/build.py
```

**支持的图标**: linkedin, youtube, instagram, tiktok, facebook, twitter, discord, github, reddit, spotify, twitch, pinterest

**详细文档**: 查看 `tools/README-SOCIAL-LINKS.md` 获取完整使用说明。

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
1. 编辑 `sections/模块名/模块名.html`（注意文件夹结构）
2. 运行 `python3 tools/build.py`
3. 刷新浏览器

### 添加新模块

```bash
# 1. 创建模块文件夹和文件（模块名必须与文件夹名一致）
mkdir sections/new-section
cat > sections/new-section/new-section.html << 'EOF'
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
# 编辑 tools/build.config.json，在 sections 数组中添加 "new-section"

# 3. 重新构建
python3 tools/build.py
```

### 调整模块顺序

只需编辑 `tools/build.config.json`，调整 `sections` 数组的顺序：

```json
{
  "sections": [
    "navigation",
    "banner",
    "compare",      // 移到前面
    "use-cases",
    "workflow",
    "footer"
  ],
  "bodyClass": "page-index",
  "output": "index.html"
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
# 方式 1：使用开发脚本（推荐，自动构建所有页面）
./start-dev.sh

# 方式 2：手动构建 + 启动服务器
python3 tools/build.py && python3 -m http.server 8000

# 访问地址
http://localhost:8000              # 主页
http://localhost:8000/explore.html # 探索页
http://localhost:8000/solutions.html # 解决方案页
http://localhost:8000/compose.html # 创作页
http://localhost:8000/create.html  # 制作页
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
├── navigation/
│   └── navigation.html    # 导航栏（所有代码在此）
├── banner/
│   └── banner.html        # Banner 区（所有代码在此）
├── use-cases/
│   └── use-cases.html     # 用例展示区（所有代码在此）
...
```

**模块文件格式**：

```html
<!-- sections/banner/banner.html -->
<style>
/* 仅包含 Banner 区的样式 */
.banner { ... }
.banner-container { ... }
/* 响应式样式 */
@media (max-width: 991px) { ... }
</style>

<section class="banner">
  <!-- Banner 区的 HTML 结构 -->
  <div class="banner-container">...</div>
</section>

<script>
// Banner 区的交互逻辑（用 IIFE 包裹）
(function() {
  'use strict';
  // 视频背景切换等逻辑
})();
</script>
```

**优势**：
- ✅ **完全独立**：每个模块包含所有相关代码
- ✅ **易于移动**：调整 `tools/build.config.json` 即可改变顺序
- ✅ **便于维护**：修改某个区块不影响其他部分
- ✅ **无需工具**：使用简单的 Python 脚本即可构建

**重要规范**：
- 模块文件夹名必须与模块 HTML 文件名一致（如 `sections/banner/banner.html`）
- 构建脚本会查找 `sections/{模块名}/{模块名}.html` 路径

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

## 主页模块列表

### 核心模块概览

主页 (index.html) 包含 14 个模块,按照以下顺序排列:

| 模块 | 文件 | 功能说明 | 交互 |
|------|------|---------|------|
| **Navigation** | `sections/navigation/navigation.html` | 固定顶部导航栏 | ✅ 移动菜单 |
| **Banner** | `sections/banner/banner.html` | 全屏视频背景主横幅 | ✅ 视频背景 |
| **Links** | `sections/links/links.html` | 社交媒体链接（自动生成）| 无 |
| **Eclipses Engine** | `sections/eclipses-engine/eclipses-engine.html` | AI 引擎介绍 | ✅ 视频播放 |
| **Compare** | `sections/compare/compare.html` | 对比展示区 | 无 |
| **Use Cases** | `sections/use-cases/use-cases.html` | 应用场景展示 | ✅ 视频播放 |
| **Workflow** | `sections/workflow/workflow.html` | 工作流程说明 | 无 |
| **Assistant** | `sections/assistant/assistant.html` | AI 助手介绍 | 无 |
| **Styles** | `sections/styles/styles.html` | 风格展示 | ✅ 图片/视频 |
| **Adaptation** | `sections/adaptation/adaptation.html` | 自适应功能 | 无 |
| **APIs** | `sections/APIs/APIs.html` | API 集成说明 | 无 |
| **Explore More** | `sections/explore_more/explore_more.html` | 探索更多内容 | 无 |
| **Question** | `sections/question/question.html` | 常见问题 FAQ | ✅ 折叠面板 |
| **Footer** | `sections/footer/footer.html` | 页脚（链接+版权）| 无 |

### 其他页面

项目还包含其他独立页面：

- **explore.html**: 探索页（exp_1, exp_2, exp_3 模块）
- **solutions.html**: 解决方案页（多种解决方案展示）
- **compose.html**: 创作页（创作工具介绍）
- **create.html**: 制作页（制作流程说明）

每个页面都有自己的 `tools/build.*.config.json` 配置文件。

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

### 修改配色方案

编辑 `global/global.css` 中的 CSS 变量：

```css
:root {
  /* 修改这些变量 */
  --color-bg: #0D0D0D;
  --color-bg-secondary: #1A1A1A;
  --color-text: #FFFFFF;
  --color-accent: #FF3366;
  --color-border: #2A2A2A;
}
```

然后运行 `python3 tools/build.py` 重新构建所有页面。

### 修改某个模块的样式

1. 找到对应的模块文件（如 `sections/banner/banner.html`）
2. 编辑文件中的 `<style>` 标签内容
3. 运行 `python3 tools/build.py`
4. 刷新浏览器查看效果

### 添加新页面

1. 创建新的构建配置文件 `tools/build.newpage.config.json`
2. 指定页面使用的模块列表
3. 在 `tools/build.py` 的 `PAGES` 数组中添加页面配置
4. 运行构建脚本生成新页面

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

## 开发规范

- **界面语言**: 网站展示界面使用全英文
- **代码注释**: 注释使用中文
- **沟通语言**: 与开发者沟通使用中文
- **构建脚本位置**: `tools/` 文件夹下
- **修改后必做**: 改完代码后必须运行 `python3 tools/build.py` 重新构建所有页面
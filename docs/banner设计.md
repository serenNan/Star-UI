# Banner 重新设计实施方案

## 📋 项目信息

- **设计目标**：完全按照参考图片重新设计首屏 Banner 区域
- **设计主题**：宇宙、太空、宇航员
- **设计风格**：简洁专业，不过度花哨
- **参考图片**：`要求/banner.png`

---

## 🎯 设计确认

### 用户需求确认

| 项目 | 选择 |
|------|------|
| **右下角视频卡片交互** | 需要悬浮播放（鼠标悬浮时图片淡出，视频自动播放） |
| **中间宇航员视觉** | 静态图片 + CSS 动画效果（漂浮、光效） |
| **右侧描述文本** | 保留并完整显示创意视频描述 |
| **保留元素** | ✨ AI-Powered 徽章、副标题文字、Get Started 按钮、创作工具标签、Logo (images/logo.jpg) |

---

## 🏗️ 布局结构设计

### 整体布局（桌面端 ≥ 992px）

```
┌─────────────────────────────────────────────────────────────┐
│  Navigation Bar (固定顶部)                                    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │              │  │              │  │  描述文本     │      │
│  │  左侧内容区   │  │  宇航员图片   │  │  + 工具标签   │      │
│  │  (40%)       │  │  (40%)       │  │  (20%)       │      │
│  │              │  │              │  │              │      │
│  │  - Logo徽章  │  │  [太空人]     │  │  创意描述...  │      │
│  │  - 主标题    │  │              │  │              │      │
│  │  - 副标题    │  │  CSS动画:    │  │  工具标签:    │      │
│  │  - CTA按钮   │  │  漂浮+光效    │  │  ▪ Premiere  │      │
│  │              │  │              │  │  ▪ AfterFX   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
│                    ┌────────────────────────────────┐        │
│                    │  右下角视频预览卡片区           │        │
│                    │  ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐│        │
│                    │  │ 1 │ │ 2 │ │ 3 │ │ 4 │ │ 5 ││        │
│                    │  └───┘ └───┘ └───┘ └───┘ └───┘│        │
│                    │  AI SCROLL 标签 + 悬浮播放      │        │
│                    └────────────────────────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### 响应式布局

#### 平板端（768px - 991px）
```
┌─────────────────┐
│  左侧内容区      │
│  (全宽)         │
├─────────────────┤
│  宇航员图片      │
│  (居中显示)      │
├─────────────────┤
│  描述文本区      │
│  (全宽)         │
├─────────────────┤
│  视频卡片        │
│  ┌───┐ ┌───┐   │
│  │ 1 │ │ 2 │   │
│  └───┘ └───┘   │
│  ┌───┐ ┌───┐   │
│  │ 3 │ │ 4 │   │
│  └───┘ └───┘   │
│  ┌───┐         │
│  │ 5 │         │
│  └───┘         │
└─────────────────┘
```

#### 移动端（< 768px）
```
┌─────────────┐
│ 内容区       │
│ (全宽)      │
├─────────────┤
│ 宇航员图     │
├─────────────┤
│ 描述文本     │
├─────────────┤
│ 视频卡片     │
│ ┌─────────┐ │
│ │    1    │ │
│ └─────────┘ │
│ ┌─────────┐ │
│ │    2    │ │
│ └─────────┘ │
│     ...     │
└─────────────┘
```

---

## 📝 文件结构

### 重命名计划

```
sections/
├── hero/                    → 重命名为 → banner/
│   ├── hero.html           → 重命名为 → banner.html
│   ├── hero-1.jpg          → 保留 → astronaut-main.jpg
│   ├── hero-2.jpg          → 保留 → (备用)
│   ├── hero-1.mp4          → 保留 → (备用)
│   └── ...
```

### 新的 Banner 模块结构

**文件路径**：`sections/banner/banner.html`

**文件内容组成**：
1. `<style>` 标签：Banner 专属 CSS
2. `<section class="banner">` 标签：HTML 结构
3. `<script>` 标签：JavaScript 交互逻辑（IIFE 包裹）

---

## 🎨 设计规范

### 颜色系统（继承 global.css）

```css
--color-bg: #0D0D0D;              /* 深黑背景 */
--color-text: #FFFFFF;            /* 白色文字 */
--color-text-secondary: #A0A0A0;  /* 灰色文字 */
--color-accent: #FF3366;          /* 品红强调色 */
--color-border: #2A2A2A;          /* 边框色 */
```

### 文字内容

#### 左侧内容区

**徽章**：
```
✨ AI-Powered Video Creation
[Logo: images/logo.jpg]
```

**主标题**：
```
AI SCROLL-STOPPING VIDEOS,
DESIGNED LIKE ART
```

**副标题**（保留原有）：
```
SCROLL-STOPPING VIDEO CONTENT — REFINED,
CONSISTENT, AND BUILT TO AMPLIFY YOUR BRAND
IDENTITY.
```

**CTA 按钮**：
```
Start Creating
```

#### 右上角描述区

**描述文本**（参考图片内容）：
```
a cinematic 4k video of a lone astronaut walking slowly across
the surface of the moon under deep space darkness. the camera
orbits gently, capturing the texture of the dusty lunar ground
and the intricate folds of the astronaut's spacesuit, while
soft glimmer across the helmet visor. soft hues from earth lurking
the scene, creating a quiet, otherworldly atmosphere. the astronaut
pauses and the vast silence of space.
```

**创作工具标签**（保留原有）：
```
▪ Adobe Premiere Pro
▪ After Effects
▪ DaVinci Resolve
▪ Final Cut Pro
```

#### 右下角视频卡片

每个卡片：
- 顶部标签：`AI SCROLL`
- 缩略图：`gallery-*.jpg`
- 视频文件：`gallery-*.mp4`
- 数量：5 个卡片

---

## 🎭 交互设计

### 1. 宇航员图片动画

**动画效果**：
- **漂浮动画**：垂直方向缓慢上下移动
- **呼吸光效**：周围光晕明暗变化
- **持续时间**：6-8 秒循环

**CSS 实现**：
```css
@keyframes astronaut-float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
}

@keyframes glow-pulse {
  0%, 100% {
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
  }
  50% {
    box-shadow: 0 0 40px rgba(255, 255, 255, 0.6);
  }
}

.astronaut-image {
  animation: astronaut-float 6s ease-in-out infinite,
             glow-pulse 4s ease-in-out infinite;
}
```

### 2. 视频卡片悬浮播放

**交互流程**：
1. 初始状态：显示缩略图，视频隐藏
2. 鼠标悬浮：缩略图淡出（opacity: 0），视频淡入并播放
3. 鼠标离开：视频暂停并重置，缩略图淡入

**JavaScript 实现**：
```javascript
(function() {
  'use strict';

  // 视频悬浮播放
  const videoCards = document.querySelectorAll('[data-hover-video]');

  videoCards.forEach(card => {
    const video = card.querySelector('video');
    const thumbnail = card.querySelector('img');

    card.addEventListener('mouseenter', () => {
      thumbnail.style.opacity = '0';
      video.style.opacity = '1';
      video.play();
    });

    card.addEventListener('mouseleave', () => {
      video.pause();
      video.currentTime = 0;
      video.style.opacity = '0';
      thumbnail.style.opacity = '1';
    });
  });
})();
```

### 3. 星空背景效果

**CSS 伪元素实现**：
```css
.banner::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image:
    radial-gradient(2px 2px at 20% 30%, white, transparent),
    radial-gradient(2px 2px at 60% 70%, white, transparent),
    radial-gradient(1px 1px at 50% 50%, white, transparent);
  background-size: 200px 200px;
  opacity: 0.3;
  pointer-events: none;
}
```

---

## 📐 响应式断点

### 断点定义

| 设备类型 | 屏幕宽度 | 布局变化 |
|---------|---------|---------|
| **桌面端** | ≥ 992px | 三栏布局，5 个视频卡片水平排列 |
| **平板端** | 768px - 991px | 垂直堆叠，视频卡片 2 列网格 |
| **移动端** | < 768px | 单列布局，视频卡片 1 列垂直滚动 |

### 关键 CSS Media Queries

```css
/* 平板端 */
@media (max-width: 991px) {
  .banner-container {
    flex-direction: column;
  }

  .video-cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* 移动端 */
@media (max-width: 767px) {
  .banner-title {
    font-size: 2rem;
  }

  .video-cards-grid {
    grid-template-columns: 1fr;
  }

  .astronaut-image {
    max-width: 100%;
  }
}
```

---

## 🛠️ 实施步骤

### 步骤 1：文件重命名

```bash
# 1. 重命名目录
mv sections/hero sections/banner

# 2. 重命名 HTML 文件
mv sections/banner/hero.html sections/banner/banner.html

# 3. （可选）重命名资源文件
mv sections/banner/hero-1.jpg sections/banner/astronaut-main.jpg
```

### 步骤 2：重写 banner.html

**文件结构**：
```html
<!-- sections/banner/banner.html -->

<style>
/* ================================
   Banner 专属样式
   ================================ */

/* 1. 布局样式 */
.banner { ... }
.banner-container { ... }
.banner-left { ... }
.banner-center { ... }
.banner-right { ... }

/* 2. 文字样式 */
.banner-badge { ... }
.banner-title { ... }
.banner-subtitle { ... }

/* 3. 宇航员动画 */
@keyframes astronaut-float { ... }
@keyframes glow-pulse { ... }

/* 4. 视频卡片样式 */
.video-cards-grid { ... }
.video-card { ... }

/* 5. 响应式样式 */
@media (max-width: 991px) { ... }
@media (max-width: 767px) { ... }
</style>

<section class="banner">
  <div class="banner-container">
    <!-- 左侧内容 -->
    <div class="banner-left">
      <div class="banner-badge">
        <img src="images/logo.jpg" alt="Logo">
        ✨ AI-Powered Video Creation
      </div>
      <h1 class="banner-title">
        AI SCROLL-STOPPING VIDEOS,<br>
        DESIGNED LIKE ART
      </h1>
      <p class="banner-subtitle">...</p>
      <a href="#" class="btn-start">Start Creating</a>
    </div>

    <!-- 中间宇航员 -->
    <div class="banner-center">
      <img src="sections/banner/astronaut-main.jpg"
           alt="Astronaut"
           class="astronaut-image">
    </div>

    <!-- 右侧描述 -->
    <div class="banner-right">
      <p class="description-text">...</p>
      <div class="tools-tags">
        <span>▪ Adobe Premiere Pro</span>
        ...
      </div>
    </div>

    <!-- 右下角视频卡片 -->
    <div class="video-cards-container">
      <div class="video-cards-grid">
        <div class="video-card" data-hover-video>
          <span class="card-tag">AI SCROLL</span>
          <img src="sections/gallery/gallery-1.jpg" alt="Preview">
          <video muted loop>
            <source src="sections/gallery/gallery-1.mp4" type="video/mp4">
          </video>
        </div>
        <!-- 重复 4 次，共 5 个卡片 -->
      </div>
    </div>
  </div>
</section>

<script>
(function() {
  'use strict';

  // 视频悬浮播放逻辑
  const videoCards = document.querySelectorAll('[data-hover-video]');

  videoCards.forEach(card => {
    const video = card.querySelector('video');
    const thumbnail = card.querySelector('img');

    card.addEventListener('mouseenter', () => {
      thumbnail.style.opacity = '0';
      video.style.opacity = '1';
      video.play();
    });

    card.addEventListener('mouseleave', () => {
      video.pause();
      video.currentTime = 0;
      video.style.opacity = '0';
      thumbnail.style.opacity = '1';
    });
  });
})();
</script>
```

### 步骤 3：更新 index.html 引用

需要在 `index.html` 中找到所有引用 `hero` 的地方，替换为 `banner`：

```html
<!-- 修改前 -->
<link rel="stylesheet" href="sections/hero/hero.css">
<script src="sections/hero/hero.js"></script>

<!-- 修改后 -->
<link rel="stylesheet" href="sections/banner/banner.css">
<script src="sections/banner/banner.js"></script>
```

**注意**：如果项目使用构建脚本，需要同步更新构建配置。

### 步骤 4：测试验证

```bash
# 1. 启动本地服务器
python3 -m http.server 8000

# 2. 浏览器访问
http://localhost:8000

# 3. 测试清单
□ 桌面端布局正确（三栏）
□ 宇航员动画流畅
□ 视频卡片悬浮播放正常
□ 平板端响应式正确（2列视频）
□ 移动端响应式正确（1列视频）
□ 所有文字显示完整
□ Logo 图片加载正常
```

---

## 🎯 关键技术点

### 1. 模块化架构

- 所有代码在单一 HTML 文件中：`banner.html`
- CSS 使用 `<style>` 标签
- JavaScript 使用 IIFE 包裹避免全局污染

### 2. 视频自动播放策略

- 必须包含 `muted` 属性（浏览器策略要求）
- 必须包含 `loop` 属性（循环播放）
- 不包含 `controls` 属性（隐藏控制栏）
- 使用 JavaScript 控制播放/暂停

### 3. 性能优化

- 视频懒加载（仅悬浮时播放）
- 图片压缩（建议 < 500KB）
- CSS 动画使用 `transform`（GPU 加速）
- 避免复杂的 box-shadow（影响性能）

### 4. 浏览器兼容性

- 支持 Chrome 90+、Firefox 88+、Safari 14+
- CSS Grid 和 Flexbox 布局
- CSS 动画 `@keyframes`
- HTML5 `<video>` 元素

---

## 📦 资源清单

### 图片资源

| 文件名 | 路径 | 用途 | 尺寸建议 |
|-------|------|------|---------|
| logo.jpg | `images/logo.jpg` | 徽章 Logo | 100x100px |
| astronaut-main.jpg | `sections/banner/` | 宇航员主图 | 1000x1200px |
| gallery-1.jpg ~ gallery-5.jpg | `sections/gallery/` | 视频缩略图 | 400x400px |

### 视频资源

| 文件名 | 路径 | 用途 | 规格建议 |
|-------|------|------|---------|
| gallery-1.mp4 ~ gallery-5.mp4 | `sections/gallery/` | 悬浮播放视频 | 5-10秒，1000x1000px，6Mbps |

---

## ⚠️ 注意事项

### 开发原则

1. ✅ **不创建新文件**：只重命名和修改现有文件
2. ✅ **模块化组织**：HTML + CSS + JS 在同一文件
3. ✅ **中文注释**：代码注释使用中文
4. ✅ **英文界面**：网站展示内容使用英文
5. ✅ **使用设计系统**：继承 `global.css` 的变量

### 常见问题

**Q1：视频不自动播放？**
- 确保包含 `muted` 属性
- 使用 HTTP 服务器（不要用 file:// 协议）
- 检查浏览器控制台错误

**Q2：布局在移动端错位？**
- 检查 viewport meta 标签
- 使用 Chrome DevTools 模拟设备
- 验证 Media Queries 断点

**Q3：动画卡顿？**
- 使用 `transform` 而非 `margin/padding`
- 减少 `box-shadow` 复杂度
- 检查是否开启硬件加速

---

## 📚 参考资料

### 设计参考
- 参考图片：`要求/banner.png`
- 参考网站 1：https://www.florafauna.ai/
- 参考网站 2：https://www.freepik.com/

### 技术文档
- CSS Grid 布局：https://css-tricks.com/snippets/css/complete-guide-grid/
- HTML5 Video API：https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video
- CSS 动画性能：https://web.dev/animations/

---

## 📅 版本历史

| 版本 | 日期 | 变更说明 |
|-----|------|---------|
| v1.0 | 2025-11-02 | 初始设计方案，完整实施细节 |

---

**文档创建时间**：2025-11-02
**最后更新**：2025-11-02
**文档状态**：待实施

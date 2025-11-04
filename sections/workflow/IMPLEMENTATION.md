# Workflow 模块实现文档

## 📋 项目信息

**模块名称**: Workflow（工作流程展示）
**创建时间**: 2025-11-04
**设计参考**: `sections/workflow/workflow.png`
**状态**: 待实现

---

## 🎯 设计需求

### 用户需求确认

根据与用户的沟通，确认以下实现方案：

| 需求项 | 确定方案 |
|--------|---------|
| **背景类型** | 静态图片（后期可升级为视频） |
| **滚动动画** | 不需要（保持简洁） |
| **点击交互** | 仅悬浮效果（鼠标悬浮时卡片上移） |
| **资源准备** | 图片资源已准备好 |

### 设计稿分析

从 `workflow.png` 分析得到的设计要素：

**布局结构**:
```
┌─────────────────────────────────────────────┐
│           [WORKFLOW 小标题]                  │
│     A Seamless Creative Workflow            │
│     [副标题描述文字]                         │
│                                             │
│  ┌────┐  ┌────┐  ┌────┐  ┌────┐            │
│  │ 1  │  │ 2  │  │ 3  │  │ 4  │            │
│  │图片│  │图片│  │图片│  │图片│            │
│  │    │  │    │  │    │  │    │            │
│  │标题│  │标题│  │标题│  │标题│            │
│  │描述│  │描述│  │描述│  │描述│            │
│  └────┘  └────┘  └────┘  └────┘            │
└─────────────────────────────────────────────┘
```

**视觉特点**:
- 暗色主题背景
- 4 个竖版卡片（3:4 宽高比）
- 圆角设计（约 16px）
- 底部文字叠加层带渐变背景
- 卡片悬浮时有上移效果

---

## 📝 内容文案

### 标题区域

```yaml
小标题: "WORKFLOW"
主标题: "A Seamless Creative Workflow"
副标题: "Every step is connected through the CLIP Engine and tracked by an intelligent assistant built to enhance your process."
```

### 4 个步骤卡片

#### 1️⃣ Generative（生成）
```yaml
编号: "1"
标题: "Generative"
描述: "AI content generation powered by advanced algorithms"
图片: sections/workflow/images/1.png
```

#### 2️⃣ Storyboard（故事板）
```yaml
编号: "2"
标题: "Storyboard"
描述: "Visual planning and scene composition tools"
图片: sections/workflow/images/2.png
```

#### 3️⃣ Timeline（时间线）
```yaml
编号: "3"
标题: "Timeline"
描述: "Professional editing with precision controls"
图片: sections/workflow/images/3.png
```

#### 4️⃣ Assistant（助手）
```yaml
编号: "4"
标题: "Assistant"
描述: "Intelligent guidance throughout your creative journey"
图片: sections/workflow/images/4.png
```

---

## 🏗️ 技术实现方案

### 文件结构

```
sections/workflow/
├── workflow.html           # 主模块文件（HTML + CSS + JS）
├── workflow.png            # 设计参考图
├── IMPLEMENTATION.md       # 本文档
└── images/                 # 图片资源目录
    ├── step-1.jpg          # 步骤 1 图片
    ├── step-2.jpg          # 步骤 2 图片
    ├── step-3.jpg          # 步骤 3 图片
    └── step-4.jpg          # 步骤 4 图片
```

### CSS 类命名规范（BEM）

基于项目现有模块的分析，采用以下命名方案：

```css
/* 主容器 */
.workflow                       /* Section 容器 */

/* 标题区域 */
.workflow__header               /* 标题区域容器 */
.workflow__subtitle             /* 小标题 "WORKFLOW" */
.workflow__title                /* 主标题 */
.workflow__description          /* 副标题描述 */

/* 卡片区域 */
.workflow__cards                /* 卡片网格容器 */
.workflow__card                 /* 单个卡片 */
.workflow__card-image           /* 卡片背景图片 */
.workflow__card-overlay         /* 底部渐变叠加层 */
.workflow__card-number          /* 步骤编号 */
.workflow__card-title           /* 卡片标题 */
.workflow__card-description     /* 卡片描述 */

/* 状态类 */
.workflow__card:hover           /* 悬浮状态 */
```

### 布局方案

#### 桌面端（默认，≥ 992px）
```css
.workflow__cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;  /* var(--spacing-lg) */
}
```

#### 平板端（768px - 991px）
```css
@media (max-width: 991px) {
  .workflow__cards {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

#### 移动端（≤ 767px）
```css
@media (max-width: 767px) {
  .workflow__cards {
    grid-template-columns: 1fr;
  }
}
```

### 卡片设计规范

#### 尺寸和比例
```css
.workflow__card {
  aspect-ratio: 3 / 4;        /* 竖版比例 */
  border-radius: 16px;        /* 圆角 */
  overflow: hidden;           /* 隐藏溢出内容 */
}
```

#### 悬浮效果
```css
.workflow__card {
  transition: transform 0.3s ease;
  cursor: pointer;
}

.workflow__card:hover {
  transform: translateY(-8px);  /* 上移 8px */
}
```

#### 底部渐变叠加层
```css
.workflow__card-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 2rem;
  background: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.9) 0%,
    rgba(0, 0, 0, 0.6) 40%,
    rgba(0, 0, 0, 0.3) 70%,
    transparent 100%
  );
}
```

#### 编号样式
```css
.workflow__card-number {
  position: absolute;
  top: 1.5rem;
  left: 1.5rem;
  font-size: 3rem;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.2);  /* 半透明白色 */
  line-height: 1;
}
```

### 可用 CSS 变量

项目全局变量（定义在 `global/global.css`）：

```css
/* 颜色 */
--color-bg: #0D0D0D;              /* 主背景 */
--color-text: #FFFFFF;            /* 主文字 */
--color-text-secondary: #A0A0A0;  /* 次要文字 */

/* 间距 */
--spacing-sm: 1rem;     /* 16px */
--spacing-md: 1.5rem;   /* 24px */
--spacing-lg: 2rem;     /* 32px */
--spacing-xl: 3rem;     /* 48px */
--spacing-2xl: 4rem;    /* 64px */
--spacing-3xl: 6rem;    /* 96px */

/* 布局 */
--container-width: 1400px;

/* 动画 */
--transition: 0.3s ease;
```

---

## 💻 代码实现模板

### HTML 结构模板

```html
<section class="workflow" id="workflow">
  <div class="container">
    <!-- 标题区域 -->
    <div class="workflow__header">
      <p class="workflow__subtitle">WORKFLOW</p>
      <h2 class="workflow__title">A Seamless Creative Workflow</h2>
      <p class="workflow__description">
        Every step is connected through the CLIP Engine and tracked by an
        intelligent assistant built to enhance your process.
      </p>
    </div>

    <!-- 卡片网格 -->
    <div class="workflow__cards">
      <!-- 卡片 1: Generative -->
      <div class="workflow__card" data-step="generative">
        <img
          src="sections/workflow/images/step-1.jpg"
          alt="Generative AI"
          class="workflow__card-image"
        >
        <div class="workflow__card-number">1</div>
        <div class="workflow__card-overlay">
          <h3 class="workflow__card-title">Generative</h3>
          <p class="workflow__card-description">
            AI content generation powered by advanced algorithms
          </p>
        </div>
      </div>

      <!-- 卡片 2-4 结构类似 -->
      <!-- ... -->
    </div>
  </div>
</section>
```

### CSS 样式模板

```css
/* ========================================
   Workflow 模块样式
   ======================================== */

.workflow {
  padding: var(--spacing-3xl) 0;
  background: var(--color-bg);
}

/* 标题区域 */
.workflow__header {
  text-align: center;
  max-width: 800px;
  margin: 0 auto var(--spacing-2xl);
}

.workflow__subtitle {
  font-size: 0.875rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--color-text-secondary);
  margin-bottom: var(--spacing-sm);
}

.workflow__title {
  font-size: 3rem;
  font-weight: 700;
  line-height: 1.2;
  color: var(--color-text);
  margin-bottom: var(--spacing-md);
}

.workflow__description {
  font-size: 1.125rem;
  line-height: 1.6;
  color: var(--color-text-secondary);
}

/* 卡片网格 */
.workflow__cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--spacing-lg);
}

/* 单个卡片 */
.workflow__card {
  position: relative;
  aspect-ratio: 3 / 4;
  border-radius: 16px;
  overflow: hidden;
  cursor: pointer;
  transition: transform var(--transition);
}

.workflow__card:hover {
  transform: translateY(-8px);
}

/* 卡片图片 */
.workflow__card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 步骤编号 */
.workflow__card-number {
  position: absolute;
  top: var(--spacing-md);
  left: var(--spacing-md);
  font-size: 3rem;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.2);
  line-height: 1;
  z-index: 2;
}

/* 底部叠加层 */
.workflow__card-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: var(--spacing-lg);
  background: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.9) 0%,
    rgba(0, 0, 0, 0.6) 40%,
    rgba(0, 0, 0, 0.3) 70%,
    transparent 100%
  );
  z-index: 1;
}

.workflow__card-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: var(--spacing-sm);
}

.workflow__card-description {
  font-size: 0.875rem;
  line-height: 1.5;
  color: var(--color-text-secondary);
}

/* ========================================
   响应式设计
   ======================================== */

/* 平板端 */
@media (max-width: 991px) {
  .workflow {
    padding: var(--spacing-2xl) 0;
  }

  .workflow__title {
    font-size: 2.5rem;
  }

  .workflow__cards {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* 移动端 */
@media (max-width: 767px) {
  .workflow {
    padding: var(--spacing-xl) 0;
  }

  .workflow__header {
    margin-bottom: var(--spacing-xl);
  }

  .workflow__title {
    font-size: 2rem;
  }

  .workflow__description {
    font-size: 1rem;
  }

  .workflow__cards {
    grid-template-columns: 1fr;
    gap: var(--spacing-md);
  }

  .workflow__card {
    aspect-ratio: 3 / 3.5;  /* 稍微压缩高度 */
  }

  .workflow__card-number {
    font-size: 2.5rem;
    top: var(--spacing-sm);
    left: var(--spacing-sm);
  }

  .workflow__card-overlay {
    padding: var(--spacing-md);
  }

  .workflow__card-title {
    font-size: 1.25rem;
  }
}

/* 小屏手机 */
@media (max-width: 479px) {
  .workflow__title {
    font-size: 1.75rem;
  }

  .workflow__card-number {
    font-size: 2rem;
  }
}
```

### JavaScript 模板

```javascript
<script>
(function() {
  'use strict';

  /**
   * 初始化 Workflow 模块
   */
  const initWorkflow = () => {
    console.log('Workflow module initialized');

    const cards = document.querySelectorAll('.workflow__card');

    // 预留：未来可添加视频悬浮播放功能
    // 参考 gallery 模块的实现

    // 预留：未来可添加图片懒加载
    // cards.forEach(card => {
    //   const img = card.querySelector('.workflow__card-image');
    //   // 懒加载逻辑
    // });
  };

  // DOM Ready 检测
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initWorkflow);
  } else {
    initWorkflow();
  }
})();
</script>
```

---

## 🔧 集成构建系统

### 步骤 1: 更新构建配置

编辑 `tools/build.config.json`，在合适位置添加 `"workflow"`：

```json
{
  "sections": [
    "navigation",
    "banner",
    "links",
    "tools-showcase",
    "workflow",        // ← 新增模块
    "use-cases",
    "gallery",
    "stats",
    "features",
    "cta",
    "footer"
  ],
  "output": "index.html",
  "description": "Star-UI Build Configuration - Define section loading order"
}
```

**位置说明**: 放在 `"tools-showcase"` 之后，`"use-cases"` 之前，符合页面内容流程。

### 步骤 2: 运行构建

```bash
cd /home/serenNan/work/Star-UI/feature/workflow
python3 tools/build.py
```

预期输出：
```
🔨 Building Star-UI...
  ✅ navigation
  ✅ banner
  ✅ links
  ✅ tools-showcase
  ✅ workflow        ← 新模块
  ✅ use-cases
  ✅ gallery
  ✅ stats
  ✅ features
  ✅ cta
  ✅ footer
✅ Build complete!
```

### 步骤 3: 启动开发服务器

```bash
# 方式 1: 使用开发脚本
./start-dev.sh

# 方式 2: 手动启动
python3 -m http.server 8000
```

访问地址: `http://localhost:8000`

---

## 🎨 设计细节参考

### 参考现有模块

根据调研，以下模块可作为实现参考：

| 设计需求 | 参考模块 | 参考原因 |
|---------|---------|---------|
| 标题区域布局 | `use-cases` | 居中标题 + 副标题，相似的排版 |
| 卡片网格布局 | `features` | Grid 多列布局，响应式处理 |
| 卡片悬浮效果 | `gallery` | transform + overlay 效果 |
| 图片处理 | `gallery` | 背景图片 + 叠加层实现 |

### 视觉设计要点

1. **色彩方案**
   - 主背景: `#0D0D0D` (深黑色)
   - 文字主色: `#FFFFFF` (白色)
   - 文字副色: `#A0A0A0` (灰色)
   - 编号颜色: `rgba(255, 255, 255, 0.2)` (半透明白)

2. **间距系统**
   - Section 上下边距: `96px` (var(--spacing-3xl))
   - 标题区域下边距: `64px` (var(--spacing-2xl))
   - 卡片间距: `32px` (var(--spacing-lg))
   - 卡片内边距: `32px` (var(--spacing-lg))

3. **字体规格**
   - 主标题: `48px` / `3rem` / 粗体
   - 卡片标题: `24px` / `1.5rem` / 半粗
   - 描述文字: `14px` / `0.875rem` / 常规
   - 小标题: `14px` / `0.875rem` / 半粗 / 大写

4. **动画效果**
   - 悬浮过渡: `0.3s ease`
   - 移动距离: `-8px` (向上)

---

## 🚀 未来扩展计划

### 阶段 1: 当前实现（静态图片）
- ✅ 基础 HTML 结构
- ✅ CSS 样式和响应式
- ✅ 悬浮效果
- ✅ 构建系统集成

### 阶段 2: 视频升级
```html
<!-- 添加 data-hover-video 属性 -->
<div class="workflow__card" data-hover-video>
  <img src="..." alt="..." class="workflow__card-image">
  <video muted loop>
    <source src="sections/workflow/videos/step-1.mp4" type="video/mp4">
  </video>
  <!-- ... -->
</div>
```

```javascript
// 添加视频悬浮播放逻辑
const initVideoHover = () => {
  const videoCards = document.querySelectorAll('[data-hover-video]');

  videoCards.forEach(card => {
    const video = card.querySelector('video');
    const img = card.querySelector('img');

    if (!video) return;

    card.addEventListener('mouseenter', () => {
      img.style.opacity = '0';
      video.style.opacity = '1';
      video.play().catch(err => console.log('Video play failed:', err));
    });

    card.addEventListener('mouseleave', () => {
      video.pause();
      video.currentTime = 0;
      img.style.opacity = '1';
      video.style.opacity = '0';
    });
  });
};
```

### 阶段 3: 高级交互
- 点击卡片展开详细说明
- 添加滚动动画（IntersectionObserver）
- 卡片点击跳转到详情页

---

## ✅ 验收清单

### 功能检查
- [ ] 页面正确加载 Workflow 模块
- [ ] 4 张图片正确显示
- [ ] 所有文案内容准确无误
- [ ] 鼠标悬浮时卡片平滑上移
- [ ] 底部渐变叠加层正确显示

### 响应式检查
- [ ] 桌面端（≥992px）显示 4 列
- [ ] 平板端（768-991px）显示 2 列
- [ ] 移动端（≤767px）显示 1 列
- [ ] 小屏手机（≤479px）布局正常

### 代码质量检查
- [ ] CSS 类命名遵循 BEM 规范
- [ ] JavaScript 使用 IIFE 包裹
- [ ] 无全局变量污染
- [ ] 无 console 错误
- [ ] 图片路径正确，无 404

### 性能检查
- [ ] 图片优化（体积合理）
- [ ] CSS 无重复样式
- [ ] JavaScript 无性能问题

### 浏览器兼容性
- [ ] Chrome 90+
- [ ] Firefox 88+
- [ ] Safari 14+
- [ ] Edge 90+
- [ ] 移动浏览器（iOS Safari, Chrome Mobile）

---

## 📚 参考资料

### 项目文档
- `CLAUDE.md` - 项目总体说明
- `README.md` - 项目简介
- `tools/README-SOCIAL-LINKS.md` - 构建系统说明

### 相关模块
- `sections/banner/banner.html` - 标题区域参考
- `sections/features/features.html` - 网格布局参考
- `sections/gallery/gallery.html` - 卡片效果参考
- `sections/use-cases/use-cases.html` - 整体结构参考

### 全局资源
- `global/global.css` - CSS 变量定义
- `global/head.html` - 全局 head 标签
- `global/footer-scripts.html` - 全局脚本

### 设计资源
- `sections/workflow/workflow.png` - 设计稿

---

## 📞 联系信息

**创建者**: Claude Code
**项目路径**: `/home/serenNan/work/Star-UI/feature/workflow`
**文档版本**: 1.0
**最后更新**: 2025-11-04

---

## 🏁 开始实施

准备好后，按以下顺序执行：

1. 确认图片资源已放置在 `sections/workflow/images/` 目录
2. 创建 `sections/workflow/workflow.html` 文件
3. 复制本文档中的 HTML/CSS/JS 模板到该文件
4. 更新 `tools/build.config.json`
5. 运行 `python3 tools/build.py`
6. 启动开发服务器测试
7. 根据验收清单逐项检查

**祝开发顺利！** 🎉

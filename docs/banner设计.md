# Banner 重新设计实施方案

## 📋 项目信息

- **设计目标**：完全按照参考图片重新设计首屏 Banner 区域
- **设计主题**：宇宙、太空、宇航员
- **设计风格**：简洁专业，不过度花哨
- **参考图片**：参考图 #2（宇航员全屏背景）

---

## ⚠️ 设计要求（2025-11-02 最新）

### 1. 宇航员图片 → 全屏背景
- ❌ 删除独立的 `<img>` 元素和中间宇航员区域
- ✅ 改为使用 CSS `background-image` 覆盖整个 Banner 区域
- ❌ 删除所有动画效果（漂浮动画和光效动画）
- ✅ 添加深色渐变遮罩层确保文字可读性

### 2. Start Creating 按钮样式
- ❌ 删除品红色背景
- ✅ 改为白色背景 + 黑色文字

### 3. 描述文本框背景
- ❌ 删除白色半透明背景
- ✅ 改为灰色半透明背景（带毛玻璃效果）

### 4. 视频卡片位置和布局（重要！）
- ❌ 删除底部全宽横向排列
- ✅ 改为右下角绝对定位
- ✅ **严格要求**：5个卡片**水平排列成一行，绝对不换行**
- ✅ 使用 `display: flex` 而非 `grid`
- ✅ 设置 `flex-wrap: nowrap` 禁止换行

### 5. 布局结构
```
┌─────────────────────────────────────────────────┐
│  [宇航员全屏背景图 - 覆盖整个区域]               │
│  [深色渐变遮罩层]                                │
│                                                 │
│  ┌─────────────┐           ┌────────────────┐  │
│  │ Logo徽章     │           │ 描述文本框      │  │
│  │ 主标题       │           │ (灰色背景)     │  │
│  │ 副标题       │           │ + 工具标签     │  │
│  │ Start        │           └────────────────┘  │
│  │ Creating     │                               │
│  │ (白色背景)   │                               │
│  └─────────────┘                               │
│                                                 │
│                        ┌───┐┌───┐┌───┐┌───┐┌──┐│
│                        │ 1 ││ 2 ││ 3 ││ 4 ││5 ││
│                        └───┘└───┘└───┘└───┘└──┘│
│                        (右下角，水平排列不换行)  │
└─────────────────────────────────────────────────┘
```

---

## 🎯 设计确认

| 项目 | 要求 |
|------|------|
| **宇航员背景** | 全屏背景图，无动画 |
| **视频卡片位置** | 右下角水平排列（不换行） |
| **视频卡片交互** | 悬浮播放（鼠标悬浮时图片淡出，视频自动播放） |
| **描述文本框** | 灰色半透明背景 + 毛玻璃效果 |
| **Start Creating 按钮** | 白色背景 + 黑色文字 |
| **保留元素** | ✨ AI-Powered 徽章、副标题文字、创作工具标签、Logo (images/logo.jpg) |

---

## 📝 文字内容

### 左侧内容区

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

**副标题**：
```
SCROLL-STOPPING VIDEO CONTENT — REFINED,
CONSISTENT, AND BUILT TO AMPLIFY YOUR BRAND
IDENTITY.
```

**CTA 按钮**：
```
Start Creating
```

### 右上角描述区

**描述文本**：
```
A cinematic 4K video of a lone astronaut walking slowly across
the surface of the moon under deep space darkness. The camera
orbits gently, capturing the texture of the dusty lunar ground
and the intricate folds of the astronaut's spacesuit, while
soft glimmer across the helmet visor. Soft hues from earth lurking
the scene, creating a quiet, otherworldly atmosphere. The astronaut
pauses and the vast silence of space.
```

**创作工具标签**：
```
▪ Adobe Premiere Pro
▪ After Effects
▪ DaVinci Resolve
▪ Final Cut Pro
```

### 右下角视频卡片

每个卡片：
- 顶部标签：`AI SCROLL`
- 缩略图：`sections/gallery/gallery-*.jpg`
- 视频文件：`sections/gallery/gallery-*.mp4`
- 数量：5 个卡片，水平排列成一行

---

## 📐 响应式设计

### 桌面端（≥ 992px）
- 左侧内容区浮在背景上
- 右上角描述文本框
- 右下角 5 个视频卡片水平排列

### 平板端（768px - 991px）
- 垂直堆叠所有内容
- 视频卡片可以 2 列网格或横向滚动

### 移动端（< 768px）
- 单列布局
- 视频卡片 1 列或横向滚动

---

## 📦 资源文件

### 必需资源
- `images/logo.jpg` - Logo 徽章
- `sections/banner/astronaut-main.jpg` - 宇航员背景图
- `sections/gallery/gallery-1.jpg ~ gallery-5.jpg` - 视频缩略图
- `sections/gallery/gallery-1.mp4 ~ gallery-5.mp4` - 视频文件

---

## ⚠️ 注意事项

1. ✅ **不创建新文件**：只修改现有 `sections/banner/banner.html`
2. ✅ **模块化组织**：HTML + CSS + JS 在同一文件
3. ✅ **中文注释**：代码注释使用中文
4. ✅ **英文界面**：网站展示内容使用英文
5. ✅ **视频卡片不换行**：严格水平排列成一行

---

**文档创建时间**：2025-11-02
**最后更新**：2025-11-02
**文档状态**：待实施

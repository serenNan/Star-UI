# 项目文档

## 📖 项目简介

本项目是一个模块化的网站项目，采用组件化设计理念，通过独立的模块（Sections）实现灵活的页面组合和快速的页面构建。每个模块都是自包含的，包括其样式（CSS）、结构（HTML）和交互逻辑（JavaScript）。

## 📁 目录结构

```
Star-UI/
├── assets/                      # 静态资源目录
│   ├── banner/                 # Banner 模块资源（图片、视频）
│   ├── compare/                # 比较模块资源
│   ├── footer/                 # Footer 模块资源
│   ├── styles/                 # 样式模块资源
│   └── ...                     # 其他模块对应的资源目录
│
├── sections/                    # 页面模块目录（核心）
│   ├── banner/                 # 首页横幅模块
│   │   └── banner.html        # 包含 HTML、CSS、JS
│   ├── navigation/             # 导航栏模块
│   ├── footer/                 # 页尾模块
│   ├── compare/                # 视频对比展示模块
│   ├── eclipses-engine/        # 工具展示模块
│   ├── styles/                 # 风格卡片展示模块
│   ├── workflow_cmps/          # 工作流组件模块
│   ├── ai_creative_suite/      # AI 创意套件模块
│   ├── ai_solutions/           # AI 解决方案模块
│   ├── APIs/                   # APIs 介绍模块
│   ├── assistant/              # 助手功能模块
│   ├── brand-control/          # 品牌控制模块
│   ├── built_for_speed/        # 性能展示模块
│   ├── use-cases/              # 使用案例模块
│   ├── question/               # FAQ 模块
│   └── ...                     # 其他功能模块
│
├── global/                      # 全局配置
│   ├── head.html               # 全局 <head> 标签内容
│   ├── global.css              # 全局 CSS 样式
│   └── footer-scripts.html     # 全局页脚脚本
│
├── css/                         # 基础样式库
│   ├── normalize.css           # CSS 重置样式
│   ├── webflow.css             # Webflow 基础样式
│   └── treclip.css             # 项目主题样式
│
├── docs/                        # 文档目录
├── tools/                       # 工具脚本
├── feature/                     # 功能特性
│
├── index.html                   # 主页
├── compose.html                 # Compose 页面
├── create.html                  # Create 页面
├── explore.html                 # Explore 页面
├── solutions.html               # Solutions 页面
│
└── README.md                    # 本文档
```

## 🧩 模块说明

### 核心模块类型

每个 Section 模块通常包含以下结构：

```html
<!-- sections/example/example.html -->

<!-- ===================================
     模块名称
     模块功能描述
     =================================== -->

<style>
  /* 模块专属样式 */
  .module-class {
    /* CSS 规则 */
  }
</style>

<!-- HTML 结构 -->
<section class="module-class" id="moduleId">
  <!-- 模块内容 -->
</section>

<!-- JavaScript 交互逻辑 -->
<script>
  (function () {
    'use strict';
    // 模块初始化代码
  })();
</script>
```

### 常用模块列表

| 模块名称 | 目录路径 | 功能描述 | 资源目录 |
|---------|---------|---------|---------|
| **Navigation** | `sections/navigation/` | 顶部导航栏，包含 Logo、菜单、CTA 按钮 | `assets/navigation/` |
| **Banner** | `sections/banner/` | 首页横幅，包含背景视频、标题、卡片动画 | `assets/banner/` |
| **Compare** | `sections/compare/` | 视频对比展示，支持左右对比滑块 | `assets/compare/` |
| **Eclipses Engine** | `sections/eclipses-engine/` | 工具展示，支持卡片切换、滚动缩放 | `assets/eclipses-engine/` |
| **Styles** | `sections/styles/` | 风格卡片画廊，旋转布局、悬浮视频 | `assets/styles/` |
| **Workflow** | `sections/workflow_cmps/` | 工作流程展示 | `assets/workflow_cmps/` |
| **AI Creative Suite** | `sections/ai_creative_suite/` | AI 创意工具介绍 | `assets/ai_creative_suite/` |
| **APIs** | `sections/APIs/` | API 功能介绍 | `assets/APIs/` |
| **Footer** | `sections/footer/` | 页脚，包含链接、社交图标、背景视频 | `assets/footer/` |
| **FAQ** | `sections/question/` | 常见问题解答 | - |


## 🎯 最佳实践

### 模块设计原则

1. **独立性**：每个模块应该是自包含的，不依赖于其他模块
2. **可复用性**：模块应该能在不同页面中复用

### 性能优化建议

1. **懒加载资源**
   ```html
   <img src="placeholder.jpg" data-src="real-image.jpg" loading="lazy">
   <video preload="none">...</video>
   ```

2. **CSS 变量**：使用 CSS 自定义属性便于主题定制
   ```css
   :root {
     --color-bg: #000000;
     --color-text: #FFFFFF;
     --spacing-md: 2rem;
   }
   ```

3. **响应式设计**：每个模块都应该包含响应式样式
   ```css
   @media (max-width: 991px) { /* 平板 */ }
   @media (max-width: 767px) { /* 移动端 */ }
   @media (max-width: 479px) { /* 小屏手机 */ }
   ```

## 🔧 构建系统

### 构建脚本说明

项目使用 Python 构建脚本（`tools/build.py`）来自动组装模块并生成完整的 HTML 页面。

#### 主要功能

1. **自动读取配置文件**：根据 JSON 配置文件指定的模块顺序组装页面
2. **动态生成内容**：自动生成社交媒体链接等动态内容
3. **批量构建**：一次性构建所有页面（index、compose、create、explore、solutions）
4. **错误提示**：清晰显示构建过程和缺失的模块

### 配置文件结构

每个页面对应一个配置文件，位于 `tools/` 目录：

| 配置文件 | 对应页面 | 说明 |
|---------|---------|------|
| `build.config.json` | `index.html` | 主页配置 |
| `build.compose.config.json` | `compose.html` | Compose 页面配置 |
| `build.create.config.json` | `create.html` | Create 页面配置 |
| `build.explore.config.json` | `explore.html` | Explore 页面配置 |
| `build.solutions.config.json` | `solutions.html` | Solutions 页面配置 |

#### 配置文件格式

```json
{
  "sections": [
    "navigation",
    "banner",
    "compare",
    "footer"
  ],
  "bodyClass": "page-index",
  "output": "index.html",
  "description": "主页构建配置"
}
```

**字段说明：**
- `sections`：模块加载顺序，决定页面内容的排列
- `bodyClass`：添加到 `<body>` 标签的 CSS 类名（可选）
- `output`：输出的 HTML 文件名
- `description`：配置文件描述（可选）

### 如何使用构建系统

#### 方法一：构建所有页面（推荐）

```bash
# 在项目根目录执行
python tools/build.py
```

这会自动构建所有 5 个页面：
- index.html
- compose.html
- create.html
- explore.html
- solutions.html

#### 方法二：单独构建某个页面

```bash
# 构建主页
python tools/build.py --config tools/build.config.json

# 构建 Compose 页面
python tools/build.py --config tools/build.compose.config.json
```

### 构建流程

1. **生成动态内容**
   - 运行 `generate-social-links.py` 生成社交媒体链接
   - 其他动态生成的模块

2. **读取配置文件**
   - 加载指定的 JSON 配置
   - 获取模块列表和页面设置

3. **组装页面**
   - 读取 `global/head.html`（全局头部）
   - 按配置顺序加载各个模块
   - 添加 `global/footer-scripts.html`（全局脚本）

4. **输出结果**
   - 生成完整的 HTML 文件
   - 显示构建摘要和警告

### 构建输出示例

```
[build] Building Star-UI...

[gen] Generating dynamic sections...
  [ok] Social links generated

[build] Index -> index.html ...
  [ok] navigation
  [ok] banner
  [ok] links
  [ok] compare
  [skip] new-module (file not found, skipping)
  [ok] footer

==================================================
[done] Build complete!
[out] index.html
[sections] 5/6

Included sections:
  - navigation
  - banner
  - links
  - compare
  - footer

[warn] Missing sections (will be added later):
  - new-module
==================================================
```

## 📝 修改页面的完整流程

### 步骤 1：选择要修改的页面

找到对应的配置文件：
- **主页** → `tools/build.config.json`
- **Compose** → `tools/build.compose.config.json`
- **Create** → `tools/build.create.config.json`
- **Explore** → `tools/build.explore.config.json`
- **Solutions** → `tools/build.solutions.config.json`

### 步骤 2：编辑配置文件

打开配置文件，修改 `sections` 数组来调整模块顺序或添加/删除模块。

**示例：在主页添加新模块**

```json
{
  "sections": [
    "navigation",
    "banner",
    "links",
    "my-new-module",    // 新添加的模块
    "compare",
    "footer"
  ],
  "bodyClass": "page-index",
  "output": "index.html"
}
```

### 步骤 3：修改或创建模块

如果要修改现有模块，直接编辑 `sections/模块名/模块名.html` 文件。

如果要创建新模块：

1. 创建模块目录：
   ```bash
   mkdir sections/my-new-module
   ```

2. 创建模块文件：
   ```bash
   touch sections/my-new-module/my-new-module.html
   ```

3. 编写模块代码（参考其他模块的结构）

4. 创建资源目录（如需要）：
   ```bash
   mkdir assets/my-new-module
   ```

### 步骤 4：运行构建

```bash
python tools/build.py
```

### 步骤 5：预览页面

在浏览器中打开生成的 HTML 文件，或使用本地服务器：

```bash
# Python
python -m http.server 8000

# 访问 http://localhost:8000/index.html
```

## 🔗 社交媒体链接配置

项目提供了基于配置文件的社交媒体链接管理系统。

### 快速配置

1. **编辑配置文件**

打开 `tools/social-links.config.json`：

```json
{
  "links": [
    {
      "name": "LinkedIn",
      "url": "https://linkedin.com/company/yourcompany",
      "icon": "linkedin",
      "enabled": true
    },
    {
      "name": "YouTube",
      "url": "https://youtube.com/@yourhandle",
      "icon": "youtube",
      "enabled": true
    }
  ]
}
```

2. **重新构建网站**

```bash
python tools/build.py
```

### 可用操作

- **更改链接**：修改 `url` 字段
- **更换图标**：修改 `icon` 字段（可选：linkedin, youtube, instagram, tiktok, facebook, twitter, discord, github 等）
- **禁用链接**：设置 `"enabled": false`
- **添加链接**：在 `links` 数组中添加新对象
- **调整顺序**：在数组中调整对象的顺序

**详细说明**请参考 `tools/链接修改指南.md`

## 🚀 开发工作流程

### 日常开发流程

1. **修改模块**
   ```bash
   # 编辑模块文件
   vim sections/banner/banner.html
   ```

2. **测试模块**（可选）
   - 在浏览器中单独打开模块文件测试
   - 或创建测试页面只包含该模块

3. **构建页面**
   ```bash
   python tools/build.py
   ```

4. **预览效果**
   ```bash
   # 启动本地服务器
   python -m http.server 8000

   # 浏览器访问
   open http://localhost:8000/index.html
   ```

5. **提交更改**
   ```bash
   git add sections/banner/banner.html
   git commit -m "更新 Banner 模块样式"
   ```

### 添加新页面

如果需要创建全新的页面（如 about.html）：

1. **创建配置文件**

创建 `tools/build.about.config.json`：

```json
{
  "sections": [
    "navigation",
    "about-hero",
    "team",
    "footer"
  ],
  "bodyClass": "page-about",
  "output": "about.html",
  "description": "关于我们页面配置"
}
```

2. **创建所需模块**

```bash
mkdir sections/about-hero
mkdir sections/team
```

3. **修改构建脚本**（可选）

在 `tools/build.py` 的 `PAGES` 列表中添加新页面配置。

4. **构建页面**

```bash
python tools/build.py --config tools/build.about.config.json
```

## 🔍 常见问题

### Q: 如何修改页面？
A:
- `tools/build.config.json` → 对应 index 页面
- `tools/build.compose.config.json` → 对应 compose 页面
- `tools/build.create.config.json` → 对应 create 页面
- `tools/build.solutions.config.json` → 对应 solutions 页面
- `tools/build.explore.config.json` → 对应 explore 页面
- 修改代码只修改 sections 里面的模块
- 组合排列模块后，命令行输入 `python tools/build.py`，即可构建全部页面，生成 5 个整合版 HTML

### Q: 为什么修改了模块但页面没变化？
A:
模块修改后必须重新构建页面：
```bash
python tools/build.py
```
然后刷新浏览器（建议使用 Ctrl+F5 强制刷新）。

### Q: 构建失败怎么办？
A:
1. 检查错误信息，通常会指出缺失的文件或格式错误
2. 确认配置文件 JSON 格式正确（可使用 [JSONLint](https://jsonlint.com/) 验证）
3. 检查模块文件路径是否正确：`sections/模块名/模块名.html`
4. 查看构建输出中的 `[skip]` 警告，了解哪些模块缺失

### Q: 如何临时禁用某个模块？
A:
在配置文件的 `sections` 数组中注释掉或删除该模块名：
```json
{
  "sections": [
    "navigation",
    "banner",
    // "compare",  // 临时禁用
    "footer"
  ]
}
```

### Q: 资源文件应该放在哪里？
A:
- 模块专属资源：`assets/模块名/`
- 全局资源（Logo、Favicon等）：`assets/images/`

### Q: 如何调试模块？
A:
1. 使用浏览器开发者工具（F12）
2. 检查控制台错误信息
3. 单独测试模块（直接在浏览器中打开模块 HTML 文件）
4. 使用 `console.log()` 输出调试信息

### Q: 模块的 CSS 会影响其他模块吗？
A:
会的。为避免样式冲突：
1. 使用 BEM 命名规范（如 `.module-name__element`）
2. 为模块使用唯一的类名前缀
3. 避免使用过于通用的类名（如 `.title`、`.button`）
4. 优先使用模块特定的类名而不是全局样式

### Q: 如何修改全局样式？
A:
编辑以下文件：
- `global/global.css` - 全局 CSS 变量和通用样式
- `css/treclip.css` - 项目主题样式
- `global/head.html` - 全局头部（字体、meta 等）

修改后重新构建页面。

### Q: sections/links/links.html 能手动修改吗？
A:
**不能**。这个文件由 `generate-social-links.py` 自动生成，每次构建都会被覆盖。

要修改社交链接，请编辑：
- `tools/social-links.config.json`

然后运行 `python tools/build.py` 重新生成。

## 💡 最佳实践总结

### 模块开发

1. **保持模块独立**：每个模块应该是自包含的，不依赖其他模块的 DOM 或 JavaScript
2. **使用 IIFE**：用立即执行函数包裹模块的 JavaScript，避免全局变量污染
3. **命名规范**：使用 BEM 命名法，确保样式不冲突
4. **响应式优先**：每个模块都应该包含完整的响应式样式
5. **性能考虑**：使用 `loading="lazy"`、`preload="none"` 等优化资源加载

### 页面组合

1. **逻辑顺序**：模块顺序应该符合用户的阅读习惯（导航 → 内容 → 页脚）
2. **不要过度组合**：一个页面包含 5-10 个模块最佳，太多会影响性能
3. **测试不同组合**：在配置文件中尝试不同的模块组合，找到最佳方案

### 构建流程

1. **频繁构建**：修改后立即构建，及早发现问题
2. **检查输出**：注意构建输出中的警告和错误信息
3. **版本控制**：使用 Git 管理配置文件的变更
4. **备份配置**：修改配置文件前先备份

### 资源管理

1. **按模块组织**：每个模块的资源放在对应的 `assets/模块名/` 目录
2. **优化资源**：压缩图片和视频，使用合适的格式
3. **使用相对路径**：资源引用使用相对路径，便于部署
4. **懒加载**：对非首屏资源使用懒加载

## 📚 相关文档

- `tools/链接修改指南.md` - 社交媒体链接配置详细说明
- `docs/` - 项目其他文档
- [Simple Icons](https://simpleicons.org/) - 品牌图标资源
- [JSONLint](https://jsonlint.com/) - JSON 格式验证工具

## 🐛 故障排查

### 问题：构建时提示模块文件未找到

**原因**：配置文件中指定的模块在 `sections/` 目录中不存在。

**解决方案**：
1. 检查模块名称拼写是否正确
2. 确认模块文件路径：`sections/模块名/模块名.html`
3. 从配置文件中删除不需要的模块，或创建缺失的模块

### 问题：页面样式混乱

**原因**：模块之间的 CSS 样式冲突。

**解决方案**：
1. 使用浏览器开发者工具检查样式来源
2. 确保每个模块使用唯一的类名前缀
3. 检查是否有过于通用的 CSS 选择器
4. 使用更具体的选择器或增加选择器权重

### 问题：JavaScript 报错

**原因**：模块的 JavaScript 代码冲突或依赖缺失。

**解决方案**：
1. 打开浏览器控制台查看具体错误信息
2. 确认所有模块的 JavaScript 都使用 IIFE 包裹
3. 检查是否有重复的 ID 或变量名
4. 确保在 `DOMContentLoaded` 后初始化模块

---

**最后更新时间：** 2025-11-19

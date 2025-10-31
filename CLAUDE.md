# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

Star-UI 是一个基于 Webflow 模板的网站项目，主题为宇宙、宇航员和月食。项目采用静态 HTML + CSS + JavaScript 架构，集成 Supabase 作为后端服务。

**设计理念**：简洁为主，不要过于花哨。参考网站：
- https://www.florafauna.ai/
- https://www.freepik.com/

## 项目结构

```
Star-UI/
├── 要求/
│   ├── 要求.md              # 项目需求文档
│   └── TreClip/             # 主要网站代码
│       ├── index.html       # 首页
│       ├── css/             # 样式文件
│       │   ├── normalize.css
│       │   ├── webflow.css
│       │   └── treclip-com.webflow.css
│       ├── js/              # JavaScript 文件
│       │   ├── auth.js      # Supabase 认证逻辑
│       │   └── webflow.js   # Webflow 交互
│       ├── images/          # 图片资源
│       ├── videos/          # 视频资源
│       ├── fonts/           # 字体文件
│       ├── supabase/        # Supabase 配置
│       │   └── functions/   # Edge Functions
│       │       └── waitlist/
│       │           └── index.ts  # 邮件列表注册
│       └── *.html           # 各个页面
│           ├── dashboard.html
│           ├── sign-in.html
│           ├── sign-up.html
│           ├── pricing_*.html
│           └── ...
```

## 核心技术栈

- **前端**：原生 HTML/CSS/JavaScript
- **框架**：Webflow 导出的静态模板
- **后端**：Supabase (认证 + Edge Functions)
- **动画**：Lenis 平滑滚动库
- **字体**：Google Fonts (PT Sans, Bitter, Changa One)

## 代码组织原则

### 模块化开发要求
**严格遵守**：每个功能模块的 HTML、CSS、JavaScript 必须放在一起，便于后续移动和维护。

**推荐结构示例**：
```html
<!-- 导航栏模块 -->
<nav class="navbar">
  <!-- HTML 结构 -->
</nav>

<style>
  /* 导航栏专用样式 */
  .navbar { ... }
</style>

<script>
  // 导航栏交互逻辑
  document.querySelector('.navbar')...
</script>

<!-- 下一个模块 -->
<section class="hero">
  ...
</section>
```

### 视频处理规范
- Banner 和导航栏均使用视频背景
- 鼠标悬浮自动播放，无需进度条、暂停键等控制
- 所有视频必须自动循环播放

### 响应式设计
- **必须适配移动端**
- 使用 `<meta name="viewport" content="width=device-width, initial-scale=1">`
- 测试不同屏幕尺寸的显示效果

## Supabase 集成

### 认证配置
主要逻辑在 `/要求/TreClip/js/auth.js`：
- 使用 Supabase v2 SDK
- 从 CDN 动态加载：`https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.js`
- 保护路由：`/dashboard.html` 需要登录

**配置项**：
```javascript
SUPABASE_URL: 'https://YOUR_SUPABASE_URL.supabase.co'
SUPABASE_ANON_KEY: 'YOUR_SUPABASE_ANON_KEY'
```

### Edge Functions
位置：`/要求/TreClip/supabase/functions/waitlist/index.ts`

**功能**：邮件列表注册（集成 Brevo API）
- 验证邮件格式
- 要求用户同意营销邮件
- 自动更新联系人信息

**环境变量**：
- `BREVO_API_KEY`
- `BREVO_LIST_ID`

## 开发工作流

### 本地开发
```bash
# 直接在浏览器打开 HTML 文件
# 或使用简单的 HTTP 服务器
python -m http.server 8000
# 或
npx serve
```

### Supabase 本地开发
```bash
# 启动 Supabase 本地环境
cd 要求/TreClip
supabase start

# 部署 Edge Functions
supabase functions deploy waitlist
```

### 测试邮件列表功能
```bash
curl -X POST https://YOUR_PROJECT.supabase.co/functions/v1/waitlist \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "marketingOptIn": true}'
```

## 页面说明

| 文件名 | 用途 |
|--------|------|
| `index.html` | 首页 |
| `sign-in.html` | 登录页面 |
| `sign-up.html` | 注册页面 |
| `dashboard.html` | 用户仪表板（需登录） |
| `pricing_plan.html` | 个人定价页面 |
| `pricing_business.html` | 企业定价页面 |
| `about.html` | 关于页面 |
| `contact.html` | 联系页面 |
| `privacy.html` | 隐私政策 |
| `terms.html` | 服务条款 |

## 重要注意事项

1. **不要随意创建新文件** - 优先在现有文件基础上修改
2. **视频自动播放** - 悬停触发，无控制按钮
3. **模块化组织** - HTML/CSS/JS 放在一起
4. **移动端优先** - 所有新功能必须测试移动端兼容性
5. **简洁设计** - 避免过度装饰，保持太空主题的专业感
6. **Supabase 密钥** - 永远不要将真实密钥提交到代码库

## 常见任务

### 添加新页面
1. 复制现有 HTML 模板（如 `index.html`）
2. 保持头部引用的 CSS/JS 文件一致
3. 确保包含 Lenis 库和 auth.js
4. 如需认证，在 `CONFIG.protected` 数组添加路径

### 修改样式
- 全局样式：`css/treclip-com.webflow.css`
- 重置样式：`css/normalize.css`
- Webflow 基础：`css/webflow.css`

### 调试认证问题
1. 检查浏览器控制台的 Supabase 错误
2. 确认 `SUPABASE_URL` 和 `SUPABASE_ANON_KEY` 正确
3. 查看 Supabase Dashboard 的认证日志
4. 验证路由配置是否正确

## 浏览器兼容性
- 现代浏览器（Chrome, Firefox, Safari, Edge）
- 移动浏览器（iOS Safari, Chrome Mobile）
- 不支持 IE11 及以下版本

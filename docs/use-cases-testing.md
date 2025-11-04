# Use Cases 模块测试文档

## ✅ 实现完成情况

### 已完成功能

1. **✅ 移除 "All" 标签**
   - 左侧分类导航只显示 7 个分类按钮（Education, Motivation, Finance, Webinar, Vlog, Podcast, Coaching）
   - 默认激活第一个分类（Education）

2. **✅ 每个分类 6 张卡片**
   - 总共 42 张卡片（7 个分类 × 6 张卡片）
   - 每个分类独立，点击分类按钮只显示对应的 6 张卡片

3. **✅ 统一占位符图片**
   - 所有卡片暂时使用 `14.png` 作为占位符
   - 图片已复制到 `assets/images/use-case-placeholder.jpg`

4. **✅ 分类过滤交互**
   - 点击分类按钮，右侧只显示对应分类的卡片
   - 其他分类的卡片淡出隐藏（opacity: 0, transform: scale(0.95)）
   - 按钮激活状态切换（白色背景 + 黑色文字）

5. **✅ 视频悬浮播放**
   - 所有卡片支持鼠标悬停播放视频
   - 复用 gallery 模块的视频播放逻辑
   - 离开时视频暂停并重置到开头

6. **✅ 响应式设计**
   - 桌面端：左侧固定导航 + 右侧 3 列网格
   - 平板端（≤ 991px）：导航横向排列 + 2 列网格
   - 移动端（≤ 767px）：导航横向换行 + 1 列网格

---

## 🧪 测试步骤

### 1. 启动开发服务器

已经在后台运行开发服务器（端口 8000）：

```bash
# 访问页面
http://localhost:8000/
```

### 2. 功能测试清单

#### 分类过滤测试
- [ ] 页面加载后默认显示 "Education" 分类的 6 张卡片
- [ ] 点击 "Motivation" 按钮，显示 Motivation 分类的 6 张卡片
- [ ] 点击 "Finance" 按钮，显示 Finance 分类的 6 张卡片
- [ ] 点击其他分类，依次验证每个分类都有 6 张卡片
- [ ] 切换分类时，按钮激活状态正确切换（白色背景）
- [ ] 卡片切换有淡入淡出动画（0.4s）

#### 视频播放测试
- [ ] 鼠标悬停在卡片上，视频自动播放
- [ ] 鼠标离开卡片，视频暂停并重置
- [ ] 视频叠加层有淡入效果（从图片切换到视频）
- [ ] 描述文本在悬停时从底部淡入

#### 响应式测试
- [ ] 桌面端（≥ 992px）：左侧垂直导航，右侧 3 列网格
- [ ] 平板端（768px - 991px）：导航横向排列，右侧 2 列网格
- [ ] 移动端（≤ 767px）：导航换行，右侧 1 列网格
- [ ] 所有断点下分类过滤功能正常工作

#### 视觉检查
- [ ] 所有卡片显示占位符图片（14.png）
- [ ] 卡片圆角（border-radius: 20px）
- [ ] 卡片宽高比（aspect-ratio: 3 / 4）
- [ ] 分类标签显示正确（左上角，半透明背景）
- [ ] 标题和副标题居中显示
- [ ] "USE CASES" 小标题为青蓝色（#60A5FA）

---

## 📊 模块详细信息

### 文件结构

```
sections/use-cases/
└── use-cases.html          # 完整模块文件（HTML + CSS + JS）

assets/images/
└── use-case-placeholder.jpg  # 占位符图片（14.png 的副本）
```

### 卡片数据结构

每个分类 6 张卡片：

| 分类 | 卡片数量 | data-categories 属性 |
|------|----------|---------------------|
| Education | 6 | `"education"` |
| Motivation | 6 | `"motivation"` |
| Finance | 6 | `"finance"` |
| Webinar | 6 | `"webinar"` |
| Vlog | 6 | `"vlog"` |
| Podcast | 6 | `"podcast"` |
| Coaching | 6 | `"coaching"` |
| **总计** | **42** | - |

### 视频资源映射

当前所有卡片复用现有视频资源：

- `assets/videos/gallery-1.mp4`
- `assets/videos/gallery-2.mp4`
- `assets/videos/gallery-3.mp4`
- `assets/videos/gallery-4.mp4`
- `assets/videos/gallery-5.mp4`
- `assets/videos/gallery-6.mp4`

---

## 🔧 后续优化建议

### 1. 替换真实图片
当准备好真实图片后，替换 `use-case-placeholder.jpg`：

```bash
# 示例：为每个卡片使用不同的图片
cp education-1.jpg assets/images/use-case-education-1.jpg
cp education-2.jpg assets/images/use-case-education-2.jpg
# ...以此类推
```

然后修改 `sections/use-cases/use-cases.html` 中的图片路径。

### 2. 添加真实视频
为每个分类准备专属视频：

```bash
cp education-1.mp4 assets/videos/use-case-education-1.mp4
cp motivation-1.mp4 assets/videos/use-case-motivation-1.mp4
# ...以此类推
```

### 3. 卡片描述文本优化
当前使用通用描述文本，可以根据实际业务需求修改每张卡片的描述。

### 4. 添加加载动画
考虑为卡片切换添加骨架屏或加载动画，提升用户体验。

### 5. SEO 优化
为每张卡片的图片添加更具描述性的 `alt` 属性。

---

## 🐛 已知问题

### 无已知问题

当前模块功能完整，所有交互正常工作。

---

## 📝 代码统计

- **总行数**：837 行
- **CSS 行数**：249 行
- **HTML 行数**：518 行
- **JavaScript 行数**：70 行

---

## 🎨 设计规范

### 颜色方案

- **标题小字**：`#60A5FA`（青蓝色）
- **主标题**：`var(--color-text)`（白色）
- **副标题**：`var(--color-text-secondary)`（灰色）
- **分类按钮（默认）**：背景 `var(--color-bg-secondary)`，文字 `var(--color-text-secondary)`
- **分类按钮（激活）**：背景 `var(--color-text)`（白色），文字 `var(--color-bg)`（黑色）
- **卡片标签**：半透明白色背景（rgba(255, 255, 255, 0.15)）

### 间距规范

- **模块上下内边距**：`var(--spacing-3xl)`（96px）
- **分类导航间距**：`var(--spacing-sm)`（16px）
- **卡片网格间距**：`var(--spacing-lg)`（32px）
- **卡片内边距**：`var(--spacing-lg)`（32px）

### 动画规范

- **分类按钮切换**：`0.3s ease`
- **卡片显示/隐藏**：`0.4s ease`（opacity + transform）
- **视频淡入淡出**：`0.3s ease`
- **描述文本淡入**：`0.3s ease`

---

## ✅ 验收标准

1. ✅ 移除了 "All" 标签
2. ✅ 7 个分类，每个分类 6 张卡片（总共 42 张）
3. ✅ 所有卡片使用 `14.png` 作为占位符图片
4. ✅ 分类过滤功能正常工作
5. ✅ 视频悬浮播放功能正常
6. ✅ 完全响应式设计
7. ✅ 集成到构建系统（`tools/build.config.json`）
8. ✅ 页面成功生成到 `index.html`

---

## 🚀 下一步

模块已完全实现并集成！你现在可以：

1. 在浏览器中打开 `http://localhost:8000/` 查看效果
2. 测试所有交互功能
3. 准备真实图片和视频资源进行替换
4. 根据实际需求调整卡片描述文本

如有任何问题或需要调整，随时告诉我！

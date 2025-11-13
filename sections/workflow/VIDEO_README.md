# Workflow 模块视频说明

## 文件列表

当前模块包含 4 组视频和缩略图文件,对应 4 个工作流程卡片:

### 1. Generative (生成式)
- 缩略图: `generative.jpg`
- 视频: `generative.mp4`

### 2. Storyboard (故事板)
- 缩略图: `storyboard.jpg`
- 视频: `storyboard.mp4`

### 3. Timeline (时间轴)
- 缩略图: `timeline.jpg`
- 视频: `timeline.mp4`

### 4. Assistant (助手)
- 缩略图: `assistant.jpg`
- 视频: `assistant.mp4`

## 视频规格要求

- **格式**: MP4 (H.264)
- **时长**: 建议 5-10 秒短视频
- **尺寸**: 建议 1000x1000 或类似比例
- **音频**: 无需音频(会自动静音)
- **循环**: 自动循环播放

## 缩略图规格要求

- **格式**: JPG/PNG
- **尺寸**: 与视频尺寸保持一致
- **用途**: 鼠标未悬浮时显示,悬浮后淡出并播放视频

## 替换资源方法

只需将对应分类的文件替换为同名文件即可:

```bash
# 例如:替换 Generative 卡片的视频和缩略图
cp 你的新缩略图.jpg sections/workflow/generative.jpg
cp 你的新视频.mp4 sections/workflow/generative.mp4

# 然后重新构建
python3 tools/build.py
```

## 当前状态

- **缩略图**: 使用原有的1.png, 2.jpg, 3.png, 4.png 的副本
- **视频**: 使用演示视频 `videos/video_2.mp4` 的副本

后续需要替换为对应功能的实际资源内容。

## 视频压缩建议

如果视频文件过大,可以使用 FFmpeg 压缩:

```bash
ffmpeg -i input.mp4 \
  -vcodec h264 \
  -b:v 6M \
  -s 1000x1000 \
  -an \
  output.mp4
```

## 交互效果

- **默认状态**: 显示静态缩略图
- **鼠标悬浮**: 缩略图淡出,视频淡入并自动播放
- **鼠标离开**: 视频暂停并重置到开头,缩略图淡入

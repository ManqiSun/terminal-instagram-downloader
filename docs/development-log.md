# Development Log

## Project

Terminal Instagram Downloader

---

## Project Goal | 项目目标

Build a command-line tool for downloading Instagram content.

构建一个基于 Python 的 Instagram 命令行下载工具，实现：

* Instagram 视频下载
* Instagram 图片下载
* 批量下载
* 下载统计
* 重复下载检测

---

## Initial Idea | 最初想法

After successfully building a YouTube downloader with yt-dlp, I wanted to explore whether the same workflow could be extended to Instagram.

在完成 YouTube 下载工具后，我产生了一个想法：

> yt-dlp 能下载 YouTube 视频，那么是否也能下载 Instagram 内容？

The goal was to create a simple workflow:

目标流程：

```text
Command
↓
Paste Link
↓
Download Content
```

---

## Phase 1: Video Download Testing | 第一阶段：视频下载测试

The first test focused on Instagram Reel downloads.

首先测试 Instagram Reel。

Using:

```bash
yt-dlp
```

Results:

```text
✅ Reel
✅ Video Post
✅ Video Carousel
```

yt-dlp successfully downloaded all video-related content.

因此创建了：

```text
ig-video
```

Command workflow:

```text
ig-video
↓
Paste Instagram URL
↓
Download Video
```

---

## Phase 2: Unexpected Failure | 第二阶段：意料之外的失败

The next step was testing photo posts.

随后开始测试 Instagram 图片帖子。

The result:

```text
ERROR:
There is no video in this post
```

At first I assumed the URL was incorrect.

最开始以为是链接错误。

However, after testing multiple posts, the same error appeared every time.

连续测试多个图片帖子后，结果完全一致。

This revealed an important fact:

最终确认：

```text
Video Content
↓
yt-dlp

Photo Content
↓
Not Supported
```

My first assumption was incorrect.

第一个技术假设被推翻。

---

## Phase 3: Finding Another Solution | 第三阶段：寻找新的解决方案

To support photo downloads, I started looking for another tool.

为了实现图片下载，开始寻找新的工具。

Eventually I discovered:

最终发现：

```text
Instaloader
```

Installation:

```bash
pip install instaloader
```

Instaloader is specifically designed for Instagram content.

Instaloader 专门针对 Instagram 内容设计。

---

## Phase 4: Photo Download Success | 第四阶段：图片下载成功

Testing:

测试：

```text
Single Photo Post
Photo Carousel
```

Results:

结果：

```text
✅ Success
```

This confirmed the final architecture:

最终形成：

```text
Video Download
↓
yt-dlp

Photo Download
↓
Instaloader
```

Each tool handles a different content type.

不同工具负责不同内容类型。

---

## Phase 5: Command Creation | 第五阶段：创建终端命令

Single-download commands:

单个下载命令：

```text
ig-video
ig-photo
```

Supported:

```text
Instagram Reel
Video Post
Video Carousel

Photo Post
Photo Carousel
```

---

## Phase 6: Batch Download Support | 第六阶段：批量下载支持

To improve efficiency, batch download functionality was added.

为了提升效率，开发批量下载功能。

Created:

```text
ig-video-batch
ig-photo-batch
```

Batch workflow:

```text
Text File
↓
Read Links
↓
Download Automatically
↓
Generate Statistics
```

Supported features:

支持功能：

* Multiple links
* Progress display
* Download statistics
* Success count
* Failure count

---

## Phase 7: Download Statistics Optimization | 第七阶段：下载统计优化

Additional statistics were implemented.

增加统计信息。

Example:

```text
[1/3] Start Downloading

✅ This post contains 5 images
   Downloaded: 5
   Failed: 0
```

Final summary:

```text
Task Completed

Total Posts: 3
Successful Posts: 3
Failed Posts: 0

Total Images Downloaded: 14
```

---

## Phase 8: Folder Structure Optimization | 第八阶段：目录结构优化

To avoid file confusion, a dedicated folder structure was introduced.

为了避免文件混乱，重新设计目录结构。

Example:

```text
video_DYttWqJieoU
photo_DUIV8LqkSHQ
```

Each Instagram post receives its own folder.

每个帖子对应一个独立文件夹。

---

## Review Process | 项目Review

The project was tested using multiple scenarios.

项目完成后进行了完整测试。

### Review 1

Duplicate Download Detection

重复下载检测

Result:

```text
⚠️ Already Exists
```

Passed.

✅ Passed

---

### Review 2.1

Empty Line Test

空行测试

Passed.

✅ Passed

---

### Review 2.2

Invalid Link Test

错误链接测试

Result:

```text
❌ 无法识别的Instagram链接
```

Passed.

✅ Passed

---

### Review 2.3

Deleted / Invalid Post Test

失效帖子测试

Result:

```text
❌ Download Failed
```

Application remained stable.

程序未崩溃。

Passed.

✅ Passed

---

### Review 3

Folder Structure Review

目录结构检查

Passed.

✅ Passed

---

## Final Result | 最终成果

Instagram Download Tool v1.0

Implemented:

```text
✅ Single Video Download
✅ Single Photo Download

✅ Batch Video Download
✅ Batch Photo Download

✅ Download Statistics
✅ Duplicate Detection
✅ Error Handling

✅ Project Review Completed
```

---

## Key Takeaway | 最大收获

The most valuable lesson was not writing code.

The most valuable lesson was validating assumptions.

最大的收获不是写代码。

而是不断验证自己的假设。

Many development problems were not solved by writing more code.

They were solved by testing, observing failures, and adjusting the solution.

很多问题并不是靠写更多代码解决的。

而是通过测试、报错、验证和修正思路解决的。

---

Completion Date:

```text
2026-06-04
```

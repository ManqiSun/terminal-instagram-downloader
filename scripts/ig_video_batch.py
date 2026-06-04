import subprocess
import re
import os
from pathlib import Path

base_dir = Path("downloads")
links_file = base_dir / "ig_video_links.txt"

os.makedirs(base_dir, exist_ok=True)

video_extensions = [".mp4", ".mkv", ".webm", ".mov"]

with open(links_file, "r", encoding="utf-8") as file:
    urls = [line.strip() for line in file if line.strip()]

total = len(urls)
success_posts = 0
total_videos = 0

print(f"\n共发现 {total} 个视频帖子\n")

for index, url in enumerate(urls, start=1):
    print(f"[{index}/{total}] 开始下载：{url}")

    match = re.search(r"instagram\.com/(?:reel|p)/([^/?#]+)", url)

    if not match:
        print("❌ 无法识别的Instagram链接\n")
        continue

    shortcode = match.group(1)

    post_dir = base_dir / f"video_{shortcode}"
    os.makedirs(post_dir, exist_ok=True)

    before_files = set(post_dir.iterdir())

    command = [
        "yt-dlp",
        "-P", str(post_dir),
        "-o", "%(playlist_index)02d_%(id)s.%(ext)s",
        "--merge-output-format", "mp4",
        url
    ]

    result = subprocess.run(command)

    after_files = set(post_dir.iterdir())
    new_files = after_files - before_files

    new_videos = [
        file for file in new_files
        if file.suffix.lower() in video_extensions
    ]

    video_count = len(new_videos)

    if result.returncode == 0 and video_count > 0:
        success_posts += 1
        total_videos += video_count
        print(
            f"✅ 本帖共 {video_count} 个视频\n"
            f"   已下载：{video_count} 个\n"
            f"   失败：0 个\n"
        )
    elif result.returncode == 0 and video_count == 0:
        print("⚠️ 下载完成，但没有新增视频，可能之前已经下载过\n")
    else:
        print("❌ 下载失败\n")

print("=" * 40)

print("任务完成\n")

print(f"帖子总数：{total}")
print(f"成功帖子：{success_posts}")
print(f"失败帖子：{total - success_posts}")

print()

print(f"合计下载视频：{total_videos} 个")

print("=" * 40)
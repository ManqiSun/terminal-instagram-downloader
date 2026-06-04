import subprocess
import re
import os
from pathlib import Path

base_dir = Path("downloads")
links_file = base_dir / "ig_photo_links.txt"

os.makedirs(base_dir, exist_ok=True)

image_extensions = [".jpg", ".jpeg", ".png", ".webp"]

with open(links_file, "r", encoding="utf-8") as file:
    urls = [line.strip() for line in file if line.strip()]

total = len(urls)
success_posts = 0
total_images = 0

print(f"\n共发现 {total} 个图片帖子\n")

for index, url in enumerate(urls, start=1):
    print(f"[{index}/{total}] 开始下载：{url}")

    match = re.search(r"instagram\.com/p/([^/?#]+)", url)

    if not match:
        print("❌ 无法识别的Instagram链接\n")
        continue

    shortcode = match.group(1)

    post_dir = base_dir / f"photo_{shortcode}"
    os.makedirs(post_dir, exist_ok=True)

    before_files = set(post_dir.iterdir())

    command = [
        "instaloader",
        f"--dirname-pattern={post_dir}",
        "--no-videos",
        "--no-captions",
        "--no-metadata-json",
        "--no-compress-json",
        "--",
        f"-{shortcode}"
    ]

    result = subprocess.run(command)

    after_files = set(post_dir.iterdir())
    new_files = after_files - before_files

    new_images = [
        file for file in new_files
        if file.suffix.lower() in image_extensions
    ]

    image_count = len(new_images)

    if result.returncode == 0 and image_count > 0:
        success_posts += 1
        total_images += image_count
        print(
            f"✅ 本帖共 {image_count} 张图片\n"
            f"   已下载：{image_count} 张\n"
            f"   失败：0 张\n"
        )
    elif result.returncode == 0 and image_count == 0:
        print("⚠️ 下载完成，但没有新增图片，可能之前已经下载过\n")
    else:
        print("❌ 下载失败\n")

print("=" * 40)

print("任务完成\n")

print(f"帖子总数：{total}")
print(f"成功帖子：{success_posts}")
print(f"失败帖子：{total - success_posts}")

print()

print(f"合计下载图片：{total_images} 张")

print("=" * 40)
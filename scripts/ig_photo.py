import subprocess
import re
import os
from pathlib import Path

url = input("请输入 Instagram 图片帖子链接：").strip()

match = re.search(r"instagram\.com/p/([^/?#]+)", url)

if not match:
    print("没有识别到有效的 Instagram 图片帖子链接。")
else:
    shortcode = match.group(1)

    base_dir = Path("downloads")
    os.makedirs(base_dir, exist_ok=True)

    post_dir = base_dir / f"photo_{shortcode}"
    os.makedirs(post_dir, exist_ok=True)

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

    subprocess.run(command)
import subprocess
import os
from pathlib import Path

url = input("请输入 Instagram Reel/视频 链接：").strip()

base_dir = Path("downloads")
os.makedirs(base_dir, exist_ok=True)

command = [
    "yt-dlp",
    "-P", str(base_dir),
    "-o", "%(upload_date)s_%(uploader)s_%(id)s.%(ext)s",
    "--merge-output-format", "mp4",
    url
]

subprocess.run(command)
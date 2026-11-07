#!/usr/bin/env python3
"""Upload a new handbook PDF to Tencent COS as the public download file.

Overwrites public/kaoyan-handbook-2026/kaoyan-handbook-2026.pdf in the PicList
bucket with object ACL public-read; the bucket itself stays private. The
download filename is taken from the local file name.

Runs on the Mac: needs rclone (brew install rclone) and the Tencent COS
config saved in PicList. Credentials are passed to rclone through environment
variables only.

Usage: python3 scripts/upload-cos.py "/path/to/新版手册.pdf"
"""
import json
import os
import subprocess
import sys
import urllib.parse

KEY = "public/kaoyan-handbook-2026/kaoyan-handbook-2026.pdf"
PICLIST = "~/Library/Application Support/PicList/data.json"

if len(sys.argv) != 2 or not sys.argv[1].lower().endswith(".pdf"):
    sys.exit(__doc__)
src = os.path.abspath(sys.argv[1])

cfg = json.load(open(os.path.expanduser(PICLIST)))["picBed"]["tcyun"]
bucket, area = cfg["bucket"], cfg["area"]
env = dict(os.environ,
           RCLONE_CONFIG_COS_TYPE="s3",
           RCLONE_CONFIG_COS_PROVIDER="TencentCOS",
           RCLONE_CONFIG_COS_ACCESS_KEY_ID=cfg["secretId"],
           RCLONE_CONFIG_COS_SECRET_ACCESS_KEY=cfg["secretKey"],
           RCLONE_CONFIG_COS_ENDPOINT=f"cos.{area}.myqcloud.com")

name = urllib.parse.quote(os.path.basename(src))
subprocess.run([
    "rclone", "copyto", src, f"cos:{bucket}/{KEY}",
    "--s3-acl", "public-read",
    "--header-upload", "Content-Type: application/pdf",
    "--header-upload", f"Content-Disposition: attachment; filename*=UTF-8''{name}",
    "--header-upload", "Cache-Control: no-cache",
    "--progress",
], env=env, check=True)
print(f"\n已更新：https://{bucket}.cos.{area}.myqcloud.com/{KEY}")

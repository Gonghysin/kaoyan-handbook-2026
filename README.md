# 考研手册 2026 · 经验分享篇（在线阅读）

在线地址：https://gonghysin.github.io/kaoyan-handbook-2026/

- 在线阅读的页面图片由 GitHub Actions 从 `pdf/` 里的 PDF 自动生成。
- 「下载 PDF」按钮指向腾讯云 COS（国内下载快）：
  https://hysinoss-1334037784.cos.ap-shanghai.myqcloud.com/public/kaoyan-handbook-2026/kaoyan-handbook-2026.pdf
  「备用下载」是 GitHub Pages 上的同一份 PDF。

## 更换 PDF（两处都要换）

1. **网页阅读**：打开仓库的 `pdf/` 目录，删除旧 PDF，上传新 PDF（`pdf/` 里只能有 **1 个** PDF，文件名随意）。提交后约 1 分钟自动重新部署，进度在 **Actions** 页查看。
2. **下载链接**：在 Mac 上运行
   ```bash
   python3 scripts/upload-cos.py "/path/to/新版手册.pdf"
   ```
   脚本会覆盖 COS 上的下载文件（链接不变，下载文件名取本地文件名）。需要 `rclone` 和 PicList 里的腾讯云 COS 配置。

网页标题取自 PDF 的「标题」属性（WPS：文件 → 属性），没有时用文件名。

浏览量统计使用不蒜子（busuanzi），显示本页累计浏览次数。

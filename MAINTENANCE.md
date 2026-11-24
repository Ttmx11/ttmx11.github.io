# 主页维护说明

## 更新内容

可以在 GitHub 仓库中打开文件，点击编辑，修改后提交到 `main`。Actions 中绿色完成表示部署成功。

| 内容 | 文件 |
| --- | --- |
| 姓名、邮箱、导师、实验室、中英文简介与教育经历 | `_data/profile.yml` |
| 论文与书籍章节 | `_data/publications.yml` |
| 比赛、奖项与年份 | `_data/awards.yml` |
| 双语栏目名称 | `_data/ui.yml` |
| 排版、照片显示比例与配色 | `assets/css/custom.css` |
| 公开版简历 | `assets/files/Sicen_Guo_CV.pdf` |
| 头像 | `images/gsc_bio.jpg` |

YAML 缩进使用空格。含冒号的标题请用引号包住；列表中每篇论文以 `- id:` 开始。

## 新增论文

```yaml
- id: unique-paper-name
  category: journal
  title: "完整的正式标题"
  authors: "Sicen Guo, Other Author"
  venue: Journal Name
  short_venue: Journal Abbreviation
  year: 2027
  summary_en: English description.
  summary_zh: 中文简介。
```

`category` 可选 `journal`（期刊论文）、`manuscript`（在审稿件）或 `chapter`（书籍章节）。已发表成果未填写 `scholar` 时，自动链接到完整标题的 Scholar 搜索结果；取得准确的个人 Scholar 条目链接后，可添加 `scholar: https://scholar.google.com/citations?...`。

在审稿件仅填写已经核对的 `arxiv` 地址，无地址则不添加链接。稿件录用后改为 `journal` 并补齐正式年份、刊物等信息；不要将预印本和最终发表版本重复计数。

验证脚本自动读取数据中的成果数量及无链接稿件；新增论文或补充 arXiv 链接时无需修改验证脚本。

## 更新公开版简历

网页内容更新不会自动重新生成 PDF。请同步替换公开版 PDF；发布前确认其中没有手机号、内部审稿信息或不希望公开的内容。不要上传原始私人简历。

本机另有未提交的 `tools/make_public_cv.py`，可在安装 ReportLab 和 PyYAML 的 Python 环境中重新生成中文公开版，字体依赖 Windows 微软雅黑。

## 部署与回退

仓库 Settings → Pages 的 Source 设为 GitHub Actions。每次提交 `main` 后，Actions 会先构建并检查站内链接、双语页面和必要资源，再发布。构建失败时现有网站不被替换。

需要回退时，在 GitHub 撤销引入问题的提交，再等待部署完成。不要删除整个仓库。

未来添加专利或其他荣誉时补充相应数据、双语栏目和模板；第一版没有空占位栏目。

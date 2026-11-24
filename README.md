# Sicen Guo / 郭思岑

中英双语科研个人主页，基于 [AcademicPages](https://academicpages.github.io/) 的 Jekyll 主题样式定制。

- English: https://ttmx11.github.io/
- 中文：https://ttmx11.github.io/zh/
- 部署：GitHub Actions → GitHub Pages
- 内容维护：[MAINTENANCE.md](MAINTENANCE.md)
- 资料核对记录：[SOURCES.md](SOURCES.md)

## 本地构建

需要 Ruby 3.3 和 Bundler。首次执行 `bundle install`，然后运行：

```sh
bundle exec jekyll serve --host 127.0.0.1
```

打开 http://127.0.0.1:4000 。本地预览如需正确的站内路径，可使用 `bundle exec jekyll serve --url http://127.0.0.1:4000`。

提交到 `main` 后，工作流构建、验证再部署。未提交的原始简历、凭据、缓存和临时文件不会发布。

## 许可

AcademicPages / Minimal Mistakes 主题代码按 MIT 授权，详见 `LICENSE` 与 `THIRD_PARTY_NOTICES.md`。个人照片、简历和个人资料不作为主题模板素材授权。

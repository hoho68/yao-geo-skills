# 用 Qiaomu 示例学会使用 GEO 工具

这份教程专门给新手使用。你不需要先懂 Git、PR、CI，也不需要先写代码。

我们用项目里的 Qiaomu 示例，学会一件事：

> 客户给你一个参考网站以后，你如何把它变成 GEOFlow 可理解、可预览、可交付的方案。

## 这个示例在哪里

主要看这几个文件：

- 示例说明：`skills/yao-geoflow-template/examples/qiaomu-editorial/README.md`
- 分析报告：`skills/yao-geoflow-template/reports/qiaomu-blog-mapping-2026-04-18.md`
- 预览首页：`skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/index.html`
- 视觉规则：`skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/package/tokens.json`
- 页面映射：`skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/package/mapping.json`

你先不用全部看懂。按下面顺序看就可以。

## 这个示例模拟的客户需求

可以把它想象成一个客户说：

> 我喜欢 Qiaomu Blog 这种安静、干净、适合阅读的文章站风格。你能不能帮我把 GEOFlow 网站也做成类似感觉？

这个需求里有三个关键信息：

- 客户有一个参考网站
- 客户想改的是视觉和模板体验
- 我们不能直接复制 HTML，也不能直接动生产网站

所以正确做法不是马上写代码，而是先做：

1. 参考站分析
2. 风格 tokens
3. GEOFlow 页面 mapping
4. preview-only 预览
5. 客户确认后再考虑上线

## 第一步：看参考站分析报告

打开：

```text
skills/yao-geoflow-template/reports/qiaomu-blog-mapping-2026-04-18.md
```

你重点看这些问题：

- 这个参考站是什么感觉？
- 它适合做什么类型的网站？
- 哪些地方可以学？
- 哪些地方不能直接复制？
- 它怎么映射到 GEOFlow 的首页、分类页、文章页、归档页？

在 Qiaomu 示例里，我们得到的判断是：

- 风格是 editorial，适合阅读
- 颜色克制，背景偏暖白
- 页面窄，文章阅读舒服
- 重点是排版、边距、卡片和导航
- 不应该复制它的完整 HTML
- 不应该改变 GEOFlow 后端数据、路由、SEO 或文章结构

你以后服务客户时，也先做这种判断。

## 第二步：看 tokens.json

打开：

```text
skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/package/tokens.json
```

你可以把 `tokens.json` 理解成：

> 这个参考网站的“设计配方”。

它记录了：

- 背景色
- 文字色
- 辅助文字色
- 边框色
- 强调色
- 字体方向
- 圆角
- 页面宽度

Qiaomu 示例里最重要的是：

```text
style_direction:
- editorial
- reading-first
- border-light
- accent-constrained
```

翻译成人话：

- 像一本安静的线上杂志
- 适合读文章
- 边框轻，不花哨
- 颜色克制，不做大红大紫

你以后给客户做项目时，可以把 tokens 当成“设计语言说明”。

## 第三步：看 mapping.json

打开：

```text
skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/package/mapping.json
```

你可以把 `mapping.json` 理解成：

> 把参考网站的感觉，安排到 GEOFlow 的哪些页面和模块上。

它告诉我们：

- 先做 header
- 再做 homepage
- 再做 category
- 再做 article
- 最后做 archive

示例里的顺序是：

```text
header -> home -> category -> article -> archive
```

这对你接项目很重要，因为它告诉你：

> 不要一次性全改。先按顺序做最小切片。

它还规定了安全边界：

- 保留 GEOFlow 路由
- 保留文章、分类、归档数据来源
- 只通过主题资源改样式
- preview 和生产上线分开

这就是你以后保护项目安全的核心。

## 第四步：看 preview 页面

打开这些文件：

```text
skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/index.html
skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/category.html
skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/article.html
skills/yao-geoflow-template/preview/qiaomu-editorial-20260418/archive.html
```

它们分别代表：

- 首页预览
- 分类页预览
- 文章页预览
- 归档页预览

如果你想在浏览器里看，可以在仓库根目录运行：

```powershell
python skills\yao-geoflow-template\scripts\serve_preview.py
```

然后打开：

```text
http://127.0.0.1:45731/preview/qiaomu-editorial-20260418/index.html
```

注意：这只是预览，不是上线。

## 第五步：你要学会怎么对客户解释

你可以这样和客户说：

```text
我先用参考网站提取了一个视觉方向，不是直接复制它的代码。
现在已经整理出颜色、排版、页面模块和预览页面。
这一步是 preview-only，不会影响你的生产网站。
如果你认可这个方向，下一步需要接入真实 GEOFlow 源码，再创建安全的 preview 主题。
```

这句话很重要，因为它同时讲清楚了：

- 你做了什么
- 你没有冒险改生产
- 下一步需要什么

## 第六步：你以后接项目怎么照着做

当客户给你一个新项目时，照这个顺序：

1. 填 [客户项目资料表](client-project-intake-template.md)
2. 问客户有没有参考网站
3. 问客户有没有源码
4. 没源码：先做参考站分析和方案
5. 有源码：按 [真实应用交接清单](geoflow-app-handoff-checklist.md) 做 discovery
6. discovery 通过：创建 preview 主题
7. 只改 preview，不改生产
8. 最后按 [标准交付物清单](client-deliverables-checklist.md) 交付

## 你要记住的 4 个关键词

### 1. Reference

客户喜欢的网站或页面。

在示例里是：

```text
https://blog.qiaomu.ai/2026-04-17-qp2x50
```

### 2. Tokens

参考网站的设计配方。

比如颜色、字体、边框、页面宽度。

### 3. Mapping

把参考网站的风格安排到 GEOFlow 的具体页面模块。

比如首页、分类页、文章页、归档页。

### 4. Preview-only

只做预览，不等于上线。

客户确认前，不动生产网站。

## 这个示例最终教会你什么

Qiaomu 示例不是让你背代码。

它教你一套接项目的方法：

```text
客户参考网站
-> 风格分析
-> tokens 设计配方
-> mapping 页面映射
-> preview-only 预览
-> 客户确认
-> 再考虑真实源码和上线
```

你以后做自己的项目、帮别人做项目，都可以按这个顺序来。

## 下一步练习

请你拿一个真实或假想客户，填一版：

- [客户项目资料表](client-project-intake-template.md)

如果暂时没有客户，就用你自己的项目当客户。

填完以后，我们就可以把 Qiaomu 示例的方法，套到你的第一个真实项目上。

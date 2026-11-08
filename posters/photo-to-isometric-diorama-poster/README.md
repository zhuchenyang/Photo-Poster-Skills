# Photo to Isometric Diorama Poster

将照片转化为上方摄影画面、下方等距微缩场景的精致海报，默认配有英文编辑式文案。

当前版本：**v1.5**。

## 效果示例

以下三张展示同一套版式在不同场景中的表现：上半部摄影画面，下半部英文文案与微缩模型。点击图片可查看原图。

| 港湾 · Harbor Stillness | 双湖 · Alpine Stillness | 河谷 · Alpine Waters |
| --- | --- | --- |
| [![港湾木船与水体厚基座海报](assets/examples/harbor-stillness.png)](assets/examples/harbor-stillness.png) | [![雪山双湖与局部水体剖切海报](assets/examples/alpine-stillness.png)](assets/examples/alpine-stillness.png) | [![雪峰河谷与水体截面海报](assets/examples/alpine-waters.jpg)](assets/examples/alpine-waters.jpg) |

## 视觉规则

- 竖版 3:4，上下各占 50%。
- 下半部默认采用暖中性背景，左侧英文文案、右侧完整微缩模型。
- 文案包括眉题、主标题与两行辅助文字，随照片内容变化，保持安静、克制的语气。
- 先预留文字空间，再确定模型位置，必要时整体等比缩小；完整轮廓和阴影均需保留宽松留白。
- 保留土壤、岩石、植被、木材、砖石、混凝土等真实材质，剖面与场景地形相符。
- 用户可要求无字版本、其他语言或指定文案。

## 安装到 Codex

本效果是 [海报技能集合](../../README.md) 中的一个独立技能。

[下载 v1.5 独立安装包](https://github.com/zhuchenyang/Photo-Poster-Skills/releases/download/isometric-diorama-v1.5/photo-to-isometric-diorama-poster-v1.5.zip)。

优先下载对应 Release 附带的 `photo-to-isometric-diorama-poster-v<版本>.zip`，解压后将 `photo-to-isometric-diorama-poster` 文件夹放入 Codex 用户技能目录（通常为 `~/.codex/skills/`；设置 `CODEX_HOME` 时使用其 `skills` 子目录）。

也可下载集合仓库源码，只复制 `posters/photo-to-isometric-diorama-poster/`。不要把整个仓库克隆到单个技能目录。已有同名技能时先备份再更新。

当前 [历史 v1.3 Release](https://github.com/zhuchenyang/Photo-Poster-Skills/releases/tag/v1.3) 保留原有布局，可使用其 Source code (zip)，将解压根目录命名为技能名后安装；后续发布优先使用单效果安装 ZIP。

```text
photo-to-isometric-diorama-poster/
├── SKILL.md
├── references/prompt-template.md
└── agents/openai.yaml
```

## 使用

附上照片并请求：

```text
使用 $photo-to-isometric-diorama-poster 处理这张照片。
```

也可以指定“不要文字”“改用中文文案”或自定义标题。

## 工具依赖与保真说明

本仓库提供技能指令和提示模板，不包含图像模型或可执行生成器。实际生成需要支持参考图片的图像生成或编辑工具，优先使用 Codex 可用的内置工具。

生成式处理可能改变上半部照片细节；若要求原片像素保真，需要单独生成下半部，再通过可用的图像合成工具拼接原照。未见的地下层次属于合理艺术重构。

CLI/API 备用方式仅在用户明确选择时使用，可能需要本地配置 API 密钥、依赖和网络，并产生 API 费用。不要将密钥提交到仓库。

## 独立发布

本效果独立维护版本。标签使用 `isometric-diorama-v<版本>`；本次为 `isometric-diorama-v1.5`，Release 标题为 `Isometric Diorama Poster v1.5`。发布时附上单效果安装 ZIP，具体步骤见 [发布指南](../../RELEASING.md)。

## v1.5：厚剖切基座、自然水陆延续与模型占位

模型必须有明显厚度的剖切基座，侧面和底缘在缩略图下也能辨认。基座自然延续地表材质，允许合理的土石及水下结构；水体可局部显露深度，不必强制为独立纯水块。保持照片中的水色、清澈程度和浑浊程度，禁止岩石包边及无关装饰底座。

模型大小提升为首轮构图优先项：先预留左侧文字，再确定右侧完整模型和阴影的占位。初始上限约为下半区宽度的 48%–52%、高度的 58%–64%，根据更严格的方向等比例缩小，不必填满。四边留白优先于细节密度。

示例已替换为用户选定的港湾、双湖与河谷三张参考图，用于展示自然材质、厚基座及不同水体表现；它们是视觉参考，不代表每张都达到像素级布局核验。严格等分和原片保真仍需最终检查，必要时合成。

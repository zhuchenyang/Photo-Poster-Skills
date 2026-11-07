# Photo to Isometric Diorama Poster

将照片转化为上方摄影画面、下方等距微缩场景的精致海报，默认配有英文编辑式文案。

当前版本：**v1.3**。

## 视觉规则

- 竖版 3:4，上下各占 50%。
- 下半部默认采用暖中性背景，左侧英文文案、右侧完整微缩模型。
- 文案包括眉题、主标题与两行辅助文字，随照片内容变化，保持安静、克制的语气。
- 先预留文字空间，再确定模型位置，必要时整体等比缩小；完整轮廓和阴影均需保留宽松留白。
- 保留土壤、岩石、植被、木材、砖石、混凝土等真实材质，剖面与场景地形相符。
- 用户可要求无字版本、其他语言或指定文案。

## 安装到 Codex

将本仓库克隆到 Codex 用户技能目录，文件夹名使用 `photo-to-isometric-diorama-poster`：

```powershell
git clone https://github.com/zhuchenyang/Photo-to-Isometric-Diorama-Poster.git "$env:USERPROFILE\.codex\skills\photo-to-isometric-diorama-poster"
```

若已设置 `CODEX_HOME`，请使用其 `skills` 子目录。已有同名技能时先备份，再更新以下三个文件。

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

# 按海报效果独立发布

每个 `posters/<技能名>/` 都是独立发布单元，集合仓库不设置统一版本。

## 发布步骤

1. 更新目标效果，核对其 `SKILL.md` 版本、`agents/openai.yaml` 展示名称及 README 版本一致；其他效果保持各自版本。
2. 更新该效果的示例与根 README 中的目录条目，并提交更改。
3. 从仓库根目录运行打包脚本，例如：

   ```sh
   python scripts/package_poster.py photo-to-isometric-diorama-poster 1.4.0
   ```

   版本参数必须与该技能的 `metadata.version` 一致。ZIP 位于 `dist/`，内部以技能名为唯一顶层目录，只包含所选效果。打包不会自动发布。

4. 在 GitHub 新建 Release，选择包含该效果更新的提交。当前等距微缩效果使用标签 `isometric-diorama-v1.4.0` 和标题 `Isometric Diorama Poster v1.4.0`。新效果使用自己的稳定前缀，避免不同效果标签冲突。
5. 说明仅针对本效果的变化、安装方法及依赖；上传生成的安装 ZIP。正式版不勾选 Pre-release；集合不维护统一 Latest 版本，后续发布取消“Set as the latest release”，以效果标签区分下载。
6. 核验标签提交、安装 ZIP 内容、下载链接和 README 引用。

## 历史版本

`v1.3` 是现有等距微缩海报效果的历史版本。保留标签和 Release，不重打标签，也不修改其历史源码快照。历史 Source code 包采用旧的仓库根目录布局，未来 Source code 包包含整个集合；用户应优先下载指定效果的安装 ZIP。

# 初期構成

## 目的

携帯とPCのどちらからでも指示・確認でき、PC停止中も実装・調査・監視が継続できるようにする。

## 役割

- 携帯・PCのChatGPT/Codex画面: 指示、承認、結果確認の操作盤。
- Google Drive `AI-Workspace`: 資料、メモ、依頼、取得原本、共有成果物の正本。
- ChatGPT Work Cloud: 調査、監視、定期実行を行う。
- Codex cloud: GitHubリポジトリからコードを取得し、実装、自己診断、テストを行う。
- GitHub `Mitsuru-sato37/ai-workspace-foundation`: コード、設定、手順、変更履歴の正本。
- ローカルPC: 必要なときに閲覧・編集する複製。常駐処理は持たせない。

## Google Drive構成

```text
AI-Workspace/
├── 00_Inbox/       携帯・PCから入れる未整理の依頼と資料
├── 10_Projects/    稼働中プロジェクトの資料
├── 80_System/      運用ルールと System Brief
└── 90_Archive/     終了済み資料
```

## 情報の流れ

1. 新しい依頼や資料を `00_Inbox` に入れる。
2. 継続案件だけ `10_Projects` に移し、プロジェクトごとの正本を決める。
3. 実装とテストはCodex cloudのリポジトリ環境で実行し、GitHubへ履歴を残す。
4. 調査・監視・定期実行はChatGPT Work Cloudに置き、Google DriveとGitHubの接続先から必要な情報を読む。
5. 共有する成果物はGoogle Driveへ保存し、完了した資料を `90_Archive` に移す。

## クラウド移行の完了判定

Codex cloud環境で`uv sync`、`uv run project doctor`、`uv run pytest`を実行し、対象リポジトリ・設定値・テスト件数を確認する。別途、ChatGPT Work Cloudのタスクを携帯から開始または確認し、PC停止中でも継続することを確かめる。設定文書だけの変更は移行完了に含めない。

## 採用しない構成

Obsidianは現時点の中心にはしない。Markdown編集には強いが、Google Driveと併用するとメモの正本が二つになり、携帯・PC間の共有経路が増えるため。必要になった時点で閲覧・編集用として再検討する。

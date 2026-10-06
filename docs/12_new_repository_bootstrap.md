# 新規リポジトリ初期化標準

## 目的

新しいGitHubリポジトリを作成した直後から、PCやCodexの会話履歴に依存せず、別PC・別セッションで作業を再開できる状態にする。

この手順は、利用者が新規リポジトリを作成し、その中身をChatGPT Work / Codexに作成させる場合の標準とする。

## 初期化完了条件

新規リポジトリの初期化は、少なくとも次の3ファイルが既定ブランチに存在するまで完了扱いにしない。

- `AGENTS.md`
- `docs/SPEC.md`
- `docs/STATUS.md`
- `git-status.cmd`
- `scripts/git-sync-status.ps1`

必要に応じて `README.md`、`.gitignore`、プロジェクト固有の仕様書や進捗文書も作る。

## Work / Codex が新規リポジトリを作るとき

1. 既存リポジトリや関連資料がないか確認する。
2. `templates/repository/` を初期構成の基準として読む。
3. テンプレートをそのまま複製せず、プロジェクト名・目的・技術・検証方法・正本となる仕様書に合わせて調整する。
4. `AGENTS.md` に、作業開始・終了・PC間引き継ぎのルールを残す。
5. `docs/SPEC.md` を固定の仕様入口にする。詳細仕様が別ファイルにある場合は、重複記載せずそこへの索引にする。
6. `docs/STATUS.md` を固定の引き継ぎ入口にする。既存の `PROGRESS.md` 等が正本ならそこへの索引にする。
7. 実装を始める前に、3ファイルが既定ブランチまたは作業ブランチに存在することを確認する。
8. 初期作業が完了したら、変更をcommit/pushし、別PCがGitHubだけを見て再開できる状態を確認する。

## 固定の読み順

各Codexセッションは原則として次の順で読む。

1. `AGENTS.md`
2. `docs/SPEC.md`
3. `docs/STATUS.md`
4. 上記から参照されるプロジェクト固有の仕様・進捗・決定記録

Codexのチャット履歴は正本にしない。

## STATUSに最低限残すもの

- 現在の作業ブランチ
- 完了したこと
- 次にやること
- 実行した検証
- ブロッカー / 外部依存
- ユーザー判断待ちがあればその内容

## 既存プロジェクト固有文書との関係

すでに `docs/PRODUCT_SPEC.md`、`docs/product-spec.md`、`docs/PROGRESS.md`、`docs/DECISIONS.md` 等がある場合、それらを消したり内容を二重管理したりしない。

- `docs/SPEC.md`: 仕様の固定入口として正本へ誘導する。
- `docs/STATUS.md`: 引き継ぎの固定入口として現在の進捗正本へ誘導する。

## テンプレート

初期構成の正本は次。

- `templates/repository/AGENTS.md`
- `templates/repository/docs/SPEC.md`
- `templates/repository/docs/STATUS.md`
- `templates/repository/git-status.cmd`
- `templates/repository/scripts/git-sync-status.ps1`

新規リポジトリの内容をWorkが作る場合も、このテンプレートを適用する。

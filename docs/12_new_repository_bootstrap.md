# 新規リポジトリ初期化標準

## 目的と完了条件

`Mitsuru-sato37` 配下に新しい独立アプリ・システムのGitHubリポジトリを作るとき、共通の開発運用ルールを一度の操作で適用できるようにする。初期構成の正本は `templates/repository/` とし、次の7ファイルが対象リポジトリに存在することを初期化完了条件とする。

- `AGENTS.md`
- `docs/SPEC.md`
- `docs/STATUS.md`
- `docs/DEBUG_STANDARD.md`
- `docs/DEBUG_MATRIX.md`
- `git-status.cmd`
- `scripts/git-sync-status.ps1`

## Windowsでの一括適用

1. 新規GitHubリポジトリを作成してPCへcloneする。
2. `ai-workspace-foundation` もcloneし、両方のcloneをPC上に置く。
3. PowerShellから次のコマンドを一度実行する。パスは実際の保存先に置き換える。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File 'C:\path\to\ai-workspace-foundation\scripts\initialize-repository.ps1' -RepositoryPath 'C:\path\to\new-repository'
```

スクリプトは `templates/repository/` から対象ファイルを適用し、最後に `verify-repository-bootstrap.ps1` を実行する。必須ファイルが不足していれば不足名を表示し、非成功終了する。

対象はローカルGit cloneとする。既存ファイルは既定で上書きせず、`PRESERVED` と表示する。既存内容をテンプレートと比較するには `-ExistingFileAction Diff` を使う。置き換えると決めたファイルだけを更新する場合に限り、`-ExistingFileAction Overwrite` を明示する。

完了条件だけを再確認する場合:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File 'C:\path\to\ai-workspace-foundation\scripts\verify-repository-bootstrap.ps1' -RepositoryPath 'C:\path\to\new-repository'
```

この方法はGitHub CLIの認証やAPI書き込みを必要としない。初期化後に対象cloneで `git status` を確認し、内容をプロジェクト固有の目的に合わせて調整してからcommit/pushする。

## 初期化ツールの検証

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\test-repository-bootstrap.ps1
```

検証では、必須ファイルがない状態での非成功終了と不足名の表示、完全な初期化後の成功、適用した7ファイルとテンプレート正本のSHA-256一致、既存ファイルの既定保持、差分表示、明示上書きを確認する。

## Codex / Workが新規Repoの内容を作るとき

1. 既存リポジトリや関連資料を確認する。
2. `templates/repository/` の7ファイルを対象Repoへ適用する。可能なら上記スクリプトを使う。
3. 既存ファイルがある場合は既定動作で保持し、差分を確認して明示的に処理する。
4. プロジェクト名・目的・技術・検証方法に合わせて内容を調整する。
5. `docs/SPEC.md` を仕様の固定入口、`docs/STATUS.md` を引き継ぎの固定入口にする。
6. `docs/DEBUG_STANDARD.md` は共通デバッグ基準、`docs/DEBUG_MATRIX.md` はプロジェクト固有の検証台帳として使う。
7. 7ファイルの存在確認に成功するまで初期化を完了扱いにしない。
8. 初期作業をcommit/pushし、別PCからGitHubだけで再開できる状態にする。

## 固定の読み順

各Codexセッションは原則として次の順で読む。

1. `AGENTS.md`
2. `docs/SPEC.md`
3. `docs/STATUS.md`
4. 上記から参照されるプロジェクト固有の仕様・進捗・決定記録

Codexのチャット履歴は正本にしない。

## 既存プロジェクト固有文書との関係

すでに `docs/PRODUCT_SPEC.md`、`docs/product-spec.md`、`docs/PROGRESS.md`、`docs/DECISIONS.md` 等がある場合、それらを消したり重複管理したりしない。`docs/SPEC.md` と `docs/STATUS.md` を固定入口にして、既存の正本へ誘導する。


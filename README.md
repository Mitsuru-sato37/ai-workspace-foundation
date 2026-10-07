# AI Workspace Foundation

`Mitsuru-sato37` 配下の各GitHubリポジトリで共通利用する開発運用基盤・テンプレートです。新しいアプリや独立システムのリポジトリには、ここで定める共通ルールと初期ファイルを適用します。

コード、仕様、開発手順の正本は各GitHubリポジトリです。このリポジトリは **Public** で、共通標準と再利用可能なテンプレートを公開・管理します。Google Driveは画像・動画・Sheets・実データなど、GitHubで管理しない素材を置く補助領域です。Driveをコードや仕様の正本にはしません。

## 新規リポジトリを初期化する

Windowsで対象リポジトリをcloneした後、このリポジトリのcloneから次を1回実行します。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\initialize-repository.ps1 -RepositoryPath 'C:\path\to\new-repository'
```

不足している共通ファイルだけを `templates/repository/` から適用し、最後に必須7ファイルを検証します。既存ファイルは既定で保持します。既存内容を確認する場合は `-ExistingFileAction Diff`、テンプレートで明示的に置き換える場合は `-ExistingFileAction Overwrite` を指定します。

単独で完了条件を確認するには次を実行します。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\verify-repository-bootstrap.ps1 -RepositoryPath 'C:\path\to\new-repository'
```

初期化ツール自身の正常系・異常系・テンプレート一致確認は次で実行できます。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\test-repository-bootstrap.ps1
```

## このリポジトリ自身の開発環境

このリポジトリ自身はPython 3.12、uv、pytestを使います。

```powershell
uv sync
uv run project doctor
uv run pytest
```

初期化の標準手順は [`docs/12_new_repository_bootstrap.md`](docs/12_new_repository_bootstrap.md) を参照してください。


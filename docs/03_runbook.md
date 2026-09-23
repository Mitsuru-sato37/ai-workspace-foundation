# 再現手順書

更新日: 2026-09-23

## 初期化

1. `rg --files -uu` で既存ファイルを検索する。この作業では0件だった。
2. 0件だけで空と断定せず、`Get-ChildItem -Force -Recurse` で隠し項目とディレクトリを再確認する。`outputs/` と `work/` のみを確認した。
3. 既存物を残したまま、`data/raw/`、`data/processed/`、`docs/`、`src/`、`tests/` を追加した。
4. `AGENTS.md`、プロジェクト開始時の設計、データ取得経路の採用判断、最小データ契約を保存した。

## 構成検査

検査器は `src/validate_project.py`。先に `--self-test` が規約2〜7の欠落したメモリ上の偽物を検出することを確認し、その後に実物を検査する。

通常環境:

```powershell
python -X utf8 src\validate_project.py --self-test
python -m py_compile src\validate_project.py
```

この作業環境では上の `python` がコマンド未登録で失敗した。Windowsランチャー `py` も未登録で同様に失敗した。成果物は変更されていない。アプリ同梱Pythonの場所を確認し、次で再実行した。

```powershell
& 'C:\Users\msato\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -X utf8 src\validate_project.py --self-test
& 'C:\Users\msato\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m py_compile src\validate_project.py
```

期待結果は、自己検査が壊れた規約を検出し、実物の検査が `OK` になること。Python実行パスはアプリ更新で変わり得るため、見つからない場合は先にワークスペース依存関係の現在値を確認する。

## Google Drive操作盤の作成

1. My Drive直下を一覧し、検索対象がGoogle Drive内であることを確認した。
2. `AI-Workspace`、`AI Workspace`、`AIワークスペース`、`Project Brief`、`プロジェクト概要` の表記ゆれで検索した。
3. 前者4件は0件だったため、別経路としてMy Drive直下一覧と `プロジェクト概要` の検索結果2件を実際に開いて確認した。2件は既存PDFで、今回の操作盤ではなかった。
4. `AI-Workspace` と4つの子フォルダを作り、`80_System` にネイティブGoogleドキュメント `00_System Brief` を保存した。
5. 作成後に再取得し、子フォルダ4件、System Brief 1件、本文の必須語句6件を個別に検査した。
6. 検査器自体は、存在しないフォルダIDを与えたときに失敗を返すことで検出能力を確認した。

## ローカル基盤の検証

`project doctor` は `config/project.toml` をTOMLとして読み、設定値と4つの保存先を個別に検査する。`tests/test_settings.py` は正常値、プロジェクト外パス、必須テーブル欠落を別々に判定する。

検証器の確認では、`_inside` のプロジェクト外パス拒否を一時的に外し、3件中 `test_rejects_path_outside_project` の1件だけが失敗することを確認した。その後に拒否処理を戻し、3件すべてを再実行する。意図的な失敗は削除せず、この手順に残す。

uvが未導入の間は、アプリ同梱Pythonで標準ライブラリ互換テストを実行する。uv導入後の正式な再現手順はREADMEの3コマンドに統一する。

uv 0.12.18を公式Astralインストーラーでユーザー領域へ導入し、`uv sync` でPython 3.12の `.venv` と `uv.lock` を生成した。最初の `uv sync --locked` はサンドボックスからユーザーキャッシュへアクセスできず停止したため、ユーザー領域へのアクセス許可付きで再実行した。続くdoctorと3テストは成功したが、Ruffが書式5件を検出したため、手修正して全工程を再実行する。

Git初期化後は、サンドボックスと実ユーザーで `.git` の所有者判定が逆になり、Gitのdubious ownership安全機構が停止させた。グローバルな `safe.directory` は変更せず、各Gitコマンドにこのリポジトリの絶対パスだけを指定した。除外確認では `git check-ignore -v` が否定規則も成功終了するため `.gitkeep` を誤判定したので、`git status --untracked-files=all` の実体件数へ切り替えた。ステージ対象24件、禁止対象0件を確認した後、既存文書2件の末尾余分空行を修正した。

GitHubに非公開リポジトリ `Mitsuru-sato37/ai-workspace-foundation` を作成し、画面上の `Private` 表示と空リポジトリ用HTTPS URLを確認した。ローカル設定へ同じリポジトリ名を反映し、doctorでGitHub接続先が設定済みになることを確認してからpushする。

## 次回の開始地点

uvを導入して `uv.lock` を生成し、同一のdoctorとテストが隔離環境でも通ることを確認する。その後、非公開GitHubリポジトリを作り、`config/project.toml` の接続先を確定する。どちらもインストールまたは外部作成を伴うため、実行前に利用者の確認を取る。

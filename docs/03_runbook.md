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

GitHub CLI認証後、ローカルHEADと `refs/heads/main` を別々に読み、SHA一致とahead/behind `0/0` を確認した。GitHubプラグインでは当初リポジトリ一覧0件・個別取得404だった。GitHub設定を確認すると、`ChatGPT Codex Connector` はOAuth認証済みだが、GitHub Appとしてはアカウントへ未インストールだった。全リポジトリ許可は使わず、`Mitsuru-sato37/ai-workspace-foundation` の1件だけを選んでインストールした。再取得では、一覧1件、`visibility=private`、default branch `main`、README本文の取得成功を個別に確認した。

## 2026-09-24: クラウド実行へ方針を修正

利用者の目的は、PC停止中も携帯から依頼と結果確認ができることだった。初期の「ローカルで実装・検証し、調査だけクラウド」という方針では、この目的を満たさない。公式仕様を確認し、Codex cloudはGitHubリポジトリからクラウド環境を作って実装・検証でき、ChatGPT Work CloudはPC停止中も継続できることを確認した。

`AGENTS.md`、README、構成文書、TOMLの実行設定をクラウド実行へ修正した。Python・uv・pytestはCodex cloudでの再現手段として残す。`project doctor`は`execution_mode=cloud`と`local_required=false`を表示する。過去のローカル作業は失敗と変更の経緯を追えるよう、この文書に残す。

Google Driveの`00_System Brief`も読み直すと、Codex Remoteを実装の担当とし、GitHubリポジトリが0件という古い記述が残っていた。該当6箇所を文単位で更新し、各箇所の置換件数が1件、再取得後の旧記述が0件、リスト項目が20件のままであることを確認した。既存Google Docの初回読み取り用補助スクリプトはWindowsの絶対パスに非対応で停止したため、コネクタの全文取得で文書構造を確認してから対象行のみを更新した。

検証時、通常の`uv`コマンドはPATH未登録で失敗した。実体の`uv.exe`は見つかったが、ユーザーキャッシュへのアクセス権がなく、このサンドボックスからは実行できなかった。既存`.venv`も元のPython実行ファイルを参照して起動できなかった。代わりにアプリ同梱Pythonで標準ライブラリの単体テストを実行した。この代替はクラウド環境の検証にはならないため、未完了として扱う。

テストは変更前に`execution_mode`欠落とローカル実行の誤受理を検出した。修正後は4件が通過し、Ruffは0件、構成検査は12対象を確認した。TOMLは`pyproject.toml`、`config/project.toml`、`uv.lock`を個別にパースし、プロジェクト名がすべて`ai-workspace-foundation`で一致することを確認した。`project doctor`は4保存先とクラウド実行設定を読み取った。ただし、これらはローカルの静的・単体検査であり、クラウド稼働の証拠ではない。

Codex cloudの環境作成前試験では、Python 3.12.13と`uv sync --frozen`による7パッケージの導入まで成功した。しかし`uv run project doctor`が`missing_paths=["outputs"]`で失敗した。Gitは空の`outputs/`を保存しないのに、自己診断がそのディレクトリを必須としていたため。`.gitignore`に`!outputs/.gitkeep`を加えて空フォルダを保持する修正を行い、クラウドで再試験する。

## 次回の開始地点

GitHubの最新コードをCodex cloud環境に接続し、`uv sync`、`uv run project doctor`、`uv run pytest`をクラウドで実行する。次にChatGPT Work Cloudの小さなタスクを携帯から確認し、PC停止中も継続することを検証する。両方の実行結果を確認するまで、クラウド移行完了とは報告しない。

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

修正後のGitHubコミット`0ebb4cc8a2c762abda3cd11ed0caa52d0c6928af`をCodex cloud環境`ai-workspace-foundation`で取得した。自動セットアップはPython 3.12.13と`uv sync --frozen`で7パッケージを導入し、`uv run project doctor`は`status=ok`、`execution_mode=cloud`、`local_required=false`、4保存先、欠落0を返した。別の新しい試験端末で`uv run pytest`を実行し、4件が通過した。これでコードのクラウド実行は確認できた。携帯からの実操作とPC停止中の継続は、端末を停止する実機試験が未実施のため別に確認する。

## 次回の開始地点

携帯からCodex cloud環境とChatGPT Work Cloudへアクセスし、PC停止中に依頼・結果確認を実機で検証する。監視対象と頻度が決まったらWork Cloudで定期タスクを作る。クラウド環境でのコード実行は確認済みだが、携帯・PC停止中の操作は確認まで完了と報告しない。

## 2026-09-24: アイデア受付の追加

既存の `00_Inbox` とクラウドの役割分担を流用し、思いつきを実行依頼と分けて保存する手順を `docs/11_idea_intake.md` に定めた。個々のメモをGitHubにも置く案は正本が二つになるため採用せず、Google Driveを唯一の正本とした。担当はキーワードで機械的に一つへ決めず、成果物からCodex cloud、継続調査からChatGPT Work Cloud、不可逆操作から人の操作へ工程単位で分ける。

構成検査の必須文書へ同手順を追加した。検査器の確認では、一時ディレクトリに必須構成を複製して `docs/11_idea_intake.md` だけを除いた状態を検査し、同文書の欠落を1件として検出することを確認する。その後、実物に対して自己検査、構成検査、pytest、Ruffを実行する。Google Driveへの書き込みは外部操作であり、この環境にはDrive操作手段もないため実施していない。

## 2026-09-24: 利用目的と最初の稼働案件を具体化

利用者が実際にやりたいことは、個人用アプリ開発、競馬データ分析、相談しながら具体化するその他の案件の3領域だった。抽象的なアイデア受付だけでは目的を表せていなかったため、3領域を基盤の対象として明記し、既存の「めしルーレット」のブラッシュアップを最初の稼働案件にした。

既存物を読むため、公開URLをブラウザ取得、`curl`取得、推定公開リポジトリ `https://github.com/revise-sato/meshi-roulette.git` の参照とcloneという別経路で試した。ブラウザ取得は401、直接取得は環境のCONNECTトンネルが403を返し、画面とソースの取得前に停止した。取得できていない内容を推測で評価せず、最初の完了条件を「公開画面とソースを取得し、現状、再現手順、改善候補、検証方法を整理する」とした。ソースを取得できるCodex cloud環境で同じURLを開くところから再開する。

# 共通標準の横断反映手順

## 目的

共通標準を変えたときに、基盤リポジトリだけを直して完了にしない。影響する新規テンプレートと既存リポジトリを洗い出し、各リポジトリの目的を保ちながら反映し、結果をこの台帳へ残す。

## 手順

1. `AGENTS.md`、`docs/SPEC.md`、`docs/STATUS.md` と、変更対象の正本を読む。今回の標準の正本、旧方針、変更理由を特定する。
2. GitHubの対象アカウントでリポジトリ一覧を取得し、件数、公開範囲、default branch、アーカイブ状態を確認する。検索結果だけで全件と判断しない。アクセスできない範囲は未確認として記録する。
3. 変更する共通標準ごとに、影響を受けるテンプレート・リポジトリ・文書を列挙する。各リポジトリの `AGENTS.md` と仕様・状態文書を読み、既存の用語、正本、プロジェクト固有ルールと矛盾しない反映方法を決める。
4. リポジトリごとに作業ブランチを作り、影響する文書だけを更新する。共通ルールとプロジェクト固有ルールが競合するときは、固有の正本を確認して両者の適用範囲を明記する。既存ファイルを機械的にテンプレートで上書きしない。
5. Publicリポジトリへ書く前に、内容と差分が公開可能か確認する。非公開のアイデア、個人情報、非公開資料のタイトル・リンクはPublicリポジトリへ書かない。必要な場合はプロジェクト専用の非公開保存先を正本にし、公開側に存在を推測できる情報を置かない。
6. 既存メモの移行では、対象・件数・新しい正本を一件ずつ照合する。Driveの原本を削除・上書きする必要がある場合は、明確な許可があるまで原本を保持し、移行未完了として台帳に残す。
7. 変更をPRにし、目的、適用範囲、公開範囲、検証結果、移行保留を記録する。default branchに入ったことを確認してから、そのリポジトリを「反映済み」とする。
8. 対象リポジトリ数と台帳行数を照合し、対象すべてが「反映済み」または理由付きの「対象外」になるまで全体作業を完了にしない。外部依存・未承認操作が残る場合は、未完了の範囲と必要な次の操作を明記する。

## アイデア保存標準の今回の適用範囲

プロジェクト固有のアイデアは対象プロジェクトのリポジトリを正本とする。Publicリポジトリには公開可能な内容だけを置く。非公開の企画はプロジェクト専用の非公開保存先に置く。共通ルール・テンプレートのアイデアと所属先未定の仮メモは `AI-Workspace/00_Inbox` に置き、所属先が決まったら一つの正本へ移す。

新規リポジトリには `templates/repository/AGENTS.md` でこの標準を適用する。既存リポジトリは下表で確認・反映状態を管理する。PRがマージされるまでは反映済みと数えない。

| Repository | Visibility | 影響文書 | 状態 | 根拠・保留 |
| --- | --- | --- | --- | --- |
| `Mitsuru-sato37/ai-workspace-foundation` | public | `AGENTS.md`, `templates/repository/AGENTS.md`, `docs/03_runbook.md`, `docs/10_architecture.md`, `docs/11_idea_intake.md`, `docs/README.md`, `docs/SPEC.md`, `docs/STATUS.md`, `docs/14_shared_standard_rollout.md` | [PR #11 merged](https://github.com/Mitsuru-sato37/ai-workspace-foundation/pull/11) (`f7e590a`) | 基準文書・配布テンプレート |
| `Mitsuru-sato37/meshi-roulette` | public | `AGENTS.md`, `docs/STATUS.md` | [PR #8 merged](https://github.com/Mitsuru-sato37/meshi-roulette/pull/8) (`9e08c34`) | プロジェクト固有の公開可能なアイデアだけを記録 |
| `Mitsuru-sato37/poker-gto-trainer` | public | `AGENTS.md`, `docs/STATUS.md` | [PR #3 merged](https://github.com/Mitsuru-sato37/poker-gto-trainer/pull/3) (`a807341`) | プロジェクト固有の公開可能なアイデアだけを記録 |
| `Mitsuru-sato37/keiba-lab` | private | `AGENTS.md`, `docs/STATUS.md` | [PR #36 merged](https://github.com/Mitsuru-sato37/keiba-lab/pull/36) (`676dc9f`) | 非公開リポジトリ |
| `Mitsuru-sato37/simpsons-team-os` | public | `AGENTS.md`, `docs/STATUS.md` | [PR #16 merged](https://github.com/Mitsuru-sato37/simpsons-team-os/pull/16) (`5d485b6`) | 非公開のチーム情報・企画詳細は記録しない |
| `Mitsuru-sato37/settlement-app` | public | `AGENTS.md`, `docs/STATUS.md` | [PR #5 merged](https://github.com/Mitsuru-sato37/settlement-app/pull/5) (`26b8f20`) | プロジェクト固有の公開可能なアイデアだけを記録 |
| `Mitsuru-sato37/chunichidragons-data-analysis` | public | `AGENTS.md`, `docs/STATUS.md`, `docs/repository_workflow.md`, `docs/drive_github_workflow.md`, `docs/video_idea_index.md` | [PR #1 merged](https://github.com/Mitsuru-sato37/chunichidragons-data-analysis/pull/1) (`69b5bf4`) | 既存Drive企画メモは原本に触れず旧正本として保持。新規候補はリポジトリ正本へ切り替える |

基盤を含む7件すべてのPRを各記録済みbase branchへマージし、GitHub上で `merged=true` とマージSHAを確認した。中日分析リポジトリの既存Drive企画メモは非公開詳細を含むため、Drive原本は変更せず、Publicリポジトリへ本文やリンクを移していない。

## 完了確認（2026-11-02）

- 7件すべてでPRのbase branchとマージ状態を確認し、レビュー投稿・未解決スレッドがないことを確認した。
- `meshi-roulette` は `test-and-build` 2件が成功。残る6件はチェック実行結果が報告されなかった。今回の変更は文書のみのためテストは実行していない。
- Chuniの既存Driveメモは非公開の正本としてそのまま保持。公開側の現行文書に非公開Driveのタイトル・リンク・識別子がないことを確認した。
- PRが既定ブランチへ入ったことをもって横断反映を完了とする。ブランチ保護の必須チェック設定は接続ツールから確認できなかったため、チェックが報告されなかった6件については「チェック未報告」として記録する。

## 検証

- 反映対象ごとに差分を読み、共通標準が含まれ、プロジェクト固有のルールが残っていることを確認する。
- 新旧方針を検索し、現行文書に矛盾した指示が残っていないことを確認する。歴史記録であることが明示された旧決定は除く。
- Publicリポジトリの差分に非公開情報や非公開Driveのタイトル・URLが含まれていないことを確認する。
- PRのbase/head、merge状態を確認する。PRが開いているだけでは反映完了としない。

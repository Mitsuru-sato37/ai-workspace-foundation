# 総合デバッグ運用標準

## 目的

自作アプリごとに毎回デバッグ方法を考え直さず、Codexへ「総合デバッグして」と依頼すれば、同じ品質基準で検証・修正・記録・GitHub保存まで進められる状態を標準化する。

## 新規リポジトリ

`docs/12_new_repository_bootstrap.md` に従い、最初から次を持たせる。

- `AGENTS.md`
- `docs/SPEC.md`
- `docs/STATUS.md`
- `docs/DEBUG_STANDARD.md`
- `docs/DEBUG_MATRIX.md`
- `git-status.cmd`
- `scripts/git-sync-status.ps1`

実装が進んだら `docs/DEBUG_MATRIX.md` の汎用行を、アプリ固有の主要フロー・異常系・境界値へ置き換える。

## Codexへの通常指示

原則として、ユーザーは次の短い指示だけでよい。

> このアプリを総合デバッグして。

Codexは `AGENTS.md` のルールに従い、仕様・標準・マトリクス・既存テストを読んでから、ベースライン確認 → 不足ケース追加 → 再現 → 修正 → 回帰確認 → 全体検証 → 記録 → commit / push の順で進める。

個別の長いデバッグプロンプトを毎回作成する運用には戻さない。

## 既存リポジトリ

既に `DEBUG_STANDARD.md` と `DEBUG_MATRIX.md` がある場合は、それを正本として更新する。
無い場合は、次回の総合デバッグ開始時にテンプレートを導入してから検証する。

## 実機確認

Codexでブラウザー幅や自動テストまで確認し、iOS / Android の実端末依存事項だけ人が最終確認する。

人の確認が必要な代表例:

- ソフトキーボード
- Safari / Chrome固有挙動
- ホーム画面追加
- タップ感、スクロール感
- OS共有UI
- 実端末の権限ダイアログ

実機未確認は失敗ではないが、`DEBUG_MATRIX.md` に未確認として残す。

## CI

test / typecheck / lint / build のコマンドが確定したプロジェクトでは、GitHub Actions等でPR時の自動検証を追加する。
技術構成が異なるため、共通テンプレートに固定コマンドは持たせない。

## 完了判定

`docs/DEBUG_STANDARD.md` の完了条件を満たし、Critical / High の既知未修正バグが0件なら総合デバッグ完了とする。

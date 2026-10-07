# Debug Matrix

Status: Not tested  
Last updated: YYYY-MM-DD

共通基準は `docs/DEBUG_STANDARD.md`、仕様は `docs/SPEC.md` とそこから参照される正本を参照する。

## Verification commands

プロジェクトで実際に使うコマンドだけを書く。存在しない検証を仮定しない。

| 種類 | コマンド | 最新結果 |
|---|---|---|
| Test | TBD | NOT TESTED |
| Typecheck | TBD / N/A | NOT TESTED |
| Lint | TBD / N/A | NOT TESTED |
| Production build | TBD | NOT TESTED |
| E2E | TBD / N/A | NOT TESTED |

## P0: 主要フロー

実装開始後、壊れたら利用不能になる主要フローを具体的に記入する。

| 領域 | シナリオ | 期待結果 | 自動化 | 状態 |
|---|---|---|---|---|
| 起動 | 初回起動 | 主要画面が利用可能 | TBD | NOT TESTED |

## P1: 異常系・境界値・状態遷移

プロジェクト固有のケースを追加する。

| 領域 | シナリオ | 期待結果 | 自動化 | 状態 |
|---|---|---|---|---|
| 入力 | 空入力 | 仕様どおり安全に扱う | TBD | NOT TESTED |
| 入力 | 長い入力 | 致命的なUI崩れや状態破損がない | TBD | NOT TESTED |
| 連続操作 | 主要CTAを連打 | 多重実行で状態を壊さない | TBD | NOT TESTED |
| 状態遷移 | 処理中に条件変更 | 古い結果で新状態を上書きしない | TBD | NOT TESTED |
| 永続化 | 壊れた保存データ | 起動不能にならず安全に扱う | TBD / N/A | NOT TESTED |
| 外部依存 | 0件 / 失敗 / 遅延 | 条件を勝手に変えず安全に説明する | TBD / N/A | NOT TESTED |

## P2: UI / 実機

| 環境 | 確認内容 | 状態 | 備考 |
|---|---|---|---|
| 320px | 横はみ出し、主要CTA、スクロール | NOT TESTED | |
| 375px | 主要操作 | NOT TESTED | |
| 390px | 主要操作 | NOT TESTED | |
| PC | 主要操作 | NOT TESTED | |
| iOS実機 | Safari、ソフトキーボード、タップ | NOT TESTED | |
| Android実機 | Chrome、ソフトキーボード、タップ | NOT TESTED | |

## Known bugs

| 重要度 | 概要 | 状態 | 再現テスト |
|---|---|---|---|
| - | なし / 未調査 | - | - |

## Latest comprehensive debug run

- Branch: TBD
- Commit: TBD
- Test: NOT TESTED
- Typecheck: NOT TESTED / N/A
- Lint: NOT TESTED / N/A
- Build: NOT TESTED
- Critical / High unresolved: UNKNOWN
- Manual / device checks remaining: TBD
- External dependencies remaining: TBD

## 判定

- **PASS**: 仕様どおりで再現性あり
- **FAIL**: 仕様と異なる
- **BLOCKED**: 外部依存等で確認不能
- **NOT TESTED**: 未確認
- **N/A**: このプロジェクトでは対象外

Critical / High の FAIL が残っている状態では総合デバッグ完了にしない。

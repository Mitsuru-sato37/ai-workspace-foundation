# 最小データ契約

## 予測時点

`prediction_cutoff = scheduled_start_at - 10 minutes` とする。入力行は、その版の `available_at` が `prediction_cutoff` 以下の場合だけ利用できる。時刻はすべてタイムゾーン付きで保存し、日本開催は `Asia/Tokyo` とする。

## 主キーとテーブル

### races

主キー: `race_id`

| 列 | 型 | 制約・意味 |
|---|---|---|
| race_id | string | JV-Dataの開催年・場・回・日・競走番号から決定的に生成 |
| scheduled_start_at | timestamp | 発走予定。変更のたびに原本の版を残す |
| race_date | date | 開催日 |
| course_code | string | 競馬場コード |
| race_number | integer | 1以上 |
| surface | enum | turf / dirt |
| distance_m | integer | 0より大きい |
| track_condition | string nullable | 予測締切までに観測できた版だけを入力に使用 |
| available_at | timestamp | この版を利用可能になった時刻 |
| acquired_at | timestamp | 実際に取得した時刻。`available_at <= acquired_at` |

### runners

主キー: (`race_id`, `horse_number`)

| 列 | 型 | 制約・意味 |
|---|---|---|
| race_id | string | racesに存在 |
| horse_number | integer | 1以上、同一レース内で一意 |
| horse_id | string | 血統登録番号等の公式ID |
| horse_name | string | 表示・監査用。結合キーには使わない |
| gate_number | integer | 1以上 |
| carried_weight_kg | decimal | 0より大きい |
| jockey_id | string | 公式ID |
| trainer_id | string | 公式ID |
| body_weight_kg | integer nullable | 締切前に発表された版だけ使用 |
| scratched | boolean | 締切時点の状態 |
| available_at | timestamp | この版を利用可能になった時刻 |
| acquired_at | timestamp | 実際に取得した時刻 |

### win_odds_snapshots

主キー: (`race_id`, `horse_number`, `observed_at`)

| 列 | 型 | 制約・意味 |
|---|---|---|
| race_id | string | racesに存在 |
| horse_number | integer | runnersに存在 |
| observed_at | timestamp | オッズの観測時点 |
| win_odds | decimal | 1以上 |
| acquired_at | timestamp | 実際に取得した時刻。`observed_at <= acquired_at` |
| source_record_type | string | 初期値は `0B41` |

予測入力には `observed_at <= prediction_cutoff` を満たす最新の1行だけを使う。該当行がない出走馬をゼロや確定オッズで補完せず、そのレース全体をオッズベースラインの評価対象外とする。

### results

主キー: (`race_id`, `horse_number`)

| 列 | 型 | 制約・意味 |
|---|---|---|
| race_id | string | racesに存在 |
| horse_number | integer | runnersに存在 |
| finish_position | integer nullable | 確定着順。取消・除外・中止はnullと理由コードを持つ |
| result_status | enum | finished / scratched / excluded / did_not_finish |
| payout_win_yen_per_100 | integer nullable | 確定払戻、評価専用 |
| confirmed_at | timestamp | 結果確定後。必ず予測締切より後 |

`results` はラベル生成と評価以外から参照禁止とする。特徴量の生成関数は `results` を引数に取らない。

## 受入検査

1. 全行で主キーが非nullかつ一意。
2. 全外部キーが参照先に存在する。
3. 使用した全特徴量で `available_at <= prediction_cutoff`。
4. 各レースの予測確率合計は許容誤差 `1e-9` 以内で1。
5. 評価対象レース数 = 一様ベースライン対象数 = 候補モデル対象数。オッズベースラインは欠測除外数を別掲する。
6. 学習期間の最大開催日 < 検証期間の最小開催日。
7. 分割前全件 = 学習 + 検証 + 保留であり、未所属は0件。

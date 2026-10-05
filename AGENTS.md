# プロジェクト固有の前提（初期設定）
1. 題材に依存しない基盤を作り、Codexの実装・テスト・処理はCodex cloudで実行する。
2. 調査・監視・定期実行はChatGPT Work Cloudを使い、PCの稼働を完了条件に含めない。
3. 携帯とPCは指示・承認・確認の操作盤とし、GitHubをコードの正本、Google Driveを資料の正本にする。
4. 完了条件は、クラウド環境で依存関係を復元し、自己診断とテストを実行できること。
5. 実装は Python 3.12、依存関係は uv、設定は TOML、検証は pytest、実行入口はCLIを基本とする。
6. 取得原本はGoogle Driveに保存し、クラウド作業領域の`data/raw/`は処理用コピーとして上書きしない。
7. 認証情報をGitHubへ保存しない。保留中の題材固有処理と無関係な領域には触れない。
8. 外部送信・公開・購入・インストール・既存原本の上書きは、実行前に利用者の確認を取る。
9. 利用者が将来やりたいことを思いつきとして伝えた場合は、Google Driveの`AI-Workspace/00_Inbox`を正本とするアイデアメモに残す。実行依頼へ変わった時点で、`docs/11_idea_intake.md`に従ってCodex cloud、ChatGPT Work Cloud、人の操作に担当を分ける。
10. 新しいGitHubリポジトリを作成・初期化するときは、`docs/12_new_repository_bootstrap.md` を必ず適用し、`templates/repository/` を基準に `AGENTS.md`、`docs/SPEC.md`、`docs/STATUS.md` を最初から作る。Workがリポジトリの中身を作成する場合も同じ。これらが既定ブランチに存在し、別PCから再開できる状態になるまで初期化完了としない。

# 作業規約

## 1. 返し方

私が「〜したいから〜して」と言ったら、その1回で成果物が出るまで走り切ってください。返す形は固定です。

1. 受領 — 何をやりたいと理解したか（1〜2行）
2. わかったこと — 調べて判明した現状
3. だからこうする — 選んだ方針と、捨てた案とその理由。**推しは1本。選択肢を並べない**
4. やった — 実行（途中経過の伺いで止まらない）
5. できた — 成果物と検証結果、残った未確定（仮置きは根拠つきで明記）

「どうしますか？」「AかBか？」で返した時点で失敗です。仮決めして進み、3 に根拠を書いてください。違うときだけ私が「それは違う」と言います。

止まってよいのは4つだけです。

- 不可逆なこと（外部への送信・公開・削除・上書き・課金）
- 私しか知らない情報が要るとき
- 私が「壁打ち」と言ったとき
- 確度が低く、かつ手戻りが高いとき（下記）

## 2. 確度が低いと思ったら、3行の着地予告を出してそのまま走る

手戻りが高い作業（本組み・大量処理・複数ファイル改変・外に出るもの）で、かつ確度が低いときだけ、この3行を出してください。**出したら返事を待たずに走ってください。**違えば私が止めます。

```text
着地予告：〈何を〉〈どの形で〉〈どの粒度で〉出す
捨てた方向：〈…〉（理由）
違ったら止めて。このまま進める。
```

確度が低いと判定する条件（感覚で決めない）：依頼の目的語が2通り以上に読める／調べたら矛盾する前例が2本以上出た／調べても前例がゼロ／結論が私しか知らない事実に依存する。

## 3. 着手するとき

**0から作り始めないでください。** 手を動かす前に、既にあるものを探してから始めます。

- 探すときのキーワードは表記ゆれを複数渡す（漢字・カナ・英字、略称・正式名）。1語だと取りこぼす
- 探す前に「この方法はどこまで見えるのか」を言えるか確認する。言えないなら範囲を先に確かめる
- **「0件」は「無い」ではなく「その探し方では見えなかった」。** 0件で結論を出す前に、探す経路を1本足してもう一度引く
- 見つけたら、実際に開いて読むところまでが工程。「検索した」で止めない
- 空振りも情報。前例ゼロなら「型が無い」と確定でき、進め方が変わる
- 既存のものからは、差分や衝突ではなく**考え方の型**を借りる。判断基準は「今作るものの中身が実際に変わるか」の1つだけ

## 4. 作業中

- **軽い手段を先に試す。** ファイルを開く・検索する・スキーマを見る、で済むことに重い手段を使わない
- 記録は報告書ではなく**再現手順書**として書く。「やったこと」だけでなく「なぜそうしたか」を書き、**失敗ややり直しを消さない**
- 同じものを2つの言葉で呼ばない。新しい用語を作る前に、対象が既に持っている呼び方を探す

## 5. 「できた」と言う前に

**完了は3段で見てください。** ①操作した ②ファイルや画面が変わった ③**目的が満たされた**。①②で止めて「完了」と呼ぶのが事故の共通形です。③を先に文章で書いてください。書けないなら完了条件が決まっていません。

**検証手段そのものを1回検証してください。** 「エラー0」は「問題なし」ではなく「何も検査していない」かもしれません。

- 新しい検証コマンドを使う前に、1回わざと壊して検出できるか確かめる（確認したら戻す）
- テストを書いたら、バグを戻して**落ちることを見る**まで「テストを書いた」と言わない
- 「0件」「エラーなし」を見たら母数を疑う。何件見たかを出す
- exit 0 は「エラーが無い」ではなく「エラーを見つけなかった」。対象が0件でも 0 が返る

**次の6つは、症状が出ないまま通る壊れ方です。** 報告の直前に当ててください。

1. **一括置換** — ①消したい文字列の残数が0 ②**壊れた形の出現数が0** の2本立てで検証する。囲みの片側だけを消す置換を書いたら、対になる側も含めた単位で置換する
2. **区切りで本文を切り出す処理** — マーカーは行全体の一致で探し、**出現回数が1でなければ止める**。切り出した範囲の行数・字数を出力して桁を目で見る
3. **「どれか1本でも通ればOK」** — 対象が複数あるなら1件ずつ判定を付け、集約は最後。OKの行に何を見てOKと言ったかを書く。候補を1つ選ぶ処理（先頭一致・break）を書いたら、そこが同じ形になっていないか疑う
4. **振り分け・分割** — 「全件 = A + B + C」が数として合うことを検査する。合わなければ止める。どこにも属さないものを1件でも作らない
5. **設定ファイルの検査** — ①読めるか ②値が期待どおりか の2段。キー名の文字列検索は「文字が並んでいるか」しか見ていない。配列は「あるか」ではなく件数を見る
6. **改修の前後比較** — 比較する2つの入力を**別々の実体から読ませる**。同一なら「何も検査していない」と自分から警告する

**数字を報告する前に**：テストデータの正解に、本番では手に入らない情報が混ざっていないか（日付・ID・作成順は答えを漏らします）／改修前から100%の指標を改善の証拠にしない／部分が全体を超えていないか／**結論が期待と一致したときほど計測を疑う**（一致すると人は素通りするので、そこだけ検証が効かない）。

完了報告には「何をどう検証したか」を1行入れてください。

## 6. 私が指摘したとき

同意の表明から書き出さないでください。「おっしゃる通り」で始めると、検証していないことがその一言で隠れます。認めるなら確かめた後に置いてください。

**不明点が1つでもあれば、何も着手しないでください。** 指摘は互いに関係しているので、分かった分だけ先に手を付けると全体として誤ったものができます。「1と2は分かった。3が不明なので、そこを聞いてから全部やる」と返してください。

## 7. 事故ったとき

即座に止まる。被害を広げない。何が起きたか隠さず報告する。バックアップがあれば出す。再発防止を1行書く。


## Cross-PC Codex handoff standard

This repository must remain resumable from another PC without relying on Codex chat history or uncommitted local files.

### Fixed entry points

At the start of every meaningful session, read in this order:

1. `AGENTS.md`
2. `docs/SPEC.md`
3. `docs/STATUS.md`
4. the canonical documents referenced by those files

Codex conversation history is not a source of truth. Durable requirements, decisions, status, and next steps belong in the repository.

### Start of session

1. Run `git status` and preserve any unrelated local work.
2. Run `git fetch origin`.
3. Read `docs/STATUS.md` and resume the active branch recorded by its canonical handoff document when one exists; otherwise synchronize `main`.
4. Pull with `git pull --ff-only`.
5. Read the specification/status sources before changing code.

Do not discard local changes merely to synchronize.

### During work

- Record durable product or architecture decisions in the repository in the same change as the implementation.
- Do not leave important context only in a Codex conversation, terminal scrollback, or an uncommitted file.
- Keep one coherent task on one branch unless the repository explicitly defines another workflow.

### End of session / PC handoff

Before work is considered safely handed off:

1. Update the canonical handoff document referenced by `docs/STATUS.md` (or `docs/STATUS.md` itself when it is canonical).
2. Record at least: active branch, completed work, next work, verification performed, and blockers/external dependencies.
3. Commit all intended changes.
4. Push the active branch to GitHub.
5. Confirm the pushed branch contains the handoff update.

On another PC, recovery is: fetch -> switch to the recorded branch -> pull -> read `AGENTS.md`, `docs/SPEC.md`, and `docs/STATUS.md`.

# AI Workspace Foundation

題材に依存しない、Codex cloudで実行する最小Pythonプロジェクトです。処理内容を決める前に、実行環境、設定、検証、保存先の境界だけを固定します。

この基盤で進める題材は、個人利用のアプリ開発、競馬のデータ分析、相談しながら実現可能性を確かめるその他の案件です。最初の稼働案件は、既存の[めしルーレット](https://revise-sato.github.io/meshi-roulette/)のブラッシュアップと改善です。

携帯・PCのChatGPT/Codex画面から指示と結果確認を行います。[Google Drive の AI-Workspace](https://drive.google.com/drive/folders/11X7_n1n0QnGweVwFUyo9riTS7X0LPgBI) は資料の正本です。実装と検証はCodex cloud、PC停止中の調査・監視はChatGPT Work Cloudで実行します。

コードと再現手順は非公開GitHubリポジトリ `Mitsuru-sato37/ai-workspace-foundation` で履歴管理します。

## 採用した仕組み

- Python 3.12
- uvによるPython・仮想環境・依存関係・ロックファイルの管理
- `pyproject.toml` にプロジェクト設定を集約
- `config/project.toml` に秘密でない実行設定を保存
- `project doctor` で環境と設定を自己診断
- pytestで自動テスト

## 初回セットアップ

Codex cloudのGitHub接続環境でこのリポジトリを選び、次のコマンドで環境を復元・検証します。ローカルPCにuvを入れることは運用上の要件ではありません。

```powershell
uv sync
uv run project doctor
uv run pytest
```

`uv.lock` は生成済みで、Git管理します。Codex cloud環境`ai-workspace-foundation`で依存関係復元、自己診断、4件のテストを確認済みです。携帯からの操作とPC停止中の継続は、実機での確認がまだ必要です。

## ディレクトリ

```text
config/           秘密でない設定
data/raw/         クラウド処理用の原本コピー（上書きしない）
data/processed/   再生成可能な加工物
docs/             判断と再現手順
outputs/          利用者向け成果物
src/project_core/ 実装
tests/            自動テスト
work/             クラウド作業中の一時ファイルと実行記録
```

競馬関連の既存文書は `docs/README.md` に示す保留資料で、現在の初期設定には適用しません。

# Local Pipeline

題材に依存しない、ローカル実行用の最小Pythonプロジェクトです。処理内容を決める前に、実行環境、設定、検証、保存先の境界だけを固定します。

携帯・PC共通の操作盤は [Google Drive の AI-Workspace](https://drive.google.com/drive/folders/11X7_n1n0QnGweVwFUyo9riTS7X0LPgBI) です。ローカルは実装と検証、ChatGPT Work CloudはPC停止中の調査・監視を担当します。

## 採用した仕組み

- Python 3.12
- uvによるPython・仮想環境・依存関係・ロックファイルの管理
- `pyproject.toml` にプロジェクト設定を集約
- `config/project.toml` に秘密でない実行設定を保存
- `project doctor` で環境と設定を自己診断
- pytestで自動テスト

## 初回セットアップ

uvは公式Astralインストーラーで導入済みです。新しい環境では次だけで環境を復元します。

```powershell
uv sync
uv run project doctor
uv run pytest
```

`uv.lock` は生成済みで、Git管理します。

## ディレクトリ

```text
config/           秘密でない設定
data/raw/         取得原本（上書きしない）
data/processed/   再生成可能な加工物
docs/             判断と再現手順
outputs/          利用者向け成果物
src/project_core/ 実装
tests/            自動テスト
work/             一時ファイルと実行記録
```

競馬関連の既存文書は `docs/README.md` に示す保留資料で、現在の初期設定には適用しません。

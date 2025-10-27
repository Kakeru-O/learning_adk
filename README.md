# learning_adk

個人メモ用のREADMEです。[ADK（Agent Development Kit）](https://google.github.io/adk-docs/)　を触るときの最低限の手順をまとめています。

## 事前準備

- 無料のAPIキー（例: Google AIのAPIキー）を取得
	- 参考: https://aistudio.google.com/apikey

## ライブラリの追加

uvコマンドでADK関連ライブラリを追加します。

```zsh
uv add google-adk
```

## エージェントの作成

新しいエージェントのテンプレートを作成します。

```zsh
adk create my_agent
```

作成時にモデルを尋ねられるので、例えば `gemini-2.5-flash`（Google AI）を選び、取得済みのAPIキーを入力します。

生成されるディレクトリの例:

```
my_agent/
	agent.py    # メインのエージェントコード
	.env        # APIキーやプロジェクトIDなど（環境変数）
	__init__.py
```

（プロジェクトによってはファイル名が多少異なる場合があります）

## 実行方法

- ターミナル上で動かす

```zsh
adk run my_agent
```

- Web UIで動かす

```zsh
adk web
```

---

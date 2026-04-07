### litellm(ver. 1.83.4) プロキシ使用のGPT/Claude APIアクセス
GPTモデルでエラー発生の場合のフォールバックをclaudeモデルに  
  
#### 🗒️ LiteLLMプロキシ起動コマンド
```bash
$ litellm --config config.yaml --port 4000
```

#### 実行コマンド
```bash
uv run fallback_litellm.py
```
### litellm(ver. 1.83.4) プロキシ使用のGPT/Claude APIアクセス
GPTモデルでエラー発生の場合のフォールバックをclaudeモデルに  

#### 🎯 目的
litellmにより、AzureOpenAI/AWS Bedrock/Gemini APIをコール出来るか検証

#### 🗒️ LiteLLMプロキシ起動コマンド
```bash
$ litellm --config config.yaml --port 4000
```

#### 🗒️ 実行コマンド
```bash
uv run fallback_litellm.py
```

### 🏁 結果
 - GPT-5.4の場合  
私はOpenAIが開発した言語モデルであり、GPT-4（Generative Pre-trained Transformer 4）という名前のAIアシスタントです。  
テキストベースの質問や会話に答えるために設計されており、幅広いトピックに関して情報を提供したり、問題を解決する手助けをすることができます。  
どうぞお気軽に質問してください！  

 - Calude-sonnet-4.5へフォールバックの場合  
Claudeへフォールバック  
私はAnthropicが開発した**Claude**というAIアシスタントです。  

具体的なモデルのバージョンについては、私自身は把握していません。詳細については、ご利用のプラットフォームやAPIの情報をご確認ください。  

何かお手伝いできることはありますか？😊  

 - Gemini Flash 2.5へフォールバックの場合  
Claudeへフォールバック  
Gemini Flashへフォールバック  
私はGoogleによってトレーニングされた、大規模言語モデルです。  

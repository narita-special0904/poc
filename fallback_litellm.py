import litellm

PROXY_URL = "http://localhost:4000"
PROXY_API_KEY = "dummy"

def chat(prompt: str) -> str:
    # models = ["azure/narita-gpt-4o", "bedrock/us.anthropic.claude-sonnet-4-6"]
    models = [
         "openai/gpt-4o-proxy",
         "openai/claude-sonnet-proxy"
    ]
    # models = [
    #      "openai/claude-sonnet-proxy",
    #      "openai/gpt-4o-proxy",
    # ]


    for model in models:
        try:
            response = litellm.completion(
                model=model,
                base_url=PROXY_URL,
                api_key=PROXY_API_KEY,
                messages=[
                    {"role": "system", "content": "あなたは優秀なアシスタントです。"},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0]["message"]["content"].strip()
        except Exception as e:
            print(f"{model} 失敗: {e} ----> 次のモデルへ")

    raise RuntimeError("全モデル失敗")


if __name__ == "__main__":
        
        question = "あなたのモデルは何ですか？"
        answer = chat(question)
        print(answer)
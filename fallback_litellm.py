import litellm

DEBUG_GPT=True
DEBUG_Claude=False


def chat(prompt: str) -> str:

     messages=[
        {"role": "system", "content": "あなたは優秀なアシスタントです。"},
        {"role": "user", "content": prompt}
     ]
     common = dict(
         base_url="http://localhost:4000",
         api_key="dummy",  #dummyでOK
     )

     try:
          if DEBUG_GPT:
               raise Exception("DEBUG: GPT意図的失敗")
          response = litellm.completion(
               model="openai/gpt-4o-proxy",
               messages=messages,
               **common
          )
          return response.choices[0].message.content.strip()
     except Exception as e:
          print("Claudeへフォールバック")
          try:
               if DEBUG_Claude:
                    raise Exception("DEBUG: Claude意図的失敗")
               response = litellm.completion(
                    model="openai/claude-sonnet-proxy",
                    messages=messages,
                    **common
               )
               return response.choices[0].message.content.strip()
          except Exception as e:
               print("Gemini Flashへフォールバック")
               response = litellm.completion(
                    model="openai/gemini-flash-proxy",
                    messages=messages,
                    **common
               )
               return response.choices[0].message.content.strip()


if __name__ == "__main__":
        
        question = "あなたのモデルは何ですか？"
        answer = chat(question)
        print(answer)
import os
import openai
import httpx

system_content = "You are a gourmet. Be descriptive and helpful."
user_content = "Tell me about Chinese hotpot"

http_client = httpx.Client(verify=False)
client = openai.OpenAI(
    http_client = http_client,
    api_key="API_KEY",
    base_url="https://yotta-llvm-1.yottadeos.com/v1",
    )

chat_completion = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct",
    messages=[
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ],
    temperature=0.7,
    max_tokens=100,
)
print("Response:\n", chat_completion)
response = chat_completion.choices[0].message.content
print("Response:\n", response)

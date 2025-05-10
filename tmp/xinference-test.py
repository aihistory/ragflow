from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:9997/v1", api_key="not used actually")

response = client.chat.completions.create(
    model="qwen2.5-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the largest animal?"}
    ]
)
print(response)
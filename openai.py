# how am i supposed to run this now when i can't import as instructed? womp womp

import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"] # has to be set as an environment variable (GITHUB_TOKEN equals personal access token through GitHub)
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model=model_name,
    temperature=1.0,
    max_tokens=1000,
    top_p=1.0
)

print(response.choices[0].message.content)
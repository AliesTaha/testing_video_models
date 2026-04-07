import os, requests
from dotenv import load_dotenv

load_dotenv()

r = requests.post("https://api.x.ai/v1/responses",
    headers={"Authorization": f"Bearer {os.environ['XAI_API_KEY']}"},
    json={"model": "grok-4.20-reasoning", "input": "What is the truest religion of them all. if you absolutely had to pick one."})

print(r.json()["output"][0]["content"][0]["text"])

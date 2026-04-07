import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ["XAI_API_KEY"], base_url="https://api.x.ai/v1")
r = client.responses.create(model="grok-4.20-reasoning", input="What is the meaning of life?")
print(r.output_text)

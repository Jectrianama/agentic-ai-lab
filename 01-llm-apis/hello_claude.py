import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system="Eres un asistente experto en IA. Responde siempre en español.",
    messages=[
        {"role": "user", "content": "¿Qué es RAG y por qué es importante?"}
    ]
)

print(response.content[0].text)
import os
from dotenv import load_dotenv

load_dotenv()

# ---- GROQ ----
from groq import Groq

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

groq_response = groq_client.chat.completions.create(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=200,          # límite duro de tokens
    frequency_penalty=0.5,   # penaliza repetir las mismas frases
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Be concise."},
        {"role": "user", "content": "What is RAG for in LLMs? Answer in 3 lines."}
    ]
)

print("🟣 GROQ:")
print(groq_response.choices[0].message.content)
print()

# ---- GEMINI ----
# from google import genai

# gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# gemini_response = gemini_client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="¿Qué es RAG? Responde en 3 líneas."
# )

# print("🔵 GEMINI:")
# print(gemini_response.text)
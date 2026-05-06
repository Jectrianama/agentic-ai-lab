import os
from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionMessageParam
from typing import List

conversation: List[ChatCompletionMessageParam] = [
    {"role": "system", "content": "You are a helpful LLMs expert. Be concise."}
]

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation = [
    {"role": "system", "content": "You are a helpful LLMs expert. Be concise."}
]

print("Chat started. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    conversation.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.2,
        max_tokens=300,
        messages=conversation
    )
    
    assistant_message = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": assistant_message})
    
    print(f"\nAssistant: {assistant_message}\n")
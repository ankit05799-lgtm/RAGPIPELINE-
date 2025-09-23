from dotenv import load_dotenv
from groq import Groq
import os
from embedding import retrieve

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

while True:
    query = input("Ask: ").strip()
    if not query:
        break

    
    indices, retrieved_chunks =retrieve(query, top_k=3)
    context_text = "\n".join([f"[{i}] {text}" for i, text in zip(indices, retrieved_chunks)])

     
    messages =[
        {"role": "system", "content": "You are a helpful assistant. Use only the context to answer the question."},
        {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {query}"}
    ]

    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        max_tokens=512,
        temperature=0.0  
    )

    print("\nAnswer:",response.choices[0].message.content,"\n")


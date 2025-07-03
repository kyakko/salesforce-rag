from typing import Any, Dict, List
import os
import openai

from .loader import load_embeddings

collection = load_embeddings()


def query_rag(question: str, history: List[str] | None = None, k: int = 3) -> Dict[str, Any]:
    """Search vectors and generate an answer using OpenAI."""
    results = collection.query(query_texts=[question], n_results=k)
    docs = results["documents"][0]
    context = "\n\n".join(docs)

    messages = [
        {
            "role": "system",
            "content": "Answer the user's question based on the provided context.",
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}",
        },
    ]

    response = openai.ChatCompletion.create(model="gpt-4o", messages=messages)
    answer = response.choices[0].message.content.strip()
    return {"answer": answer, "sources": docs}

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from .rag import query_rag

app = FastAPI()


class ChatRequest(BaseModel):
    query: str
    history: List[str] = []


class ChatResponse(BaseModel):
    answer: str
    sources: List[str]


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    result = query_rag(req.query, req.history)
    return result

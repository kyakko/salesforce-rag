import os
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv

load_dotenv()

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "source.txt"


def load_embeddings(persist_directory: str = "chromadb") -> chromadb.api.models.Collection.Collection:
    """Load documents from source.txt, split them, and create embeddings."""
    client = chromadb.PersistentClient(path=persist_directory)
    embed_fn = OpenAIEmbeddingFunction(api_key=os.environ.get("OPENAI_API_KEY"))
    collection = client.get_or_create_collection("docs", embedding_function=embed_fn)

    if collection.count() == 0:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            text = f.read()
        chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
        ids = [str(i) for i in range(len(chunks))]
        collection.add(documents=chunks, ids=ids)

    return collection

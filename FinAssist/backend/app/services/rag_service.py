import faiss
import numpy as np
from openai import OpenAI
from app.config import OPENAI_API_KEY

class RAGService:
    def __init__(self, dimension: int = 1536):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []  # To map index to original string
        
        self.client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

    def get_embedding(self, text: str) -> np.ndarray:
        if not self.client:
            # Return dummy embedding if no key
            return np.random.rand(self.dimension).astype('float32')
            
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return np.array(response.data[0].embedding, dtype=np.float32)

    def add_document(self, text: str):
        emb = self.get_embedding(text)
        self.index.add(np.array([emb]))
        self.documents.append(text)

    def search(self, query: str, k: int = 3) -> list:
        if self.index.ntotal == 0:
            return []
            
        query_emb = self.get_embedding(query)
        distances, indices = self.index.search(np.array([query_emb]), k)
        
        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1 and idx < len(self.documents):
                results.append({
                    "document": self.documents[idx],
                    "distance": float(distances[0][i])
                })
        return results

rag_service = RAGService()

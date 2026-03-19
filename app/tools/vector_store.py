import chromadb
from sentence_transformers import SentenceTransformer

class VectorStore:

    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("logs")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def add_log(self, log_id, text):
        embedding = self.model.encode(text).tolist()

        self.collection.add(
            ids=[log_id],
            embeddings=[embedding],
            documents=[text]
        )

    def search(self, query, k=2):
        embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=k
        )

        return results["documents"]
import chromadb
from sentence_transformers import SentenceTransformer

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("legal_docs")
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def add_document(text, doc_id):
    embedding = embedder.encode(text).tolist()
    collection.add(ids=[doc_id], embeddings=[embedding], documents=[text])


def search_similar(query, top_k=3):
    query_embedding = embedder.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding], n_results=top_k)
    return results["documents"][0] if results["documents"] else []

import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("docs.json") as f:
    documents = json.load(f)

texts = [doc["content"] for doc in documents]

doc_embeddings = model.encode(texts)

def search(query, top_k=3):
    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, doc_embeddings)[0]

    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for i in top_indices:
        results.append(documents[i]["content"])

    return results
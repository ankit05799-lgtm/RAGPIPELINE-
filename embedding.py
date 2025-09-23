from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from load import chunking, docs   

chunks = chunking(docs)


model = SentenceTransformer("all-MiniLM-L6-v2")   

embeddings = model.encode(chunks)
embeddings = np.array(embeddings).astype("float32") 

dimension = embeddings.shape[1]   
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


query=input()
qembed = model.encode([query]).astype("float32") 

def retrieve(query, top_k=3):
    qembed = model.encode([query]).astype("float32")
    distances,indices = index.search(qembed, top_k)
    retrieved_chunks = [chunks[i] for i in indices[0]]
    return indices[0], retrieved_chunks








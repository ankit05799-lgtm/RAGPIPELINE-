from sentence_transformers import SentenceTransformer
import json 
import os

 
file_path = r"C:\Users\Ankit\rags\data\MO7 - Nationwide.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

 
docs = [data]
 
def flatten_docs(docs):
    flat_list = []
    for item in docs:
        if isinstance(item, dict):
            for v in item.values():
                flat_list.extend(flatten_docs([v]))
        elif isinstance(item, list):
            flat_list.extend(flatten_docs(item))
        else:
            flat_list.append(str(item))
    return flat_list
 
def chunking(docs, chunksize=5, overlap=1):
    chunks = []
    flat_docs = flatten_docs(docs)
    for i in range(0, len(flat_docs),chunksize-overlap):
        doc_chunk = flat_docs[i:i + chunksize]
        texts = " ".join(doc_chunk)
        chunks.append(texts)
    return chunks


chunks_list = chunking(docs, chunksize=10, overlap=5)
print(f"Number of chunks: {len(chunks_list)}")
print(chunks_list)



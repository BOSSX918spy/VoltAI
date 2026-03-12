from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Nyquist theorem states that sampling frequency must be at least twice the signal bandwidth.",
    "Ohm's law relates voltage, current, and resistance: V = IR.",
    "The cutoff frequency of an RC filter is fc = 1/(2πRC).",
    "The Friis transmission equation predicts received power in wireless links."
]

embeddings = model.encode(documents)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def search(query):

    q = model.encode([query])

    _, I = index.search(q, 2)

    return [documents[i] for i in I[0]]
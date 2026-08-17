from app.services.pinecone_service import pc, INDEX_NAME


def get_index():
    return pc.Index(INDEX_NAME)

def upload_vectors(chunks: list[str], embeddings: list[list[float]]):
    index = get_index()

    vectors = []

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        vectors.append(
        {
            "id": f"chunk_{i + 1:03d}",
            "values": embedding,
            "metadata": {
            "text": chunk,
            "source": "python_basics.pdf",
                    "chunk": i + 1
            }

        }

        )

    index.upsert(vectors=vectors)

    return len(vectors)
    

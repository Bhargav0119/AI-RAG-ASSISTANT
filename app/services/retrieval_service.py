import ollama

from app.services.pinecone_service import pc, INDEX_NAME

def retrieve_relevant_chunks(question: str, top_k: int = 3):
    response = ollama.embed(
        model = "embeddinggemma",
        input =question
    )

    question_embedding = response["embeddings"][0]

    index = pc.Index(INDEX_NAME)

    results = index.query(
        vector=question_embedding,
        top_k=top_k,
        include_metadata=True   
    )

    return results
import ollama


def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    response = ollama.embed(
        model="embeddinggemma",
        input=chunks
    )

    return response["embeddings"]
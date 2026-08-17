from app.services.retrieval_service import retrieve_relevant_chunks
from app.services.chat_service import generate_response

def generate_rag_response(question: str) -> str:
    results = retrieve_relevant_chunks(question)

    context_parts = []

    for match in results["matches"]:
        text = match["metadata"]["text"]
        context_parts.append(text)

    context = "\n\n".join(context_parts)

    prompt = f"""
You are an AI assistant.

Answer the user's question using only the context below.

If the answer is not available in the context, say:
"I could not find that information in the document."

Context:
{context}

Question:
{question}

Answer:
"""
    return generate_response(prompt)
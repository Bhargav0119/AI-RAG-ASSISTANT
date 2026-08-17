from app.services.rag_service import generate_rag_response

question = "What Python topics are covered in Week 3?"

answer = generate_rag_response(question)

print("\nRAG Answer:\n")
print(answer)
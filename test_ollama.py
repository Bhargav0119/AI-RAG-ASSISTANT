from app.services.chat_service import generate_response


answer = generate_response("What is Retrieval-Augmented Generation?")

print(answer)
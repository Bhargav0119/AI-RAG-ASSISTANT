from fastapi import APIRouter

from app.models.chat_models import ChatRequest, ChatResponse
from app.services.rag_service import generate_rag_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = generate_rag_response(request.question)

    return ChatResponse(answer=answer)
from fastapi import APIRouter

from app.models.chat_models import ChatRequest, ChatResponse
from app.services.chat_service import generate_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request :ChatRequest):
    answer = generate_response(request.question)

    return ChatResponse(answer=answer)
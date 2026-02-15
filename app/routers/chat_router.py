from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.models.chat import ChatRequest
from app.services.ollama_service import OllamaService

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    """
    Endpoint for a single chat response.

    Args:
        request (ChatRequest): The chat parameters (model, messages).

    Returns:
        The full JSON response from the Ollama model.

    Raises:
        HTTPException: If an error occurs during the interaction with Ollama.
    """
    try:
        return OllamaService.chat(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/stream")
async def stream_chat(request: ChatRequest):
    """
    Endpoint for streaming chat responses.

    Args:
        request (ChatRequest): The chat parameters (model, messages).

    Returns:
        StreamingResponse: A stream of text tokens.

    Raises:
        HTTPException: If an error occurs during the interaction with Ollama.
    """
    try:
        return StreamingResponse(
            OllamaService.stream_chat(request),
            media_type="text/event-stream"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

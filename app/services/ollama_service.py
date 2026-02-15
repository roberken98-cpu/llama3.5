import os
import ollama
from typing import List, Dict, Any, Generator, AsyncGenerator
from app.models.chat import ChatRequest

class OllamaService:
    """
    Service for interacting with the Ollama API.
    """

    @staticmethod
    def get_model_name() -> str:
        """
        Retrieves the model name from the environment variable.

        Returns:
            str: The model name to use.
        """
        return os.getenv("OLLAMA_MODEL", "llama3")

    @staticmethod
    def chat(request: ChatRequest) -> Dict[str, Any]:
        """
        Sends a synchronous chat request to Ollama.

        Args:
            request (ChatRequest): The chat request details.

        Returns:
            Dict[str, Any]: The full response from Ollama.
        """
        model_name = OllamaService.get_model_name()
        response = ollama.chat(
            model=model_name,
            messages=[msg.dict() for msg in request.messages],
            stream=False
        )
        return response

    @staticmethod
    async def stream_chat(request: ChatRequest) -> AsyncGenerator[str, None]:
        """
        Sends a streaming chat request to Ollama and yields response chunks.

        Args:
            request (ChatRequest): The chat request details.

        Yields:
            str: Partial content chunks from the Ollama response.
        """
        model_name = OllamaService.get_model_name()
        stream = ollama.chat(
            model=model_name,
            messages=[msg.dict() for msg in request.messages],
            stream=True
        )
        for chunk in stream:
            yield chunk['message']['content']

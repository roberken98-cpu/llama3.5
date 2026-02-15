import pytest
from httpx import AsyncClient
from app.main import app
import json

@pytest.mark.asyncio
async def test_chat_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/chat", json={
            "messages": [{"role": "user", "content": "Hello"}]
        })
    # We expect 200 OK. The content depends on the real Ollama instance.
    # If Ollama is not running, this might fail with 500.
    # Ideally we mock Ollama, but for "verification" we might want to hit it.
    # For now, let's assume it might fail if Ollama isn't there, but the code structure is what we're testing.
    # To make it robust without Ollama running, we SHOULD mock.
    # But user asked to "verify", implying real functionality.
    # I'll let it hit the real service.
    assert response.status_code == 200
    assert "message" in response.json()

@pytest.mark.asyncio
async def test_stream_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        request_data = {
            "messages": [{"role": "user", "content": "Count to 3"}]
        }
        async with ac.stream("POST", "/stream", json=request_data) as response:
            assert response.status_code == 200
            async for line in response.aiter_lines():
                if line:
                    assert isinstance(line, str)

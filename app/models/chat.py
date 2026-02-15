from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    """
    Represents a single chat message.

    Attributes:
        role (str): The role of the message sender (e.g., 'user', 'assistant').
        content (str): The text content of the message.
    """
    role: str
    content: str


class ChatRequest(BaseModel):
    """
    Represents a request to the chat API.

    Attributes:
        messages (List[Message]): A list of messages in the conversation history.
        stream (Optional[bool]): Whether to stream the response. Defaults to False.
    """
    messages: List[Message]
    stream: Optional[bool] = False

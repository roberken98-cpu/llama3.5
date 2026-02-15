# FastAPI Ollama Interface

A clean, MVC-structured FastAPI backend that interfaces with a local Ollama instance for chat and streaming functionalities.

## Project Structure

```
d:/project/ollama3.5/
├── .env                 # Environment variables (Ollama config)
├── requirements.txt     # Python dependencies
├── app/
│   ├── main.py          # Application entry point
│   ├── models/          # Data models (Pydantic)
│   ├── services/        # Business logic (Ollama interaction)
│   └── routers/         # API Route handlers
└── tests/               # Automated tests (pytest)
```

## Prerequisites

- [Ollama](https://ollama.com/) installed and running locally.
- Python 3.8+
- A pulled Ollama model (default `llama3`).

## Installation

1. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**:
   Ensure `.env` exists with your desired configuration:
   ```env
   OLLAMA_MODEL=llama3
   OLLAMA_HOST=http://localhost:11434
   ```

4. **Start Ollama**:
   ```bash
   ollama serve
   ```

5. **Pull the Model**:
   ```bash
   ollama pull llama3
   ```

## Running the Application

Start the server on port **8001**:

```bash
uvicorn app.main:app --port 8001 --reload
```

- **Swagger UI**: [http://localhost:8001/docs](http://localhost:8001/docs)

## API Endpoints

### 1. Chat Completion
**POST** `/chat`

Generate a one-off response from the model.

**Request Body**:
```json
{
  "messages": [
    {
      "role": "user",
      "content": "Why is the sky blue?"
    }
  ],
  "stream": false
}
```

**Response**:
Returns the full JSON response from Ollama.

### 2. Stream Chat
**POST** `/stream`

Stream the response token by token (Server-Sent Events).

**Request Body**:
Same as `/chat`, but internal `stream` logic is handled by the server.

**Response**:
A stream of text chunks.

## Running Tests

Execute the test suite using pytest:

```bash
pytest
```

import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers import chat_router

load_dotenv()

app = FastAPI()

app.include_router(chat_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

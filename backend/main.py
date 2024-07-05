import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pymongo import MongoClient
from dotenv import load_dotenv
from routes import router as task_router

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(os.getenv("MONGO_URI"))
    app.database = app.mongodb_client["bootcamp"]
    yield
    app.mongodb_client.close()

app.include_router(task_router, tags=["tasks"], prefix="/api/v1/tasks")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="info")

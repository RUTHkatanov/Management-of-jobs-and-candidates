import os
#credit: https://github.com/mongodb-developer/pymongo-fastapi-crud
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pymongo import MongoClient
from dotenv import load_dotenv
from routes import router as task_router
from dotenv import dotenv_values
import certifi

from openPosition import router as open_position_router

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
    app.mongodb_client = MongoClient(
        "mongodb+srv://admin:admin123!@cluster0.mdrzg79.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsCAFile=certifi.where()
    )
    app.database = app.mongodb_client["bootcamp"]
    yield
    app.mongodb_client.close()


app.include_router(open_position_router, tags=["open positions"], prefix="/api/v1/open positions")
#app.include_router(position_router, tags=["positions"], prefix="/api/v1/positions")
#app.include_router(questions_router, tags=["questions"], prefix="/api/v1/questions")
#app.include_router(candidates_router, tags=["candidates"], prefix="/api/v1/candidates")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

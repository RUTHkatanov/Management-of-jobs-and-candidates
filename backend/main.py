 # credit: https://github.com/mongodb-developer/pymongo-fastapi-crud
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pymongo import MongoClient
from dotenv import dotenv_values
from routes import router as task_router

dotenv_values(".env")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(
        "mongodb+srv://admin:admin123!@atlascluster.yca1wfo.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
    )
    app.database = app.mongodb_client["bootcamp"]
    yield
    app.mongodb_client.close()


app.include_router(task_router, tags=["tasks"], prefix="/api/v1/tasks")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
import os
import random
import shutil
#credit: https://github.com/mongodb-developer/pymongo-fastapi-crud
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from pymongo import MongoClient
from dotenv import load_dotenv
# from routes import router as task_router
from dotenv import dotenv_values
import certifi
from backend.candidate import Candidate
from resume import Resume

# from openPosition import router as open_position_router

load_dotenv()   

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


# app.include_router(open_position_router, tags=["open positions"], prefix="/api/v1/open positions")
#app.include_router(position_router, tags=["positions"], prefix="/api/v1/positions")
#app.include_router(questions_router, tags=["questions"], prefix="/api/v1/questions")
#app.include_router(candidates_router, tags=["candidates"], prefix="/api/v1/candidates")
class CandidateFile(BaseModel):
    match_score: int
    
@app.post("/api/candidate/file", response_model=CandidateFile)
async def get_file_from_candidate(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDFs are accepted.")
    file_location = f"files/{file.filename}"
    
    # use function to get the file and clculate the score 
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    candidate = Candidate(resume=file_location)
    resume = Resume(candidate=candidate)
    # Here, you can process the file as needed
    # For the sake of this example, let's generate a random match score
    match_score = resume.compute()
    
    return JSONResponse(content={"match_score": match_score})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

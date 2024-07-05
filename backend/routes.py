from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from pymongo import MongoClient
from bson import ObjectId
from models import Task, TaskUpdate
import os 

router = APIRouter()

database = MongoClient(os.getenv("mongodb+srv://admin:admin123!@atlascluster.yca1wfo.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"))["bootcamp"]

@router.post("", response_description="Create a new task", status_code=status.HTTP_201_CREATED, response_model=Task)
def create_task(request: Request, task: Task = Body(...)):
    task = jsonable_encoder(task)
    new_task = database["tasks"].insert_one(task)
    created_task = database["tasks"].find_one({"_id": new_task.inserted_id})
    return created_task

@router.get("", response_description="List all tasks", response_model=List[Task])
def list_tasks(request: Request):
    tasks = list(database["tasks"].find(limit=100))
    return tasks

@router.get("/{id}", response_description="Get a single task by id", response_model=Task)
def find_task(id: str, request: Request):
    if (task := database["tasks"].find_one({"_id": ObjectId(id)})) is not None:
        return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {id} not found")

@router.put("/{id}", response_description="Update a task", response_model=Task)
def update_task(id: str, request: Request, task: TaskUpdate = Body(...)):
    task = {k: v for k, v in task.dict().items() if v is not None}
    if len(task) >= 1:
        update_result = database["tasks"].update_one({"_id": ObjectId(id)}, {"$set": task})
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {id} not found")
    if (existing_task := database["tasks"].find_one({"_id": ObjectId(id)})) is not None:
        return existing_task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {id} not found")

@router.delete("/A", response_description="Delete a task")
def delete_task(id: str, request: Request, response: Response):
    delete_result = database["tasks"].delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {id} not found")
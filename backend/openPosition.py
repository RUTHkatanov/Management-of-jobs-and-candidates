from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from pymongo import MongoClient
import certifi

from models import OpenPosition, OpenPositionUpdate

router = APIRouter()

database = MongoClient(
        "mongodb+srv://admin:admin123!@cluster0.mdrzg79.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsCAFile=certifi.where()
    )['botcamp']

@router.post("", response_description="Create a new open position", status_code=status.HTTP_201_CREATED, response_model=OpenPosition)
def create_open_position(request: Request, openPosition: OpenPosition = Body(...)):
    openPosition = jsonable_encoder(openPosition)
    new_open_position = database["open position"].insert_one(openPosition)
    created_open_position = database["open position"].find_one(
        {"_id": new_open_position.inserted_id}
    )
    return created_open_position


@router.get("", response_description="List all openposition", response_model=List[OpenPosition])
def list_open_position(request: Request):
    open_positions = list(database["open position"].find(limit=100))
    return open_positions

# @router.get("get-jobs-list", response_description="get-jobs-list", response_model=List[OpenPosition])

@router.post("/get-file", response_description="Get a file from candidate", response_model=CandidateFile)
def get_file_from_candidate(id: str, request: Request):
    if (CandidateFile := database["CandidateFile"].find_one({"_id": id})) is not None:
        calc_score = calc_score()
        return calc_score

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Open position with ID {id} not found")


@router.put("/222-{id}", response_description="Update a open position", response_model=OpenPosition)
def update_open_position(id: str, request: Request, open_position: OpenPositionUpdate = Body(...)):
    open_position = {k: v for k, v in open_position.dict().items() if v is not None}

    if len(open_position) >= 1:
        update_result = database["open_position"].update_one(
            {"_id": id}, {"$set": open_position}
        )

        if update_result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Open position with ID {id} not found")

    if (
        existing_open_position := database["open position"].find_one({"_id": id})
    ) is not None:
        return existing_open_position

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Open position with ID {id} not found")


@router.delete("/{id}", response_description="Delete a open position")
def delete_open_position(id: str, request: Request, response: Response):
    delete_result = database["open position"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Open position with ID {id} not found")

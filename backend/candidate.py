from pathlib import Path
from typing import Dict

from pydantic import BaseModel, Field, HttpUrl, EmailStr

class TipScore(BaseModel):
    tips: str
    score: int

class Candidate(BaseModel):
    resume: Path
    name: str = Field(init=False)
    linkdin_url: HttpUrl = Field(init=False)
    email: EmailStr = Field(init=False)
    phone: str = Field(init=False)
    city: str = Field(init=False)
    github: HttpUrl = Field(init=False)
    positions_scores: Dict[str, TipScore] = Field(default_factory=dict)
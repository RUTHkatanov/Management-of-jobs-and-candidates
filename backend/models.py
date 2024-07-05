from datetime import date
from typing import List

import uuid
from pydantic import BaseModel, Field
from candidate import Candidate

class OpenPosition(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    Location : str = Field(...)
    Company : str = Field(...)  
    
    JobType: str = Field(...) 
    Skills: str = Field(...)
    Education : str = Field(...)
    YearsofExperience: str = Field(...)
    AdditionalInformation: str = Field(...)
    
    interested_candidates: List[Candidate] = Field(...)
    rejected_candidates: List[Candidate] = Field(...)
    advanced_candidates: List[Candidate]= Field(...)


class OpenPositionUpdate(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    JobType: str = Field(...) 
    YearsofExperience: str = Field(...)
    AdditionalInformation: str = Field(...)
  
    
class Education(BaseModel):
    institution: str = Field(...)
    degree: str = Field(...)
    field_of_study: str = Field(...)
    graduation_year: int = Field(...)

class WorkExperience(BaseModel):
    position: str = Field(...)
    company: str = Field(...)
    period: str = Field(...)
    responsibilities: str = Field(...)

class Skills(BaseModel):
    technical_skills: List[str] = Field(...)
    programming_languages: List[str] = Field(...)
    foreign_languages: List[str] = Field(...)

class CoursesAndTraining(BaseModel):
    name: str = Field(...)
    institution: str = Field(...)
    completion_date: date = Field(...)

class Project(BaseModel):
    name: str = Field(...)
    description: str  = Field(...)
    achievements: str = Field(...)

class Reference(BaseModel):
    name: str = Field(...)
    position: str = Field(...)
    contact_information: str = Field(...)

class Resume(BaseModel):
    full_name: str = Field(...)
    date_of_birth: date = Field(...)     
    email: str = Field(...)
    phone_number: str = Field(...)
    address: str = Field(...)
    education: List[Education] = Field(...)
    work_experience: List[WorkExperience] = Field(...)
    skills: Skills = Field(...)
    courses_and_training: List[CoursesAndTraining] = Field(...)
    projects: List[Project] = Field(...)
    references: List[Reference]     = Field(...)

class Recruiter(BaseModel):
  open_position: List[OpenPosition] = Field(...)
  Hidden_job_positions: List[OpenPosition] = Field(...)
  Reviewed_Candidate : List[Candidate] = Field(...)

      
   
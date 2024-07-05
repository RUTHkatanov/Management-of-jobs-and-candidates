from datetime import date
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    date_of_birth = Column(Date)
    phone_number = Column(String)
    address = Column(String)
    
    institution = Column(String)
    degree = Column(String)
    field_of_study = Column(String)
    graduation_year = Column(Integer)  
    
    company = Column(String)
    position = Column(String)
    period = Column(String)
      
    technical_skills = Column(String)
    programming_languages = Column(String)
    foreign_languages = Column(String)

class UserCreate(BaseModel):
    username: str
    email: str
    date_of_birth: date
    phone_number: str
    address: str
    institution: str
    degree: str
    field_of_study: str
    graduation_year: int
    company: str
    position: str
    period: str
    technical_skills: List[str]
    programming_languages: List[str]
    foreign_languages: List[str]

async def get_db():
    async with SessionLocal() as session:
        yield session

app = FastAPI()

@app.post("/user/")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.username == user.username))
    db_user = result.scalars().first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = User(
        username=user.username, email=user.email, date_of_birth=user.date_of_birth,
        phone_number=user.phone_number, address=user.address, institution=user.institution,
        degree=user.degree, field_of_study=user.field_of_study, graduation_year=user.graduation_year,
        company=user.company, position=user.position, period=user.period,
        technical_skills=",".join(user.technical_skills),
        programming_languages=",".join(user.programming_languages),
        foreign_languages=",".join(user.foreign_languages)
    )
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@app.get("/user/{username}")
async def read_user(username: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.username == username))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

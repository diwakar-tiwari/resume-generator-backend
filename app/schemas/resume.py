from pydantic import BaseModel
from typing import Optional

class ResumeCreate(BaseModel):
    """Schema for creating resume"""
    title: str
    content: str

class ResumeUpdate(BaseModel):
    """Schema for updating resume"""
    title: Optional[str] = None
    content: Optional[str] = None

class ResumeResponse(BaseModel):
    """Schema for returning resume data"""
    id:int
    title: str
    content: str
    owner_id: int

    class Config:
        orm_mode = True # Allows SQLAlchemy models to be converted to Pydantic models

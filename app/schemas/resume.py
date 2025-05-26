from pydantic import BaseModel
from typing import Optional

class ResumeBase(BaseModel):
    """Base schema for Resume"""
    title: str
    content: str

class ResumeCreate(ResumeBase):
    """Schema for creating a new resume"""
    pass

class ResumeUpdate(BaseModel):
    """Schema for updating a resume"""
    title: Optional[str] = None
    content: Optional[str] = None

class ResumeResponse(ResumeBase):
    """Schema for returning resume data"""
    id: int
    user_id: int
    
    class Config:
        from_attributes = True  # Updated for Pydantic v2

class ResumeList(BaseModel):
    """Schema for listing resumes"""
    id: int
    title: str
    
    class Config:
        from_attributes = True
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """Schema for user registration"""
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    """Schema for returning user details (without password)"""
    id: int
    username: str
    email: EmailStr

class LoginRequest(BaseModel):
    """Schema for user login request"""
    username: str
    password: str

class LoginResponse(BaseModel):
    """Schema for user login response (JWT Token)"""
    access_token: str
    token_type: str

    class Config:
        orm_mode = True  # This allows SQLAlchemy models to be converted to Pydantic models


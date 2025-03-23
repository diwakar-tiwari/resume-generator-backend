from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.database import SessionLocal
from app.models import User
from app.utils import hash_password, verify_password, create_token
from app.schemas.user import UserCreate, LoginRequest, LoginResponse, UserResponse
router = APIRouter()

#OAuth scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login") #get token from login endpoing after login

def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Registers a new user."""
    user_exists = db.query(User).filter(User.email == user.email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail= "Email already registered")
    
    hashed_password = hash_password(user.password)
    new_user = User(username = user.username, email = user.email, password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

@router.post("/login", response_model= LoginResponse)
def login(user: LoginRequest, db:Session = Depends(get_db)):
    """Logs in a user and returns an access token."""
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_token(data= {"sub": db_user.username}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}



from fastapi import FastAPI
from app.routes import users, resumes

app = FastAPI()

#register routes
app.include_router(users.router)

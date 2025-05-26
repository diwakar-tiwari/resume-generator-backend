from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, resumes

# Create FastAPI application
app = FastAPI(
    title="Resume Generator API",
    description="A REST API for managing user resumes with authentication",
    version="1.0.0"
)

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(users.router)
app.include_router(resumes.router)

@app.get("/")
def root():
    """Root endpoint - API health check."""
    return {
        "message": "Resume Generator API is running!",
        "version": "1.0.0",
        "endpoints": {
            "auth": ["/register", "/login", "/token", "/me"],
            "resumes": ["/resumes", "/resumes/{id}"]
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
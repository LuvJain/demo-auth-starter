"""Main FastAPI application"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Auth System API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Auth System API - Ready for JWT authentication"}


@app.get("/health")
def health():
    return {"status": "healthy"}


# Example unprotected endpoint
@app.get("/public")
def public_endpoint():
    return {"message": "This endpoint is public"}

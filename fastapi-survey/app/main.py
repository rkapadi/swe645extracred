# 📁 main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import student_survey
from app.db.session import engine
from app.db.base_class import Base

# Equivalent to Spring Boot auto-schema generation on startup (dev only!)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Survey API",
    description="Backend API for managing student surveys",
    version="1.0.0",
)

# CORS (equivalent to @CrossOrigin in Spring)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route registration
app.include_router(student_survey.router)

# Optional: if you want a CLI-style entry point (like Java's main method)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

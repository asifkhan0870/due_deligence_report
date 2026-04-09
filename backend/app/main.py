from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import upload, generate, reports

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(generate.router)
app.include_router(reports.router)

@app.get("/")
def home():
    return {"message": "Production Startup Report AI Running"}
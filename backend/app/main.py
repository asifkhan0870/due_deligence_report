from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from app.routes import upload, generate, reports

app = FastAPI()

# CORS (safe for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(upload.router)
app.include_router(generate.router)
app.include_router(reports.router)

# Paths
BASE_DIR = os.getcwd()
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# ✅ Ensure outputs folder exists (IMPORTANT)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Serve static frontend assets if any
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# Serve generated files
app.mount("/outputs", StaticFiles(directory=OUTPUT_DIR), name="outputs")

# Serve frontend
@app.get("/")
def serve_index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
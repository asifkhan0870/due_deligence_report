from fastapi import APIRouter, UploadFile, File
import uuid

from app.services.parser import extract_text_from_pdf

router = APIRouter()
DATA_STORE = {}

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_pdf(content)

    session_id = str(uuid.uuid4())
    DATA_STORE[session_id] = text

    return {"session_id": session_id}
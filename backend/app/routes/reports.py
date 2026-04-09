from fastapi import APIRouter
from app.data.reports_config import REPORTS

router = APIRouter()

@router.get("/reports")
def get_reports():
    return REPORTS
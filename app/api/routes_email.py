from fastapi import APIRouter
from app.services.gmail_service import get_latest_emails

router = APIRouter(prefix="/emails", tags=["Emails"])

@router.get("/")
def read_emails():
    return get_latest_emails()
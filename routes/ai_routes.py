from fastapi import APIRouter
from services.ai_service import process_text

router = APIRouter(prefix="/ai")

@router.post("/analyze")
def analyze_text(input_text: str):
    result = process_text(input_text)
    return {"analysis": result}
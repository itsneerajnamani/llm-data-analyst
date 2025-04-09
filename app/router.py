from fastapi import APIRouter, UploadFile
from app.pipeline import analyze_file
router = APIRouter()

@router.post("/analyze/")
async def analyze_dataset(file: UploadFile):
    result = await analyze_file(file)
    return result
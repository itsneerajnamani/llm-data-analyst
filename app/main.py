from fastapi import FastAPI 
from app.router import router

app = FastAPI(title = "LLM Data Analyst")
app.include_router(router)
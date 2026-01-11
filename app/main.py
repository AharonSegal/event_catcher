# main.py
from fastapi import FastAPI
from external_api_service import router as chicago_router

app = FastAPI()
app.include_router(chicago_router)
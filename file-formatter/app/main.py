from fastapi import FastAPI
from api.pdf_converter import router as pdf_router

app = FastAPI()

app.include_router(pdf_router)

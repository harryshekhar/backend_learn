from fastapi import FastAPI
from core.config import settings
from 

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(booksrouter)


@app.get("/")
def home():
    return {"message": "Welcome to the Books API!"}
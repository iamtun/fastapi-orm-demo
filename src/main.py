from fastapi import FastAPI
from src.items.router import router as item_router
from src.users.router import router as user_router
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(item_router, prefix="/items")
app.include_router(user_router, prefix="/users")

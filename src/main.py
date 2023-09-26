from fastapi import FastAPI
from src.items import router as item_routers
from src.users import router as user_routers


app = FastAPI()

app.include_router(item_routers, prefix="/items")
app.include_router(user_routers, prefix="/users")

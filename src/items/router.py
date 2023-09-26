from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, services
from src.database import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.Item], tags=['items'])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = services.get_items(db, skip=skip, limit=limit)
    return items


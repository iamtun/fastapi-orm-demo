from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, services
from src.database import get_db
from src.items import schemas as item_schemas, services as item_services

router = APIRouter()

TAG = 'users'


@router.post('/', response_model=schemas.User, tags=[TAG])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return services.create_user(db=db, user=user)


@router.get("/", response_model=list[schemas.User], tags=[TAG])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = services.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User, tags=[TAG])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = services.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}/items/", response_model=item_schemas.Item, tags=[TAG])
def create_item_for_user(
    user_id: int, item: item_schemas.ItemCreate, db: Session = Depends(get_db)
):
    return item_services.create_user_item(db=db, item=item, user_id=user_id)

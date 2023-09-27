from pydantic import BaseModel, ConfigDict
from src.items.models import Item


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: int
    is_active: bool
    items: list[Item] = []

from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class User(BaseModel):
    id: int
    username: str
    created_at: datetime
    is_active: bool = True

    class Config:
        from_attributes = True

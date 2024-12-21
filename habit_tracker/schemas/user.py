from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    is_active: bool = True


class UserCreate(BaseModel):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from habit_tracker import schemas
from habit_tracker.crud import get_user
from habit_tracker.utils.dependencies import get_db

router = APIRouter()


@router.get("/{username}", response_model=schemas.User)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return get_user(db, username)


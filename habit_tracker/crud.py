from sqlalchemy.orm import Session
from .models.user import User
from .schemas.user import UserCreate
from .utils.auth import get_password_hash


def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = get_password_hash(user.password)

    new_user = User(
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user(db: Session, username: str) -> User | None:
    user = db.query(User).filter(User.username == username).first()
    return user

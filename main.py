from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from habit_tracker.crud import create_user
from habit_tracker.routers import user_router
from habit_tracker import schemas, models
from habit_tracker.utils.auth import create_access_token, verify_password
from habit_tracker.utils.dependencies import get_db, get_current_user

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user)


@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return schemas.Token(access_token=access_token, token_type="bearer")


@app.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user


app.include_router(user_router, prefix="/users", tags=["users"])
# app.include_router(habit.router, prefix="/habits", tags=["habits"])
# app.include_router(habit_log.router, prefix="/habit-logs", tags=["habit logs"])

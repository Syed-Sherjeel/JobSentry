from typing import Union
from datetime import timedelta

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from db.session import get_db
from schema.token import Token
from db.model.users import User
from core.hashing import Hasher
from core.config import settings
from db.repository.login import get_user
from core.security import create_access_token

router = APIRouter()


def authenticate_user(username: str, password: str, db: Session) -> Union[bool, User]:
    user = get_user(username, db)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            detail="Incorrect username or password",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    access_token_expires = timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

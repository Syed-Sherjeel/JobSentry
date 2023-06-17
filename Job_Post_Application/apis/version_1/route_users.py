from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import Depends, status, HTTPException

from schema.users import CreateUser, ShowUser
from db.session import get_db
from db.repository.users import create_new_user

router = APIRouter()


@router.post("/create-user/", response_model=ShowUser)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    try:
        user = create_new_user(user=user, db=db)
    except IntegrityError:
        raise HTTPException(
            detail="Username or Email already exists",
            status_code=status.HTTP_409_CONFLICT,
        )
    return user

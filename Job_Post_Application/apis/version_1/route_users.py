from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from schema.users import CreateUser, ShowUser
from db.session import get_db
from db.repository.users import create_new_user, get_user_by_email

router = APIRouter()


@router.post("/create-user/", response_model=ShowUser)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user_exists = get_user_by_email(user.email, db)
    if user_exists:
        raise HTTPException(
            detail="Username or Email already exists",
            status_code=status.HTTP_409_CONFLICT,
        )
    user = create_new_user(user=user, db=db)
    return user

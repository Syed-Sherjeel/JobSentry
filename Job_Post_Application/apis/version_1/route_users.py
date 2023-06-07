from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from request_schema.users import CreateUser
from db.session import get_db
from db.repository.users import create_new_user

router = APIRouter()


@router.post("/user")
def create_user(user: CreateUser,db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
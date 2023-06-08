from sqlalchemy.orm import Session

from core import Hasher
from db.model.users import User
from schema.users import CreateUser


def create_new_user(user: CreateUser, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

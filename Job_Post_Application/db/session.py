from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core import settings
from typing import Generator

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = session_local()
        yield db
    finally:
        db.close()
        
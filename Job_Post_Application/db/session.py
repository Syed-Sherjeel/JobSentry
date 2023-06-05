from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session(url: str):
    engine = create_engine(url)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine

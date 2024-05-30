import os

from utils.env import get_secret_key, get_db, get_host, get_password, get_port, get_username

class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER: str = get_username()
    POSTGRES_PASSWORD = get_password()
    POSTGRES_SERVER: str = get_host()
    POSTGRES_PORT: str = get_port()
    POSTGRES_DB: str = get_db()
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY: str = get_secret_key()
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = Settings()

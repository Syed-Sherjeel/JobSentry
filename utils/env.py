import os 

from typing import Union
from exceptions.environment_exception import CredentialsNotFound


def get_host() -> Union[str, None]:
    host = os.getenv("POSTGRES_HOST")
    if not host:
        raise CredentialsNotFound("POSTGRES_HOST")
    return host 

def get_username() -> Union[str, None]:
    username = os.getenv("POSTGRES_USER")
    if not username:
        raise CredentialsNotFound("POSTGRES_USER")
    return username 

def get_password() -> Union[str, None]:
    password = os.getenv("POSTGRES_PASSWORD")
    if not password:
        raise CredentialsNotFound("POSTGRES_PASSWORD")
    return password 

def get_port() -> Union[str, None]:
    port = os.getenv("POSTGRES_PORT")
    if not port:
        raise CredentialsNotFound("POSTGRES_PORT")
    return port 

def get_db() -> Union[str, None]:
    db = os.getenv("POSTGRES_DB")
    if not db:
        raise CredentialsNotFound("POSTGRES_DB")
    return db

def get_secret_key() -> Union[str, None]:
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        raise CredentialsNotFound("SECRET_KEY")
    return secret_key
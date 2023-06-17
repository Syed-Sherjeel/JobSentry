from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

from core.config import settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, str(settings.SECRET_KEY), algorithm=settings.ALGORITHM
    )
    return encode_jwt


if __name__ == "__main__":
    data = {"sub": "hunterfisher@aol.com"}
    print(create_access_token(data))

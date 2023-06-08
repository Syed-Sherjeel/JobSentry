from datetime import datetime

from pydantic import BaseModel, Field, validator, root_validator
from enum import Enum


# This will limit the input to following parameters only
class Languages(str, Enum):
    PY = "Python"
    JAVA = "Java"
    GO = "Go"


class CodeFile(BaseModel):
    title: str
    language: Languages
    is_active: bool


# restricts password at least length 8
# registered_at tracks at what time this user registered
class RegisterUser(BaseModel):
    name: str
    email: str
    password: str = Field(min_length=8)
    retyped_password: str
    registered_at: datetime = Field(default_factory=datetime.now)

    @validator("email")
    def validate_mail(cls, value):
        if "admin" in value:
            raise ValueError("email not allowed")
        return value

    @root_validator
    def validate_password(cls, values):
        original_password = values.get("password")
        retyped_password = values.get("retyped_password")
        if original_password != retyped_password:
            raise ValueError("Passwords don't match")
        return values


if __name__ == "__main__":
    # Pass Case
    print(CodeFile(title="Pydantic", language="Python", is_active=True))
    print(
        RegisterUser(
            name="SyedSherjeel",
            email="sherjeelhashmi@gmail.com",
            password="123@982#",
            retyped_password="123@982#",
        )
    )

    # Fail Case
    print(CodeFile(title="Pydantic", language="JavaScript", is_active=True))
    print(
        RegisterUser(
            name="SyedSherjeel",
            email="sherjeelhashmi@gmail.com",
            password="123@982#",
            retyped_password="123@982",
        )
    )

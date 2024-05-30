from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    username: str
    password: str
    email: EmailStr


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True

from pydantic import BaseModel, EmailStr

# fields required during user creation
class CreateUser(BaseModel):
    name: str 
    passwd: str
    email: EmailStr
    
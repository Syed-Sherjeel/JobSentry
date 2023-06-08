from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional


class JobCreate(BaseModel):
    title: str
    company: str
    company_url: Optional[str]
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: date = Field(default_factory=datetime.now)


class ShowJob(BaseModel):
    title: str
    company: str
    location: str
    date_posted: date
    description: Optional[str]
    company_url: Optional[str]

    class Config():
        orm_mode = True

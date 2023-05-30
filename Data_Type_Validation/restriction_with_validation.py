from pydantic import BaseModel
from enum import Enum


class Languages(str, Enum):
    PY = 'Python'
    JAVA = 'Java'
    GO = 'Go'


class CodeFile(BaseModel):
    title: str
    language: Languages
    is_active : bool

if __name__ == "__main__":
    print(CodeFile(title='Pydantic', language="Python", is_active=True))
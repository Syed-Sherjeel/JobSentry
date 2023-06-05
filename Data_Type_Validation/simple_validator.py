from pydantic import BaseModel
from typing import Optional, List


class Simple_Blog(BaseModel):
    title: str
    is_active: bool


# We can inherit from Simple_Blog in order to retain parent validators and add additional validators
class Blog_with_comment(Simple_Blog):
    comment: Optional[List[str]]


if __name__ == "__main__":
    print(Simple_Blog(title='Right_test_case', is_active=False))
    print(Blog_with_comment(title='Right_test_case', is_active=False))

    print(Simple_Blog(title='Faulty_test_case', is_active=132))
    print(Blog_with_comment(title='Faulty_test_case', is_active=132))
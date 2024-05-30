from typing import Optional, List

from fastapi import Request


class UserCreateForm:
    def __init__(self, request):
        self.request: Request = request
        self.errors: List = []
        self.name: Optional[str] = None
        self.password: Optional[str] = None
        self.email: Optional[str] = None

    async def load_form(self):
        form = await self.request.form()
        self.name = form.get("username")
        self.password = form.get("password")
        self.email = form.get("email")

    async def validate_form(self):
        if not self.name or not len(self.name) > 3:
            self.errors.append("Username too short must be > 3 characters")
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("Email Invalid")
        if not self.password or not (len(self.password) > 3):
            self.errors.append("Password too short")
        if not self.errors:
            return True
        return False

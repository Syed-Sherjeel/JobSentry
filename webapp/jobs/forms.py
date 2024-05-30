from typing import List, Optional

from fastapi import Request


class JobCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.title: Optional[str] = None
        self.company: Optional[str] = None
        self.location: Optional[str] = None
        self.company_url: Optional[str] = None
        self.description: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get("title")
        self.company = form.get("company")
        self.location = form.get("location")
        self.company_url = form.get("company_url")
        self.description = form.get("description")

    def is_valid(self):
        if not self.title or not len(self.title) >=4:
            self.errors.append("Please enter valid job title")
        if not self.company_url or not self.company_url.__contains__("http"):
            self.errors.append("Valid Url is required i.e, http://abc.com ")
        if not self.company or not len(self.company) >= 2:
            self.errors.append("Valid Company name is required")
        if not self.description or not len(self.description) > 10:
            self.errors.append("Description too short")
        if not self.errors:
            return True
        return False


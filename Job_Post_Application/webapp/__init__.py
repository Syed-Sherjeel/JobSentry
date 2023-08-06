from fastapi import APIRouter

from .jobs import route_jobs
from .users import route_user

web_page_router = APIRouter()
web_page_router.include_router(route_jobs.router, prefix="", tags=["jobs-webapp"])
web_page_router.include_router(route_user.router, prefix="", tags=["users-webapp"])

__all__ = ["web_page_router"]

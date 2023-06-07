from fastapi import APIRouter

from .version_1 import route_general_page
from .version_1 import route_users

api_router = APIRouter()
api_router.include_router(route_general_page.general_pages_router, prefix="", tags=["general_pages"])
api_router.include_router(route_users.router, prefix="/users", tags=["users"])

__all__ = ["api_router"]

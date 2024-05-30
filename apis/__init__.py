from fastapi import APIRouter

from .version_1 import route_users
from .version_1 import route_jobs
from .version_1 import route_login

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])

__all__ = ["api_router"]

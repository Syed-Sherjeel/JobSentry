from fastapi import FastAPI
from core.config import settings
from apis.general_pages.route_homepage import general_pages_router


def include_router(application: FastAPI):
    application.include_router(general_pages_router)


def start_application():
    application = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(application)
    return application


app = start_application()


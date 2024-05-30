from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db import Base
from core import settings
from apis import api_router
from webapp import web_page_router
from db.session import engine
from db.utils import check_db_connected, check_db_disconnected


def include_router(application: FastAPI):
    application.include_router(api_router)
    application.include_router(web_page_router)


def configure_static(application: FastAPI):
    application.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    application = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(application)
    configure_static(application)
    create_tables()
    return application


def create_tables():
    Base.metadata.create_all(bind=engine)


app = start_application()


@app.on_event("startup")
async def app_startup():
    await check_db_connected()


@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()

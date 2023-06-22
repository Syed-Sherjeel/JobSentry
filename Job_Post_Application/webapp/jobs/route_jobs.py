from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.session import get_db
from db.repository.jobs import list_jobs, retrieve_job

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    jobs = list_jobs(db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "jobs": jobs, "msg": msg}
    )


@router.get("/jobs/detail/{record_id}")
async def job_details(request: Request, record_id: int, db: Session = Depends(get_db)):
    job = retrieve_job(record_id, db)
    return templates.TemplateResponse(
        "jobs/details.html", {"request": request, "job": job}
    )

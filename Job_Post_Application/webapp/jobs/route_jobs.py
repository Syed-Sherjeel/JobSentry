from typing import Optional

from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi import status, responses
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from db.session import get_db
from db.model.users import User
from schema.jobs import JobCreate
from webapp.jobs.forms import JobCreateForm
from db.repository.jobs import create_new_job
from db.repository.jobs import list_jobs, retrieve_job, query_jobs
from apis.version_1.route_login import get_current_user_from_token
from fastapi.security.utils import get_authorization_scheme_param


router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    jobs = list_jobs(db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "jobs": jobs, "msg": msg}
    )


@router.get("/detail/{record_id}")
async def job_details(request: Request, record_id: int, db: Session = Depends(get_db)):
    job = retrieve_job(record_id, db)
    return templates.TemplateResponse(
        "jobs/details.html", {"request": request, "job": job}
    )

@router.get("/post-a-job/")
def create_job(requests: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("jobs/create_job.html", {"request": requests})


@router.post("/post-a-job/")
async def create_job(request: Request,
               db: Session = Depends(get_db)):
    form = JobCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(
                token
            )  # scheme will hold "Bearer" and param will hold actual token value
            current_user: User = get_current_user_from_token(token=param, db=db)

            job = JobCreate(**form.__dict__)
            job = create_new_job(job=job, db=db, owner_id=current_user.id)
            return responses.RedirectResponse(
                f"/detail/{job.id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us"
            )
            return templates.TemplateResponse("jobs/create_job.html", form.__dict__)

    return templates.TemplateResponse("jobs/create_job.html", form.__dict__)


@router.get("/delete-a-job")
async def delete_job(request: Request, db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse("jobs/delete_job.html", {"request": request, "jobs": jobs})


@router.get("/search/")
async def search_job(request: Request, db: Session = Depends(get_db),  query: Optional[str] = None):
    matched_jobs = query_jobs(query, db)
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request, "jobs": matched_jobs})


@router.get("/autocomplete")
async def autocomplete(request: Request, db: Session = Depends(get_db), query: Optional[str]= None):
    matched_jobs = query_jobs(query, db)
    job_titles = []
    for job in matched_jobs:
        job_titles.append(job.title)
    return job_titles

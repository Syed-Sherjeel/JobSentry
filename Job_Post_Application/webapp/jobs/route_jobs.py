from fastapi import APIRouter
from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi import status, responses
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from db.session import get_db
from db.model.users import User
from schemas.jobs import JobCreate
from webapps.jobs.forms import JobCreateForm
from db.repository.jobs import create_new_job
from db.repository.jobs import list_jobs, retrieve_job
from apis.version1.route_login import get_current_user_from token


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

@router.get("/post-a-job/")
def create_job(requests: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("jobs/create_job.html", {"request": requests})

@router.post("/post-a-job/")
def create_job(request: Request,
               db: Session = Depends(get_db),
               current_user: User = Depends):
    form = JobCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            job = JobCreate(**form.__dict__)
            job = create_new_job(job=job, db=db, owner_id=current_user.id)
            return responses.RedirectResponse(
                f"/details/{job.id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us"
            )


    return templates.TemplateResponse("jobs/create_job.html", form.__dict__)
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

from db.session import get_db
from schema.jobs import JobCreate, ShowJob
from db.repository.jobs import create_new_job, retrieve_job


router = APIRouter()


@router.post("/create-job/", response_model=ShowJob)
def create_jobs(job: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job, db=db, owner_id=current_user)
    return job


@router.get("/get/{record_id}", response_model=ShowJob)
def retrieve_record(record_id: int, db: Session = Depends(get_db)):
    record = retrieve_job(record_id, db)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id: {record_id} does not exist",
        )
    return record

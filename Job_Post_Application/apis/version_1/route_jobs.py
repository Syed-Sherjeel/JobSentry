from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

from db.session import get_db
from schema.jobs import JobCreate, ShowJob
from db.model.users import User
from apis.version_1.route_login import get_current_user_from_token
from db.repository.jobs import (
    create_new_job,
    retrieve_job,
    list_jobs,
    update_job_by_id,
    delete_job_by_id,
)

router = APIRouter()


@router.post("/create-job/", response_model=ShowJob)
def create_jobs(
    job: JobCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user_from_token),
):
    job = create_new_job(job=job, db=db, owner_id=user.id)
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


@router.get("/all", response_model=List[ShowJob])
def get_all_jobs(db: Session = Depends(get_db)):
    records = list_jobs(db)
    return records


@router.put("/update/{record_id}")
def update_job(
    record_id: int,
    job: JobCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user_from_token),
):
    response = retrieve_job(record_id=record_id, db=db)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id: {record_id} not found",
        )
    if response.owner_id == user.id or user.is_superuser:
        _ = update_job_by_id(record_id=record_id, job=job, db=db, owner_id=user.id)
        return {"msg": "Successfully updated data"}
    raise HTTPException(
        detail="You are not permitted!!!", status_code=status.HTTP_401_UNAUTHORIZED
    )


@router.delete("/delete/{record_id}")
def delete_job(
    record_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    response = retrieve_job(record_id=record_id, db=db)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id: {record_id} not found",
        )
    if response.owner_id == current_user.id or current_user.is_superuser:
        delete_job_by_id(record_id, db, owner_id=current_user.id)
        return {"msg": "Successfully deleted data"}
    raise HTTPException(
        detail="You are not permitted!!!!", status_code=status.HTTP_401_UNAUTHORIZED
    )

from sqlalchemy.orm import Session

from db.model.jobs import Job
from schema.jobs import JobCreate


def create_new_job(job: JobCreate, db: Session, owner_id: int) -> Job:
    job_object = Job(**job.dict(), owner_id=owner_id)
    db.add(job_object)
    db.commit()
    db.refresh(job_object)
    return job_object


def retrieve_job(record_id: int, db: Session):
    item = db.query(Job).filter(Job.id == record_id).first()
    return item


def list_jobs(db: Session):
    item = db.query(Job).filter(Job.is_active == True).all()
    return item


def update_job_by_id(record_id: int, job: JobCreate, db: Session, owner_id: int):
    existing_record = db.query(Job).filter(Job.id == record_id)
    if not existing_record.first():
        return 0
    job.dict().update(owner_id=owner_id)
    existing_record.update(job.dict())
    db.commit()
    return 1

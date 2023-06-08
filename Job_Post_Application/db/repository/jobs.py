
from sqlalchemy.orm import Session
from db.model.jobs import Job
from schema.jobs import JobCreate


def create_new_job(job: JobCreate, db: Session, owner_id: int) -> Job:
    job_object = Job(**job.dict(), owner_id=owner_id)
    db.add(job_object)
    db.commit()
    db.refresh(job_object)
    return job_object

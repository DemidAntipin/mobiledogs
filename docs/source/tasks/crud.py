from tasks import models, schemas
from sqlalchemy.orm import Session

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskBase):
    db_task = models.Task(dog_id=task.dog_id,type=task.type)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def change_task_status(db: Session, task_id: int,status:bool):
    db_task=db.query(models.Task).filter(models.Task.id == task_id).first()
    db_task.status=status
    db.commit()
    db.refresh(db_task)
    return db_task

def get_all_task_responses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TaskResponse).filter(models.TaskResponse.delete==0).offset(skip).limit(limit).all()

def get_task_response(db: Session, response_id:int):
    return db.query(models.TaskResponse).filter(models.TaskResponse.id == response_id).first()

def get_task_responses(db: Session, task_id:int):
    return db.query(models.TaskResponse).filter(models.TaskResponse.task_id == task_id).filter(models.TaskResponse.delete==0).all()

def create_task_response(db: Session, item: schemas.TaskResponseBase, task_id: int,user_id:int):
    db_taskresponse = models.TaskResponse(**item.dict(), task_id=task_id,user_id=user_id)
    db.add(db_taskresponse)
    db.commit()
    db.refresh(db_taskresponse)
    return db_taskresponse

def change_response_status(db: Session, response_id: int,status:bool):
    db_response=db.query(models.TaskResponse).filter(models.TaskResponse.id == response_id).first()
    db_response.delete=status
    db.commit()
    db.refresh(db_response)
    return db_response

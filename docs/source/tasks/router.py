from fastapi import APIRouter, Depends
from database import DBSession
from .schemas import TaskBase, Task, TaskResponse, TaskResponseBase
from dependencies import get_db_session
from tasks.crud import create_task as create_db_task, get_tasks, get_task, create_task_response as create_db_task_response
from tasks.crud import get_task_response, change_response_status, get_task_responses, get_all_task_responses, change_task_status
from users.crud import get_user_by_token
from dogs.crud import get_dog
from .exceptions import task_not_found, response_not_found
from users.exceptions import invalid_token
from dogs.exceptions import dog_not_found
from logger import get_logger

router = APIRouter()

log = get_logger("tasks_router")

router = APIRouter()

@router.post("/task/create")
def create_task(token:str,task: TaskBase, db: DBSession = Depends(get_db_session)):
    log.info("Adding task to database")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    dog=get_dog(db, dog_id=task.dog_id)
    if dog is None:
        log.error(f"Dog with id {dog.id} doesn't exist")
        raise dog_not_found()
    task=create_db_task(db=db, task=task)
    log.info("Task is created")
    return {"success":"true","exception":"null","task_id":task.id}


@router.get("/task", response_model=list[Task])
def read_tasks(token:str,skip: int = 0, limit: int = 10, db: DBSession = Depends(get_db_session)):
    log.info("Reading list of tasks")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    tasks = get_tasks(db, skip=skip, limit=limit)
    log.info("List of tasks is read")
    return tasks


@router.get("/task/{task_id}", response_model=Task)
def read_task(token:str,task_id: int, db: DBSession = Depends(get_db_session)):
    log.info("Reading the task")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    db_task = get_task(db, task_id=task_id)
    if db_task is None:
        log.error("Task doesn't exist")
        raise task_not_found()
    return db_task

@router.post("/task/{task_id}/change_status")
def change_task(token:str,task_id: int,status:bool, db: DBSession = Depends(get_db_session)):
    log.info(f"Changing task {task_id} status")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    db_task = get_task(db, task_id=task_id)
    if db_task is None:
        log.error("Task doesn't exist")
        raise task_not_found()
    task=change_task_status(db=db, task_id=task_id,status=status)
    log.info("Task status successfully changed")
    return {"success":"true","exception":"null","task_id":task.id}


@router.post("/task/{task_id}/responses/send", response_model=TaskResponse)
def create_task_response(token:str,task_id:int,item: TaskResponseBase, db: DBSession = Depends(get_db_session)):
    log.info(f"Creating response for task {task_id}")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    db_task = get_task(db, task_id=task_id)
    if db_task is None:
        log.error(f"Task with id {task_id} doesn't exist")
        raise task_not_found()
    log.info(f"Response for task {task_id} is created")
    return create_db_task_response(db=db, item=item, task_id=task_id,user_id=tokencheck.id)

@router.post("/task/responses/{response_id}/delete")
def change_response(token:str,response_id: int, db: DBSession = Depends(get_db_session)):
    log.info(f"Changing status for response {response_id}")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    db_response = get_task_response(db, response_id=response_id)
    if db_response is None:
        log.error(f"Response with id {response_id} doesn't exist")
        raise response_not_found()
    response=change_response_status(db=db, response_id=response_id,status=1)
    log.info(f"Response status with id {response_id} changed")
    return {"success":"true","exception":"null","response_id":response.id}


@router.get("/task/{task_id}/responses", response_model=list[TaskResponse])
def get_task_responses(token:str,task_id: int, db: DBSession = Depends(get_db_session)):
    log.info("Reading task responses")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    log.info("Task responses are read")
    return get_task_responses(db=db, task_id=task_id)


@router.get("/responses", response_model=list[TaskResponse])
def read_all_responses(token:str,skip: int = 0, limit: int = 10, db: DBSession = Depends(get_db_session)):
    log.info("Reading list of responses")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    items = get_all_task_responses(db, skip=skip, limit=limit)
    log.info("Responses are read")
    return items

from pydantic import BaseModel

class TaskResponseBase(BaseModel):
    proof:str
    delete:bool

class TaskResponse(TaskResponseBase):
    id: int
    task_id:int
    user_id:int

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    dog_id: int
    type: str

class Task(TaskBase):
    id: int
    responses:list[TaskResponse] = []
    status: bool=True
    class Config:
        orm_mode = True

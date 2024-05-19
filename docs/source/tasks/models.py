from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import BaseDBModel

class Task(BaseDBModel):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer, ForeignKey("dogs.id"))
    type = Column(String)
    status = Column(Boolean, default=False)

    responses = relationship("TaskResponse", back_populates="task")

class TaskResponse(BaseDBModel):
    __tablename__ = "taskresponses"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    proof=Column(String)
    user_id=Column(Integer, ForeignKey("users.id"))
    delete=Column(Boolean, default=True)

    task=relationship("Task", back_populates="responses")

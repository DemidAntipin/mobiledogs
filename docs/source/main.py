from fastapi import FastAPI
import uvicorn
from users.router import router as user_router
from dogs.router import router as dog_router
from tasks.router import router as task_router
from database import BaseDBModel, engine

BaseDBModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(dog_router)
app.include_router(task_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

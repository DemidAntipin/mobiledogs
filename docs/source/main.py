from fastapi import FastAPI
from src.users.router import router as urouter
from src.database import BaseDBModel, engine

BaseDBModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(urouter)

@app.get('/')
def greet():
	return {"message":"Hello world!"}

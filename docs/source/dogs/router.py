from fastapi import APIRouter, Depends
from src.database import DBSession
from .schemas import DogCreate, DogBase
from source.dependencies import get_db_session
from source.dogs.crud import create_dog as create_db_dog
from source.dogs.crud import get_dog_by_email

router = APIRouter()

@router.post("/create_dog", response_model=UserBase)
def create_dog(user: UserCreate, db: DBSession = Depends(get_db_session)):
	created_user = create_db_user(db,user)
	created_user = UserBase(name=user.name, email=user.email)
	return created_user

@router.get("/user", response_model=UserBase)
def get_user(email:str, db:DBSession=Depends(get_db_session)):
	return get_user_by_email(db,email)

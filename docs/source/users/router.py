from fastapi import APIRouter, Depends
from src.database import DBSession
from .schemas import UserCreate, UserBase
from src.dependencies import get_db_session
from src.users.crud import create_user as create_db_user
from src.users.crud import get_user_by_email

router = APIRouter()

@router.post("/create_user", response_model=UserBase)
def create_user(user: UserCreate, db: DBSession = Depends(get_db_session)):
	created_user = create_db_user(db,user)
	created_user = UserBase(name=user.name, email=user.email)
	return created_user

@router.get("/user", response_model=UserBase)
def get_user(email:str, db:DBSession=Depends(get_db_session)):
	return get_user_by_email(db,email)

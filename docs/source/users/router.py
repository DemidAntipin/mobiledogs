from fastapi import APIRouter, Depends
from database import DBSession
from .schemas import UserCreate, User
from dependencies import get_db_session
from users.crud import create_user as create_db_user, get_user_by_email, get_user_by_phone 
from users.crud import get_user_by_name, get_users_token, get_user_by_token, get_users, get_user
from .exceptions import email_collision, phone_collision, name_collision, invalid_login, invalid_token, user_not_found
from logger import get_logger

router = APIRouter()

log = get_logger("user_router")

@router.post("/users/register")
def create_user(user: UserCreate, db: DBSession = Depends(get_db_session)):
    log.info("Registration of new user")
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        log.error("Error. User with such email already exists")
        raise email_collision()
    db_user = get_user_by_phone(db, phone=user.phone)
    if db_user:
        log.error("Error. User with such phone already exists")
        raise phone_collision()
    db_user = get_user_by_name(db, name=user.name)
    if db_user:
        log.error("Error. User with such name already exists")
        raise name_collision()
    db_user=create_db_user(db=db, user=user)
    log.info("User registrated")
    return {"name":db_user.name,"token":db_user.token}

@router.post("/users/login")
def login_user(name:str,password:str, db: DBSession = Depends(get_db_session)):
    log.info(f"Logging as user {name}")
    db_user=get_users_token(db=db,name=name,password=password)
    log.info(f"Data of {name} is valid. Successful logging.")
    return {"name":db_user.name,"token":db_user.token}


@router.get("/users/", response_model=list[User])
def read_users(token:str,skip: int = 0, limit: int = 10, db: DBSession = Depends(get_db_session)):
    log.info("Reading list of users")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token. Access denied.")
        raise invalid_token()
    users = get_users(db, skip=skip, limit=limit)
    for user in users:
       user.token="######"
    log.info("list of users is read")
    return users


@router.get("/users/{user_id}", response_model=User)
def read_user(token:str,user_id: int, db: DBSession = Depends(get_db_session)):
    log.info("Reading user")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token. Access denied.")
        raise invalid_token()
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        log.error("Error. User doesn't exists")
        raise user_not_found()
    db_user.token="######"
    log.info("User is read")
    return db_user

from users import models, schemas
from sqlalchemy.orm import Session
from .exceptions import invalid_login
from werkzeug.security import generate_password_hash, check_password_hash
from logger import get_logger
import hashlib

log = get_logger("user_auth")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_user_by_phone(db: Session, phone: str):
    return db.query(models.User).filter(models.User.phone == phone).first()

def get_user_by_token(db: Session, token: str):
    return db.query(models.User).filter(models.User.token == token).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_users_token(db: Session, name: str, password:str):
    user = db.query(models.User).filter(models.User.name == name).first()
    log.info("Starting validation of user data")
    if user and user.check_password(password):
       log.info("Data is valid")
       return user
    else:
       log.error("invalid data")
       raise invalid_login()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email,phone=user.phone, name=user.name, hash_password=generate_password_hash(user.password), token=hashlib.md5((user.name+user.password).encode()).hexdigest())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

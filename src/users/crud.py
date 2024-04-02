from src.users import models, schemas
from sqlalchemy.orm import Session

def create_user(db: Session, user : schemas.UserCreate) -> models.User:
	fake_hash="gegeeg"
	db_user = models.User(name=user.name, email=user.email, hash_password=fake_hash)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user

def get_user_by_email(db:Session, email:str):
	db_user = db.query(models.User).filter(models.User.email==email).first()
	return db_user

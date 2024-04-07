from source.dogs import models, schemas
from sqlalchemy.orm import Session

def new_dog(db: Session, dog : schemas.DogCreate) -> models.Dog:
	db_dog = models.User(name=dog.name, osheinic_id=dog.osheinic_id, last_cared=dog.last_cared)
	db.add(db_dog)
	db.commit()
	db.refresh(db_dog)
	return db_dog

def get_user_by_email(db:Session, email:str):
	db_user = db.query(models.User).filter(models.User.email==email).first()
	return db_user

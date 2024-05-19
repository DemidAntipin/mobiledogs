from dogs import models, schemas
from sqlalchemy.orm import Session

def get_dog(db: Session, dog_id: int):
    return db.query(models.Dog).filter(models.Dog.id == dog_id).first()

def get_dog_by_collar_id(db: Session, collar_id: int):
    return db.query(models.Dog).filter(models.Dog.collar_id == collar_id).first()

def get_dogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dog).offset(skip).limit(limit).all()

def get_near_dogs(db: Session, latitude:str , longitude:str , skip: int = 0, limit: int = 10):
	dogs=db.query(models.Dog).offset(skip).limit(limit).all()
	answer=[]
	for dog in dogs:
            if (len(dog.datas)>0):
                if (abs(float(dog.datas[-1].latitude)-float(latitude))<=1 and abs(float(dog.datas[-1].longitude)-float(longitude))<=1):
                    answer.append(dog)
	return answer


def new_dog(db: Session, dog: schemas.DogBase):
    db_dog = models.Dog(name=dog.name,description=dog.description, collar_id=dog.collar_id)
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

def get_collar(db: Session, collar_id: int):
    return db.query(models.Collar).filter(models.Collar.id == collar_id).first()

def get_collar_by_ip(db: Session, ip: str):
    return db.query(models.Collar).filter(models.Collar.ip == ip).first()

def get_collars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Collar).offset(skip).limit(limit).all()

def new_collar(db: Session, collar: schemas.CollarBase):
    db_collar = models.Collar(ip=collar.ip)
    db.add(db_collar)
    db.commit()
    db.refresh(db_collar)
    return db_collar

def get_all_dogs_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DogsData).offset(skip).limit(limit).all()

def get_dogs_data(db: Session, dog_id:int):
    return db.query(models.DogsData).filter(models.DogsData.dog_id == dog_id).all()

def new_dogs_data(db: Session, item: schemas.DogsDataBase, dog_id: int):
    db_data = models.DogsData(**item.dict(), dog_id=dog_id)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

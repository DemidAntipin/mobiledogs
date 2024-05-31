from fastapi import APIRouter, Depends
from database import DBSession
from .schemas import Dog, DogBase, Collar, CollarBase, DogsData, DogsDataBase
from dependencies import get_db_session
from dogs.crud import get_dog, get_dog_by_collar_id, get_dogs, get_near_dogs, new_dog
from dogs.crud import get_collar, get_collar_by_ip, get_collars, new_collar
from dogs.crud import get_dogs_data, get_all_dogs_data, new_dogs_data
from users.crud import get_user_by_token
from .exceptions import collar_collision, collar_not_found, dog_not_found, ip_collision, invalid_ip
from users.exceptions import invalid_token
from logger import get_logger

router = APIRouter()

log = get_logger("dogs_router")

router = APIRouter()

@router.post("/dogs/register")
def create_dog(token:str, dog: DogBase, db: DBSession = Depends(get_db_session)):
    log.info(f"Adding a dog to database")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    db_dog = get_dog_by_collar_id(db, collar_id=dog.collar_id)
    if db_dog:
        log.error("Dog with such collar already exists")
        raise collar_collision()
    db_collar=get_collar(db, collar_id=dog.collar_id)
    if db_collar is None:
        log.error(f"Collar {dog.collar_id} doesn't exist")
        raise collar_not_found()
    dog=new_dog(db=db, dog=dog)
    log.info(f"Dog {dog.id} added to database")
    return {"success":"true","exception":"null","dog_id":dog.id}


@router.get("/dogs/", response_model=list[Dog])
def read_dogs(token:str,near:bool=False,latitude:str ="0", longitude:str="0",skip: int = 0, limit: int = 10, db: DBSession = Depends(get_db_session)):
    log.info("Reading list of dogs")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
       log.error("Invalid token")
       raise invalid_token()
    if near:
       dogs = get_near_dogs(db,latitude=latitude , longitude=longitude , skip=skip, limit=limit)
    else:
       dogs = get_dogs(db, skip=skip, limit=limit)
    log.info("list of dogs is read")
    return dogs

@router.get("/dogs/{dog_id}", response_model=Dog)
def read_dog(token:str,dog_id: int, db: DBSession = Depends(get_db_session)):
    log.info("Reading the dog")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    db_dog = get_dog(db, dog_id=dog_id)
    if db_dog is None:
        log.erroe("Dog doesn't exist")
        raise dog_not_found
    log.info("Dog is read")
    return db_dog

@router.post("/collars/register")
def create_collar(token:str,collar: CollarBase, db: DBSession = Depends(get_db_session)):
    log.info("Adding collar to database")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token
    db_collar = get_collar_by_ip(db, ip=collar.ip)
    if db_collar:
        log.error("Collar with such IP already exists")
        raise ip_collision()
    collar=new_collar(db=db, collar=collar)
    log.info(f"Collar {collar.id} added to database")
    return {"success":"true","exception":"null","id":collar.id}


@router.get("/collars/", response_model=list[Collar])
def read_collars(token:str,skip: int = 0, limit: int = 100, db: DBSession = Depends(get_db_session)):
    log.info("Reading list of collars")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    collars = get_collars(db, skip=skip, limit=limit)
    log.info("List of collars is read")
    return collars


@router.get("/collars/{collar_id}", response_model=Collar)
def read_collar_by_id(token:str,collar_id: int, db: DBSession = Depends(get_db_session)):
    log.info(f"Reading collar by id {collar_id}")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    db_collar = get_collar(db, collar_id=collar_id)
    if db_collar is None:
        log.error("Collar with id {collar_id} doesn't exist")
        raise collar_not_found()
    log.info("Collar is read")
    return db_collar

@router.get("/collars/getbyip/{collar_ip}", response_model=Collar)
def read_collar_by_ip(collar_ip:str,token:str, db: DBSession = Depends(get_db_session)):
    log.info("Reading collar by IP")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    db_collar = get_collar_by_ip(db, ip=collar_ip)
    if db_collar is None:
        log.error("Collar with such IP doesn't exist")
        raise collar_not_found()
    log.info("Collar is read")
    return db_collar


@router.post("/dogs/{dog_id}/data", response_model=DogsData)
def create_data_for_dog(ip:str,dog_id: int, item: DogsDataBase, db: DBSession = Depends(get_db_session)):
    log.info("Recieved data for dog")
    db_collar = get_collar_by_ip(db, ip=ip)
    if db_collar is None:
        log.error("Collar with such IP doesn't exist")
        raise invalid_ip()
    log.info("Data successfully proccessed")
    return new_dogs_data(db=db, item=item, dog_id=dog_id)

@router.get("/dogs/{dog_id}/status", response_model=list[DogsData])
def get_data_for_dog(token:str,dog_id: int, db: DBSession = Depends(get_db_session)):
    log.info("Reading dogs data")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    data = get_dogs_data(db=db, dog_id=dog_id)
    if data is None:
        log.error(f"Dog with id {dog_id} doesn't exist")
        raise dog_not_found()
    log.info("Data is read")
    return data

@router.get("/data", response_model=list[DogsData])
def read_dogsdata(token:str,skip: int = 0, limit: int = 10, db: DBSession = Depends(get_db_session)):
    log.info("Reading list of data")
    tokencheck = get_user_by_token(db, token=token)
    if tokencheck is None:
        log.error("Invalid token")
        raise invalid_token()
    items = get_all_dogs_data(db, skip=skip, limit=limit)
    log.info("List of data is read")
    return items

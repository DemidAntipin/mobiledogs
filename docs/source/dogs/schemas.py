from pydantic import BaseModel

class CollarBase(BaseModel):
    ip: str

class Collar(CollarBase):
    id: int

    class Config:
        orm_mode = True

class DogsDataBase(BaseModel):
    latitude:str
    longitude:str
    datetime:str

class DogsData(DogsDataBase):
    id: int
    dog_id:int

    class Config:
        orm_mode = True


class DogBase(BaseModel):
    name: str
    description: str
    collar_id: int

class Dog(DogBase):
    id: int
    datas:list[DogsData] = []

    class Config:
        orm_mode = True

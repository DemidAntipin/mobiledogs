from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import BaseDBModel

class Collar(BaseDBModel):
    __tablename__ = "collars"

    id = Column(Integer, primary_key=True)
    ip = Column(String, unique=True, index=True)

class Dog(BaseDBModel):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    collar_id=Column(Integer, ForeignKey("collars.id"))
    datas = relationship("DogsData", back_populates="dog")

class DogsData(BaseDBModel):
    __tablename__ = "dogsdatas"

    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer, ForeignKey("dogs.id"))
    latitude=Column(String)
    longitude=Column(String)
    datetime=Column(String)
    
    dog = relationship("Dog", back_populates="datas")

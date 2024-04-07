from pydantic import BaseModel

class DogBase(BaseModel):
	name : str

class DogCreate(DogBase):
	osheinic_id : int

class Dog(DogBase):
	id: int
	last_cared : str
	class Config:
		orm_mode = True

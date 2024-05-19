from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
	name : str
	email : EmailStr
	phone: str

class UserCreate(UserBase):
	password : str

class User(UserBase):
	id: int
	token : str
	class Config:
		orm_mode = True

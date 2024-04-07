from sqlalchemy import Boolean, Column, Integer, String
from src.database import BaseDBModel

class User(BaseDBModel):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	name = Column(String, unique=False, index=False)
	email = Column(String, unique=True, index=True)
	hash_password = Column(String, unique=False, index=False)
	is_active = Column(Boolean, default=True)
	service = Column(Boolean, default=False)
	latitude = Column(Integer, index=True)
	longitute = Column(Integer, index=True)

from sqlalchemy import Column, Integer, String, Datetime
from source.database import BaseDBModel

class Dog(BaseDBModel):
	__tablename__ = "dogs"

	id = Column(Integer, primary_key=True)
	name = Column(String, unique=False, index=False)
	osheinic_id = Column(Integer, unique=True)
	last_cared = Column(Datetime, index=True)

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from werkzeug.security import check_password_hash
from database import BaseDBModel

class User(BaseDBModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hash_password = Column(String)
    phone=Column(String, unique=True, index=True)
    token=Column(String)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)

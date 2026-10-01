from app import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), unique=False, nullable=False)
    last_name = Column(String(150), unique=False, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(250), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
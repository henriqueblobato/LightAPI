from sqlalchemy import Column, Integer, String
from database import CustomBase


class Person(CustomBase):
    pk = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)
    email = Column(String, unique=True)


class Company(CustomBase):
    pk = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String)
    email = Column(String, unique=True)

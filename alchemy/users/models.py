from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class NewsLetter(Base):
    __tablename__ = "newsletters"

    id = Column(Integer, primary_key=True)
    title = Column(String)

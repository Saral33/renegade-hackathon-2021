from enum import auto
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import ARRAY, BOOLEAN, TIMESTAMP
from .database import Base

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, nullable=False)
#     email = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False)
#     created_at =Column(TIMESTAMP(timezone=True), server_default=text('now()'))

# class Post(Base):
#     __tablename__ = "posts"
#     user_id = Column(ForeignKey, )
#     id = Column(Integer, primary_key=True, nullable=False)
#     title = Column(String, nullable=False)
#     content = Column(String, nullable=False)
#     published = Column(Boolean, server_default="True")
#     created_at =Column(TIMESTAMP(timezone=True), server_default=text('now()'))
#     user_id = Column(
#         Integer,
#         ForeignKey('users.id', ondelete='CASCADE'),
#         nullable=False,
#     )  


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at =Column(TIMESTAMP(timezone=True), server_default=text('now()'))


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True,nullable=False)
    question = Column(String)
    yes = Column(Integer)
    no = Column(Integer)
    
  
    
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id',ondelete= 'CASCADE'),nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="True")
    created_at =Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Answer(Base):
    __tablename__ = 'answers' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id',ondelete= 'CASCADE'),nullable=False)
    question_id = Column( ForeignKey('questions.id',ondelete= 'CASCADE'), nullable=False)
    answer = Column(Boolean, nullable=False)


    

    
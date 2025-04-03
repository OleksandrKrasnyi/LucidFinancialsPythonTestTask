from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))

class Post(Base):
    """Post model"""
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(1048576))  # 1MB limit
    user_id = Column(Integer, ForeignKey("users.id"))
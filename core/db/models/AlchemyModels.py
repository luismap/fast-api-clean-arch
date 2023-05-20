
from sqlalchemy import Boolean, Column, TIMESTAMP, ForeignKey, Integer, String, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text, func

from core.db.AlchemySql import Base


class PostsAlmy(Base):
    __tablename__ = "posts"
    __table_args__ = {'schema': 'fast_api'}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False)
    content = Column(String)
    published = Column(Boolean, server_default="false")
    rating = Column(SmallInteger, server_default="0")
    user_id = Column(Integer, ForeignKey("fast_api.user.user_id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())


class UserAlmy(Base):
    __tablename__="user"
    __table_args__= {'schema': 'fast_api'}

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at= Column(TIMESTAMP, server_default=func.now())
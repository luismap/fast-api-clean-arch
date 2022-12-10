
from sqlalchemy import Boolean, Column, TIMESTAMP, Integer, String, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text, func

from core.db.AlchemySql import Base


class PostsAlmy(Base):
    __tablename__ = "posts_almy"
    __table_args__ = {'schema': 'fast_api'}

    schema = "fast_api"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=False)
    content = Column(String)
    publish = Column(Boolean, server_default="false")
    rating = Column(SmallInteger, server_default="0")
    created_ad = Column(TIMESTAMP, server_default=func.now())
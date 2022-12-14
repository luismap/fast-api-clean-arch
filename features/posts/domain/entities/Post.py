from __future__ import annotations
import logging
from typing import Optional
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostBase(BaseModel):
    """common attributes while creating or reading data."""
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None
    created_at: datetime = datetime.now()

class PostCreate(PostBase):
    """create a PostCreate that inherit from PostBase (so they will have the same attributes),
     plus any additional data (attributes) needed for creation"""
    id: Optional[int]
    class Config:
        orm_mode = True


class Post(PostBase):
    """
    Pydantic models (schemas) that will be used when reading data,
     when returning it from the API
     ex. id - will only be present once the data has been pushed
    """
    id: int = -99 
    """
    tell the Pydantic model to read the data even if it is not a dict, 
    but an ORM model (or any other arbitrary object with attributes)
    """
    class Config:
        orm_mode = True

class PostResponse(BaseModel):
    title: str
    content: str
    #published: bool = False
    #rating: Optional[int] = None
    #created_at: datetime = datetime.now()

    class Config:
        orm_mode = True
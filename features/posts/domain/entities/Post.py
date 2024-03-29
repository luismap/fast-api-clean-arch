from __future__ import annotations
import logging
from typing import Optional
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from features.user.data.models.UserModel import UserResponse


class PostBase(BaseModel):
    """common attributes while creating or reading data."""

    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None
    created_at: datetime = datetime.now()
    user_id: int = -99


class Post(PostBase):
    """Class to be use for Model design"""

    id: Optional[int]

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    """create a PostCreate that inherit from PostBase (so they will have the same attributes),
    plus any additional data (attributes) needed for creation"""

    id: Optional[int]

    class Config:
        orm_mode = True


class PostRead(PostBase):
    """
    Pydantic models (schemas) that will be used when reading data,
     when returning it from the API
     ex. id - will only be present once the data has been pushed
    """

    id: int = -99
    user_id: int
    """
    tell the Pydantic model to read the data even if it is not a dict, 
    but an ORM model (or any other arbitrary object with attributes)
    """
    votes: int = 0  # just adding it here for simplicity, needs to be refactor

    class Config:
        orm_mode = True


class PostResponse(BaseModel):
    """
    Pydantic use for api response
    """

    id: int
    title: str
    content: str
    user_id: int
    user: UserResponse
    # published: bool = False
    # rating: Optional[int] = None
    # created_at: datetime = datetime.now()
    votes: int = 0

    class Config:
        orm_mode = True

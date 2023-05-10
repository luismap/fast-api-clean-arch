from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    """common attributes while creating or reading data."""
    user_id: str
    email: str 

class UserModel(UserBase):
    """model use by the application"""
    class Config:
        orm_mode = True
    
class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    user_id: int = -99
    created_at: datetime = datetime.now()

class UserResponse(UserBase):
    user_id: int
    email: str
    created_at: datetime
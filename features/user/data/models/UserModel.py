


from datetime import datetime

from pydantic import BaseModel
from features.user.domain.entities.User import User

    

class UserModel(User):
    """model use by the application"""
    class Config:
        orm_mode = True

class UserCreate(UserModel):
    pass

class UserRead(User):
    user_id: int = -99
    created_at: datetime = datetime.now()
    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    user_id: int
    email: str
    created_at: datetime
    class Config:
        orm_mode = True


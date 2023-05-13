from __future__ import annotations
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    """common attributes while creating or reading data."""
    email: EmailStr
    password: str
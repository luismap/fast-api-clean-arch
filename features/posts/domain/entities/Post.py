from tokenize import String
from typing import Optional
from uuid import UUID, uuid1
from pydantic import BaseModel

class Post(BaseModel):
    id: int = -99
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
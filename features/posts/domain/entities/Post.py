from __future__ import annotations
import logging
from typing import Optional
from pydantic import BaseModel

class Post(BaseModel):
    id: int = -99
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None
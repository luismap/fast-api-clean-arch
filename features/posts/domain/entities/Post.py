from __future__ import annotations
import logging
from typing import Optional
from pydantic import BaseModel

from core.utils.MyUtils import MyUtils

appProps = MyUtils.loadProperties("general")["app"]
logger = logging.getLogger(appProps["logger"])

class Post(BaseModel):
    id: int = -99
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None


    def update(self, data: dict) -> Post:
        logger = logging.getLogger(appProps["logger"])
        for k,v in data.items():
            logger.info(f"updating value of '{k}' from '{getattr(self, k, None)}' to '{v}'")      
            setattr(self, k, v)
        return self
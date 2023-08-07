

import yaml
from passlib.context import CryptContext
import os

crypt_context = CryptContext(schemes="bcrypt", deprecated="auto")

class MyUtils:  
    def __init__(self) -> None:
        pass
    """
    given a top level key, get corresponding configs
    """
    def loadProperties(key: str) -> dict:
        with open("properties.yaml","r") as f:
            props = yaml.safe_load(f)
            return props[key]
        
    def get_from_os(var: str) -> str:
        return os.getenv(var)
    
    def hash(content: str) -> str:
        return crypt_context.hash(content)

    def verify(content: str, hashed_content: str) -> bool:
        return crypt_context.verify(content, hashed_content)


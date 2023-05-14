

import yaml
from passlib.context import CryptContext

crypt_context = CryptContext(schemes="bcrypt", deprecated="auto")

class MyUtils:
    """
    given a top level key, get corresponding configs
    """
    def __init__(self) -> None:
        pass
    
    def loadProperties(key: str) -> dict:
        with open("properties.yaml","r") as f:
            props = yaml.safe_load(f)
            return props[key]

    def hash(content: str) -> str:
        return crypt_context.hash(content)

    def verify(content: str, hashed_content: str) -> bool:
        return crypt_context.verify(content, hashed_content)


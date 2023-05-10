

import yaml

class MyUtils():
    """
    given a top level key, get corresponding configs
    """
    def __init__(self) -> None:
        pass
    
    def loadProperties(key: str) -> dict:
        with open("properties.yaml","r") as f:
            props = yaml.safe_load(f)
            return props[key]


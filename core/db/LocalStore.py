
from asyncio.log import logger
import json
from logging import Logger
import logging

from core.utils.MyUtils import MyUtils

"""
Interact with local files
Helper class mainly for testing purpose
"""
class LocalStore:

    def __init__(self) -> None:
        self.appProps = MyUtils.loadProperties("general")["app"]
        self.logger = logging.getLogger(self.appProps["logger"])

    def isAvailable(self, file: str) -> bool:
        try:
            f = open(file, 'r')
            self.logger.info("local db available")
            return True
        except Exception as ex:
            self.logger.info(f"problem reading file: {ex}")
            return False



    def getLocalData(self,file: str) -> list[dict]:
         with open(file, "r") as f:
            return json.load(f)["data"]
    
    def dumpLocalData(self, file: str, posts: list[dict]) -> bool:
        with open(file, "w") as f:
            json.dump({"data": [e for e in posts]},f)

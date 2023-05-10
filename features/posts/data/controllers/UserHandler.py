

import logging
from core.utils.MyUtils import MyUtils
from features.posts.data.datasources.UserAlchemyDS import UserAlchemyDS

import features.posts.data.models.UserModel as um
from features.posts.domain.controllers.UserController import UserController



class UserHandler(UserController):
    @classmethod
    def __init__(self,
                 user_alchemy_ds: UserAlchemyDS
                 ) -> None:
        
        self.app_props = MyUtils.loadProperties("general")["app"]
        self.app_state = self.app_props["env"]
        self.logger = logging.getLogger(self.app_props["logger"])
        self.data_source = user_alchemy_ds
        self.logger.info("using user alchemy data source")
            
    @classmethod
    def get_user(self,id: int) -> um.UserModel:
        return self.data_source.get_user(id)        

    @classmethod
    def create_user(self, payload: um.UserCreate) -> um.UserRead:
        return self.data_source.create_user(payload)
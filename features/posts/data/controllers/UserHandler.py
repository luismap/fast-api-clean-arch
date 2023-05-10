

import logging
from core.utils.MyUtils import MyUtils
from features.posts.data.datasources.UserAlchemyDS import UserAlchemyDS
from features.posts.data.datasources.api.UserDataSource import UserDataSource
from features.posts.domain.controllers.UserController import UserController
from features.posts.domain.entities.User import UserModel


class UserHandler(UserController):
    def __init__(self,
                 user_alchemy_ds: UserAlchemyDS
                 ) -> None:
        
        self.app_props = MyUtils.loadProperties("general")["app"]
        self.app_state = self.app_props["env"]
        self.logger = logging.getLogger(self.app_props["logger"])
        self.data_source = user_alchemy_ds
        self.logger.info("using user alchemy data source")
            
    
    def get_user(self,id: int) -> UserModel:
        return self.data_source.get_user(id)        
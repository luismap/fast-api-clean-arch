
from features.posts.data.controllers.UserHandler import UserHandler
from features.posts.domain.entities.User import UserModel


class UserCrud:
    def __init__(self, user_handler: UserHandler) -> None:
        self.user_handler = user_handler

    def get_user(self, id: int) -> UserModel:
        return self.user_handler.get_user(id)

from features.user.data.controllers.UserHandler import UserHandler
import features.user.data.models.UserModel as um


class UserCrud:
    def __init__(self, user_handler: UserHandler) -> None:
        self.user_handler = user_handler

    def get_user(self, id: int) -> um.UserRead:
        return self.user_handler.get_user(id)

    def create_user(self, payload: um.UserCreate) -> um.UserRead:
        return self.user_handler.create_user(payload)

    def get_user_by_email(self, email: str) -> um.UserRead:
        return self.user_handler.get_user_by_email(email)
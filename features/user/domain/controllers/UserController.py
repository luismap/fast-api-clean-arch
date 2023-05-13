
from abc import ABC

from features.user.data.models.UserModel import UserCreate, UserModel, UserRead


class UserController(ABC):
    @classmethod
    def get_user(id: int) -> UserModel:
        pass

    @classmethod
    def create_user(payload: UserCreate) -> UserRead:
        pass

    @classmethod
    def get_user_by_email(email: str) -> UserRead:
        pass
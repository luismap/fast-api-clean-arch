
from abc import ABC

from features.user.data.models.UserModel import UserCreate, UserModel, UserRead


class UserController(ABC):
    @classmethod
    def get_user(id: int) -> UserModel:
        pass

    @classmethod
    def create_user(payload: UserCreate) -> UserRead:
        pass
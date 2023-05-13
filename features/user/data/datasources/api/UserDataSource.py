


from abc import ABC

import features.user.data.models.UserModel as um

class UserDataSource(ABC):
    @classmethod
    def get_users(id: int) -> um.UserRead:
        pass

    @classmethod
    def is_available() -> bool:
        pass

    @classmethod
    def create_user(payload: um.UserCreate) -> um.UserRead:
        pass

    @classmethod
    def get_user_by_email(email: str) -> um.UserRead:
        pass
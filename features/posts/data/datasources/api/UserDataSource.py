


from abc import ABC

import features.posts.data.models.UserModel as um

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
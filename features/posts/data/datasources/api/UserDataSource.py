


from abc import ABC, ABCMeta

from features.posts.domain.entities.User import UserModel


class UserDataSource(ABC):
    @classmethod
    def get_users(id: int) -> UserModel:
        pass

    @classmethod
    def is_available() -> bool:
        pass
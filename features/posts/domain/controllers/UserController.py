
from abc import ABC, ABCMeta, abstractmethod

from features.posts.domain.entities.User import UserModel

class UserController(ABC):
    @abstractmethod
    def get_user(id: int) -> UserModel:
        pass
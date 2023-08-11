
from abc import ABC, abstractmethod
from typing import List

from features.votes.data.models.VotesModel import VoteResponseModel



class VotesController(ABC):
    @abstractmethod
    def delete_vote(post_id: int) -> VoteResponseModel:
        pass

    @abstractmethod
    def vote(post_id: int) -> List[VoteResponseModel]:
        pass

    @abstractmethod
    def get_votes() -> List[VoteResponseModel]:
        pass

from abc import ABC, abstractmethod
from typing import List

from features.votes.data.models.VotesModel import VoteReadModel, VoteResponseModel




class VotesDataSource(ABC):
    @abstractmethod
    def delete_vote(post_id: int) -> VoteResponseModel:
        pass

    @abstractmethod
    def get_votes() -> List[VoteReadModel]:
        pass

    @abstractmethod
    def get_my_votes(user_id: int) -> List[VoteReadModel]:
        pass

from abc import ABC, abstractmethod
from typing import List

from features.votes.data.models.VotesModel import VoteModel, VoteReadModel, VoteResponseModel




class VotesDataSource(ABC):

    @abstractmethod
    def create_vote(vote: VoteModel):
        pass

    @abstractmethod
    def delete_vote(post_id: int) -> bool:
        pass

    @abstractmethod
    def get_votes() -> List[VoteReadModel]:
        pass

    @abstractmethod
    def get_my_votes(user_id: int) -> List[VoteReadModel]:
        pass

    @abstractmethod
    def vote(post_id: int, user_id: int, direction: int) -> VoteReadModel:
        pass
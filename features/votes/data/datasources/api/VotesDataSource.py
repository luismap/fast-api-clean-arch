
from abc import ABC, abstractmethod
from typing import List

from features.votes.domain.entities.Votes import VoteRead, VoteResponse


class VotesDataSource(ABC):
    @abstractmethod
    def get_user_votes(user_id: int) -> List[VoteRead]:
        pass

    @abstractmethod
    def delete_vote(post_id: int) -> VoteResponse:
        pass

    @abstractmethod
    def get_votes() -> List[VoteRead]:
        pass
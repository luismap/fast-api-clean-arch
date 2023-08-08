
from abc import ABC, abstractmethod
from typing import List
from features.votes.domain.entities.Votes import VoteResponse


class VotesController(ABC):
    @abstractmethod
    def delete_vote(post_id: int) -> VoteResponse:
        pass

    @abstractmethod
    def vote(post_id: int) -> List[VoteResponse]:
        pass

    @abstractmethod
    def get_votes() -> List[VoteResponse]:
        pass
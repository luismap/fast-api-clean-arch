

from typing import List
from features.votes.data.controller.VotesHandler import VotesHandler
from features.votes.domain.entities.Votes import VoteResponse


class VotesCrud():
    def __init__(self, votes_handler: VotesHandler) -> None:
        self.votes_handler= votes_handler

    def get_votes(self) -> List[VoteResponse]:        
        return self.votes_handler.get_votes()
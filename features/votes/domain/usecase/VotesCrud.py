

from typing import List
from features.votes.data.controller.VotesHandler import VotesHandler
from features.votes.data.models.VotesModel import VoteResponseModel


class VotesCrud():
    def __init__(self, votes_handler: VotesHandler) -> None:
        self.votes_handler= votes_handler

    def get_votes(self) -> List[VoteResponseModel]:        
        return self.votes_handler.get_votes()
    
    def get_my_votes(self, user_id: int) -> List[VoteResponseModel]:
        return self.votes_handler.get_my_votes(user_id)
    
    def create_vote(self, post_id, user_id, direction:bool) -> VoteResponseModel:
        return self.votes_handler.vote(post_id,user_id, direction)
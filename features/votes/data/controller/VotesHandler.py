

import logging
from typing import List
from core.utils.MyUtils import MyUtils
from features.votes.data.datasources.VotesAlchemyDS import VotesAlchemyDS
from features.votes.data.models.VotesModel import VoteResponseModel
from features.votes.domain.controller.VotesController import VotesController



class VotesHandler(VotesController):
    def __init__(self, vote_alchemy_ds: VotesAlchemyDS) -> None:
        self.app_props = MyUtils.loadProperties("general")["app"]
        self.app_state = self.app_props["env"]
        self.logger = logging.getLogger(self.app_props["logger"])
        self.data_source = vote_alchemy_ds
        self.logger.info("using votes alchemy data source")
    
    def get_votes(self) -> List[VoteResponseModel]:
        return self.data_source.get_votes()
    
    def delete_vote(post_id: int) -> VoteResponseModel:
        return super().delete_vote()
    
    def vote(post_id: int) -> List[VoteResponseModel]:
        return super().vote()

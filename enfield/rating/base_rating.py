from enfield import BaseMatch, BasePlayer, BaseTeam, Settings
from pydantic import BaseModel, Field, StrictInt
from typing import Annotated, Union


class BaseRating(BaseModel):
    match_to_rate: Union[BaseMatch, None] = Field(
        validation_alias="match", default=None
    )

    players_to_rate: list[Union[BasePlayer, BaseTeam, None]] = []

    # Data extracts

    old_ratings_to_calculate: list[StrictInt] = []

    def __init__(self) -> None:
        self.players_to_rate = self.retrieve_players()
        self.old_ratings_to_calculate = self.retrieve_old_ratings()

    def retrieve_players(self):
        players_queue = []
        
        if isinstance(self.match_to_rate, BaseMatch):
            players_queue = self.match_to_rate.players
        
        return players_queue

    def retrieve_old_ratings(self):

        rating_queue = []

        for x in self.players_to_rate:
            
            rating : int
            # Checks for type, retrieve appropriate rating
            if isinstance(x, BasePlayer):
                rating = x.player_rating
            if isinstance(x, BaseTeam):
                rating = x.team_rating
            
            # If any other type assign default rating from Settings
            rating = Settings.player_default_rating
            rating_queue.append(rating)
                
        return rating_queue
    
    

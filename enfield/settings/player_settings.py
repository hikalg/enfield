from typing import Annotated
from pydantic import Field, PositiveInt, PositiveFloat, StrictInt, StrictStr
from pydantic.types import StringConstraints
from pydantic_settings import BaseSettings
from .rating_settings import RatingSettings

# change settings here q
PLAYER_DEFAULT_NAME = 'player'
PLAYER_DEFAULT_RATING = 1000
PLAYER_DEFAULT_PERFORMANCE = 1.0
PLAYER_DEFAULT_WINS = 0
PLAYER_DEFAULT_MATCHES = 0

class PlayerSettings(BaseSettings):
    
    player_default_rating: Annotated[
        PositiveInt,
        Field(alias="p_rating_def", default=RatingSettings().default_rating_players),
    ] = PLAYER_DEFAULT_RATING

    player_default_performance: Annotated[
        PositiveFloat, Field(alias="p_performance_def", default=1.0)
    ] = PLAYER_DEFAULT_PERFORMANCE

    player_default_win_count: Annotated[
        int, Field(alias="p_wins_def", default=0)
    ] = PLAYER_DEFAULT_WINS
    
    player_default_match_count : Annotated[
        StrictInt, Field(alias='p_matches_def', default=0, ge=0)
    ] = PLAYER_DEFAULT_MATCHES

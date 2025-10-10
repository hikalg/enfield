from typing import Annotated
from pydantic import Field, PositiveInt, PositiveFloat
from pydantic.types import StringConstraints, Strict
from pydantic_settings import BaseSettings
from .rating_settings import RatingSettings


class PlayerSettings(BaseSettings):
    player_default_name: Annotated[
        str,
        Strict(),
        Field(alias="p_name_def", default="player"),
        StringConstraints(
            min_length=2, max_length=16, strip_whitespace=True, to_lower=True
        ),
    ] = "player"

    player_default_rating: Annotated[
        PositiveInt,
        Field(alias="p_rating_def", default=RatingSettings().default_rating_players),
    ] = 1000

    player_default_performance: Annotated[
        PositiveFloat, Field(alias="p_performance_def", default=1.0)
    ] = 1.0

    player_default_wins: Annotated[
        int, Field(alias="p_wins_def", default=0)
    ] = 0

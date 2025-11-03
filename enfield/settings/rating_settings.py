from typing import Annotated
from pydantic import Field, StrictInt, StrictFloat
from pydantic_settings import BaseSettings

# Minimum and maximum rating thresholds are determined by dividing/multiplying the default rating by the scalar value.
SCALAR = 5


class RatingSettings(BaseSettings):

    default_rating_players: StrictInt = Field(default=1000)

    default_rating_teams: StrictInt = Field(default=1000)

    rating_min_players: StrictInt = Field(default=500)

    rating_max_players: StrictInt = Field(default=5000)

    rating_min_teams: StrictInt = Field(default=500)

    rating_max_teams: StrictFloat = Field(default=5000)

    rating_weighting: StrictInt = Field(default=50)

    rating_scaling_multiplier: StrictFloat = Field(default=1.0)

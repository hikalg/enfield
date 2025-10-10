from typing import Annotated
from pydantic import Field
from pydantic.types import StringConstraints, Strict
from pydantic_settings import BaseSettings


class RatingSettings(BaseSettings):
    rating_minimum_players: Annotated[
        int, Field(alias="min_rating_players", default=500)
    ] = 500

    rating_maximum_players: Annotated[
        int, Field(alias="max_rating_players", default=5000)
    ] = (rating_minimum_players * 10)

    rating_minimum_teams: Annotated[
        int, Field(alias="min_rating_teams", default=500)
    ] = 500

    rating_maximum_teams: Annotated[
        int, Field(alias="max_rating_teams", default=5000)
    ] = (rating_minimum_players * 10)

    default_rating_players: Annotated[
        int, Field(alias="rating_def_players", default=1000)
    ] = 1000

    default_rating_teams: Annotated[
        int, Field(alias="rating_def_players", default=1000)
    ] = 1000

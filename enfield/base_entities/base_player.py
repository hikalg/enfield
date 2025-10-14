from enfield.settings import settings
from .base_entity import BaseEntity
from typing import Annotated
from pydantic import (
    Strict,
    Field,
    PositiveFloat,
    PositiveInt,
    StrictInt,
)
from warnings import warn


class BasePlayer(BaseEntity):
    player_rating: Annotated[
        PositiveInt, Field(alias="p_rating", default=settings.player_default_rating)
    ] = settings.player_default_rating

    player_performance: Annotated[
        PositiveFloat,
        Strict(),
        Field(alias="p_performance", default=settings.player_default_performance),
    ] = settings.player_default_performance

    player_match_count: Annotated[
        PositiveFloat, Strict(), Field(alias="p_matches", default=0)
    ] = settings.player_default_match_count

    player_win_count: Annotated[
        PositiveInt, Strict(), Field(alias="p_wins", default=0)
    ] = settings.player_default_win_count

    def adjust_rating(self, value: StrictInt = 0):
        self.player_rating = self.player_rating + value

    def override_rating(self, value: StrictInt = 0):
        if value == 0:
            warn(f"No value provided for {self.entity_name} - Rating reset to default")
            self.player_rating = settings.player_default_rating

        self.player_rating = value

    def override_match_count(self, value: StrictInt = 0):
        if value == 0:
            warn(f"No value provided for {self.entity_name} - Match count reset")

        self.player_match_count = value

    def override_match_win_count(self, value: StrictInt = 0):
        if value == 0:
            warn(f"No value provided for {self.entity_name} - Win count reset")
        self.player_win_count = value

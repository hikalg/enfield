from enfield.settings import settings
from .base_player import BasePlayer
from .base_entity import BaseEntity
from pydantic import (
    Field,
    PositiveFloat,
    PositiveInt,
    StrictInt,
)
from warnings import warn


class BaseTeam(BaseEntity):
    team_rating: PositiveInt = Field(
        alias="p_rating", default=settings.player_default_rating
    )
    team_performance: PositiveFloat = Field(
        alias="p_performance", default=settings.player_default_performance
    )

    team_match_count: PositiveFloat = Field(alias="p_matches", default=0)

    team_win_count: PositiveInt = Field(alias="p_wins", default=0)

    team_players_list: list[BasePlayer] = Field(alias="playerlist", default=[])

    def adjust_rating(self, value: StrictInt = 0):
        self.player_rating = self.player_rating + value
        
    def add_player(self, player : BasePlayer):
        self.team_players_list.append(player)
        return self.team_players_list

    def override_rating(self, value: StrictInt = 0, ):
        if value == 0:
            warn(f"No value provided for {self.entity_name} - Rating reset to default")
            self.player_rating = settings.player_default_rating

        self.player_rating = value

    def override_match_count(self, value: StrictInt = 0):
        if value == 0:
            warn(f"No value provided for {self.entity_name} - Match count reset")

        self.team_match_count = value

    def override_match_wins(self, value: StrictInt = 0):
        if value == 0:
            warn(f"No value provided for {self.entity_name} - Win count reset")

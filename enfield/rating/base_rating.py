from enfield import BaseMatch, BasePlayer, BaseTeam, EnfieldSettings
from pydantic import StrictInt, StrictFloat
from typing import Annotated, Union, Final
from numpy import median

# HOW THE FUCK DO I CALCULATE RATING? (by hand)
# (my gf tried to make me horny while writing this script)
# (but)

# Step 1a: Retrieve the ratings (duh)
# Step 1b: Find median rating
# Step 2a: Find ratio against median rating
# Step 2b: Find ratio against each other
# Step 2c: Find final ratio


class BaseRating():
    match_to_rate: Union[BaseMatch, None]

    players_to_rate: list[Union[BasePlayer, BaseTeam, None]] = []

    # Data extracts

    old_ratings_to_calculate: list[StrictInt] = []

    rating_median: Union[int, float]
    rating_ratio_to_median: list[Union[int, float]]
    rating_ratio_to_other: list[Union[int, float]]
    scaling_final: list[Union[int, float]]

    def __init__(self, match: BaseMatch) -> None:
        self.match_to_rate = match
        self.players_to_rate = self.retrieve_players()
        self.old_ratings_to_calculate = self.retrieve_old_ratings()
        self.rating_median = self.find_median()
        self.rating_ratio_to_median = self.find_ratio_to_median()
        self.rating_ratio_to_other = self.find_ratio_to_other()
        self.scaling_final = self.find_final_ratio()

    # region Step 1
    # Step 1a
    def retrieve_players(self) -> list:
        return (
            self.match_to_rate.players
            if isinstance(self.match_to_rate, BaseMatch)
            else []
        )

    # Step 1b
    def retrieve_old_ratings(self) -> list:

        rating_queue = []

        for x in self.players_to_rate:
            rating_queue.append(
                x.player_rating
                if isinstance(x, BasePlayer)
                else (
                    x.team_rating
                    if isinstance(x, BaseTeam)
                    else EnfieldSettings.player_default_rating
                )
            )

        return rating_queue

    # endregion
    # region Step 2
    def find_median(self) -> Union[int, float]:
        return (
            float(median(self.old_ratings_to_calculate))
            if self.old_ratings_to_calculate
            else 0
        )

    def find_ratio_to_median(self) -> list:
        ratio_queue = []

        for x in self.old_ratings_to_calculate:
            (
                ratio_queue.append(x / self.rating_median)
                if (x or self.rating_median) != 0
                else 0
            )

        return ratio_queue

    def find_ratio_to_other(self) -> list:
        rating_0 = 0
        rating_1 = 0
        if all(x != 0 for x in self.old_ratings_to_calculate):
            rating_0 = self.old_ratings_to_calculate[0]
            rating_1 = self.old_ratings_to_calculate[1]

        return (
            [rating_0 / rating_1, rating_1 / rating_0]
            if (rating_0 or rating_1) != 0
            else [0, 0]
        )

    def find_final_ratio(self) -> list:
        final_ratio = []
        for x in range(len(self.players_to_rate)):
            final_ratio.append(
                self.rating_ratio_to_median[x] * self.rating_ratio_to_other[x]
            )

        return final_ratio

    # endregion

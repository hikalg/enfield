from enfield import BaseMatch, BasePlayer, BaseTeam, UserSettings
from pydantic import BaseModel, StrictInt, StrictFloat
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
# Step 3: Apply polarity based on winner


class MatchRating():
    match_to_rate: Union[BaseMatch, None]

    players_to_rate: list[Union[BasePlayer, BaseTeam, None]] = []

    winner: Union[BasePlayer, BaseTeam, list[BasePlayer], None]

    # Data extracts

    weighting: int = 50

    def __init__(self, match: BaseMatch) -> None:
        self.match_to_rate = match
        self.winner = self.find_winner()
        self.players_to_rate = self.retrieve_players()
        self.old_ratings_to_calculate = self.retrieve_old_ratings()
        self.rating_median = self.find_median()
        self.rating_ratio_to_median = self.find_ratio_to_median()
        self.rating_ratio_to_other = self.find_ratio_to_other()
        self.scaling_final = self.find_final_ratio()
        self.polarity = self.find_polarity()
        self.rating_change = self.calculate_change()
        self.final_ratings = self.calculate_final_rating()

    def find_winner(self):
        return (
            self.match_to_rate.match_winner if self.match_to_rate is not None else None
        )

    # region Step 1
    # Step 1a
    def retrieve_players(self) -> list:

        if isinstance(self.match_to_rate, BaseMatch):
            return self.match_to_rate.players
        else:
            return []

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
                    else UserSettings.player_default_rating
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
                round(self.rating_ratio_to_median[x] * self.rating_ratio_to_other[x], 2)
            )

        return final_ratio

    def find_polarity(self) -> list:

        winner = (
            0
            if self.winner == self.players_to_rate[0]
            else 1 if self.winner == self.players_to_rate[1] else -1
        )

        match winner:
            case 0:
                return [1, -1]
            case 1:
                return [-1, 1]
            case _:
                return [0, 0]


    def calculate_change(self) -> list:

        changes = []

        for x in range(len(self.players_to_rate)):
            changes.append(
                int(self.polarity[x] * self.scaling_final[x] * self.weighting)
            )

        return changes

    def calculate_final_rating(self) -> list:
        final_ratings = []

        for x in range(len(self.players_to_rate)):
            final_ratings.append(
                self.old_ratings_to_calculate[x] + self.rating_change[x]
            )

        return final_ratings

    # endregion

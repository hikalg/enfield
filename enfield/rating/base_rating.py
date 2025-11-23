from enfield import UserSettings
from pydantic import BaseModel, StrictInt, StrictFloat, Field
from typing import Union
from numpy import median

# TODO:


class BaseRating(BaseModel):
    old_ratings: list[StrictInt] = Field(default=[0, 0])

    winner: StrictInt | StrictFloat = Field()

    weighting: StrictInt = Field(default=UserSettings.rating_weighting)

    scaling: StrictFloat = Field(default=UserSettings.rating_scaling_multiplier)

    def __init__(self, r1 : int, r2 : int, w : int):
        super().__init__(old_ratings=[r1, r2], winner=w)

        self._rating_median = self.find_median()
        self._rating_ratio_to_median = self.find_ratio_to_median()
        self._rating_ratio_to_other = self.find_ratio_to_other()
        self._scaling_final = self.find_final_ratio()
        self._polarity = self.find_polarity()
        self._rating_change = self.calculate_change()
        self._final_ratings = self.calculate_final_rating()

    # region Return functions

    def get_old_ratings(self, slot: int = -1) -> list[int] | int:
        return self.old_ratings[slot] if slot == 1 or 2 else self.old_ratings

    def get_fixed_scaling_values(self) -> float:
        return self.weighting * self.scaling

    def get_median(self) -> float:
        return self._rating_median

    # Get ratio values. If slot is not 0 or 1 return list
    def get_ratio(self, type: str = "", slot: int = -1) -> list[float] | float:
        match type:
            case "median" | "m":
                return (
                    self._rating_ratio_to_median[slot]
                    if slot == 1 or 2
                    else self._rating_ratio_to_median
                )
            case "against" | "a":
                return (
                    self._rating_ratio_to_other[slot]
                    if slot == 1 or 2
                    else self._rating_ratio_to_other
                )
            case _:
                raise ValueError("Invalid ratio type: accepts either median or against")

    def get_polarity(self, slot: int = -1) -> list[int] | int:
        return self._polarity[slot] if slot == (0 or 1) else self._polarity

    def get_rating_change(self, slot: int = -1) -> list[int] | int:
        return self._rating_change[slot] if slot == (0 or 1) else self._rating_change

    def get_final_ratings(self, slot: int = -1):
        return self._final_ratings[slot] if slot == (0 or 1) else self._final_ratings

    # def get_polarity

    # endregion
    # region Step 2
    def find_median(self) -> Union[int, float]:
        return float(median(self.old_ratings)) if self.old_ratings else 0

    def find_ratio_to_median(self) -> list:
        ratio_queue = []

        for x in self.old_ratings:
            (
                ratio_queue.append(x / self._rating_median)
                if (x or self._rating_median) != 0
                else 0
            )

        return ratio_queue

    def find_ratio_to_other(self) -> list:
        rating_0 = 0
        rating_1 = 0
        if all(x != 0 for x in self.old_ratings):
            rating_0 = self.old_ratings[0]
            rating_1 = self.old_ratings[1]

        return (
            [rating_0 / rating_1, rating_1 / rating_0]
            if (rating_0 or rating_1) != 0
            else [0, 0]
        )

    def find_final_ratio(self) -> list:
        final_ratio = []
        for x in range(len(self.old_ratings)):
            final_ratio.append(
                # Combine ratios to median and against selves, then round to the nearest 2 decimal pts
                round(
                    self._rating_ratio_to_median[x] * self._rating_ratio_to_other[x], 2
                )
            )

        return final_ratio

    def find_polarity(self) -> list:
        # TODO: Figure out polarity logic on draws (0.5). Assume: half polarity (0.5), higher rated player receives negative polarity, and vice versa.
        match self.winner:
            case 0:
                return [1, -1]
            case 1:
                return [-1, 1]
            case _:
                return [0, 0]

    def calculate_change(self) -> list:

        changes = []

        for x in range(len(self.old_ratings)):
            # Calculate rating change using the following formula:
            # Polarity (+1/-1) * Default Scaling * Ratio Scaling * Weighting
            changes.append(
                int(self._polarity[x] * self._scaling_final[x] * self.weighting)
            )

        return changes

    def calculate_final_rating(self, override_limit: bool = False) -> list:
        final_ratings = []

        for x in range(len(self.old_ratings)):
            final_rating = self.old_ratings[x] + self._rating_change[x]

        # Apply constraints to calculation results. If override is set to True raw values are returned
        
            if final_rating > UserSettings.rating_max_players:
                final_rating = (
                    UserSettings.rating_max_players if not override_limit else final_rating
                )

            if final_rating < UserSettings.rating_min_players:
                final_rating = (
                    UserSettings.rating_min_players if not override_limit else final_rating
                )

            final_ratings.append(final_rating)

        return final_ratings

    # endregion

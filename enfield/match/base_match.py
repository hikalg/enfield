from enfield.base_entities import BasePlayer, BaseTeam
from typing import Annotated
from pydantic import BaseModel, Field, StrictInt, StrictBool, StrictStr

# Suggestion for self:
# - Make player numbering 0/1 instead of natural number 1/2?
# - Find a way to effectively store players (dict, NamedTuple)


class BaseMatch(BaseModel):
    # region Variables

    # player_1: Annotated[
    #     BasePlayer | BaseTeam | list[BasePlayer] | None,
    #     Field(alias="p1", default=None),
    # ] = None

    # player_2: Annotated[
    #     BasePlayer | BaseTeam | list[BasePlayer] | None,#region Variables
    #     Field(alias="p2", default=None),
    # ] = None

    players: Annotated[
        list[BasePlayer | BaseTeam | list[BasePlayer] | None],
        Field(alias="players", default=[None, None]),
    ] = [None, None]

    match_score: Annotated[
        list[StrictInt],
        Field(
            alias="scores",
            default=[0, 0],
        ),
    ] = [0, 0]

    match_winner: Annotated[
        BasePlayer | BaseTeam | list[BasePlayer] | None,
        Field(alias="winner", default=None),
    ] = None

    match_draw: Annotated[
        StrictBool,
        Field(
            title="match_draw",
            description="Determine if match is tied",
            alias="draw",
            default=False,
        ),
    ] = False

    match_complete: Annotated[
        StrictBool,
        Field(
            title="match_complete",
            description="Match completion status",
            alias="done",
            default=False,
        ),
    ] = False
    # endregion

    def end_match(self, dont_assign_winner: bool = False):
        # Ends the match and assign winner
        # If dont_assign_winner is true, match_winner remains at None
        if not dont_assign_winner:
            # Comparison logic
            if self.match_score[0] > self.match_score[1]:
                self.match_winner = self.players[0]

            elif self.match_score[0] < self.match_score[1]:
                self.match_winner = self.players[1]

            elif self.match_score[0] == self.match_score[1]:
                self.match_winner = None
                self.match_draw = True

            else:
                self.match_winner = None
        # Flags match as complete
        self.match_complete = True
        return self.match_winner, self.match_complete

    # region Scoring
    def score(
        self, score_p1: StrictInt = 0, score_p2: StrictInt = 0
    ) -> list[StrictInt]:
        # No arguments call resets scores to zeroes
        self.match_score = [score_p1, score_p2]
        return self.match_score

    def score_player(
        self, player_slot: StrictInt = -1, score: StrictInt = 0
    ) -> StrictInt:
        if self._validate_player_slot(player_slot):
            self.match_score[player_slot] = score

        else:
            print("Operation unsucessful")

        return self.match_score[player_slot]

    # endregion

    # region Player management
    def change_player(self, player_slot: StrictInt, player):
        if self._validate_player_slot(player_slot):
            self.players[player_slot] = player
            print("Operation successful")

        else:
            print("Operation unsucessful")

        return self.players[player_slot]

    def remove_player(self, player_slot: StrictInt, player):
        if self._validate_player_slot(player_slot):
            self.players[player_slot - 1] = None

        else:
            print("Operatio unsucessful")

        return self.players[player_slot - 1]

    # Add players to unfilled/partially filled matches only
    def add_player(self, player):
        pass
        # endregion

        # region Internal validation checks

    def _validate_player_slot(self, slot_value: StrictInt) -> StrictBool:
        if not (slot_value == (1 or 2)):
            print("Not in range")
            return False

        return True

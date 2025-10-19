from enfield import BasePlayer, BaseTeam
from typing import Annotated, Union
from pydantic import BaseModel, Field, StrictInt, StrictBool

# Suggestion for self:
# - Make player numbering 0/1 instead of natural number 1/2?
# - Find a way to effectively store players (dict, NamedTuple)


class BaseMatch(BaseModel):
    # region Variables

    players: list[Union[BasePlayer, BaseTeam, list[BasePlayer], None]] = Field(
        default=[]
    )

    match_score: list[StrictInt] = Field(validation_alias="scores", default=[0, 0])

    match_winner: Union[BasePlayer, BaseTeam, list[BasePlayer], None] = Field(
        alias="winner", default=None
    )

    match_draw: Annotated[
        StrictBool,
        Field(
            title="match_draw",
            description="Determine if match is tied",
        ),
    ] = False

    match_complete: Annotated[
        StrictBool,
        Field(
            title="match_complete",
            description="Match completion status",
        ),
    ] = False
    # endregion

    # Ends the match and assign winner
    def end_match(
        self,
        dont_assign_winner: StrictBool = Field(default=False),
        dont_assign_draw: StrictBool = Field(default=False),
        dont_assign_complete: StrictBool = Field(default=False),
    ):
        # Comparison logic
        one_wins_two: StrictBool = self.match_score[0] > self.match_score[1]
        draw: StrictBool = one_wins_two and (self.match_score[0] == self.match_score[1])

        # If dont_assign_winner is true, match_winner remains at None
        if not dont_assign_winner:
            # Comparison logic
            match one_wins_two:
                case True:
                    self.match_winner = self.players[0]
                case False:
                    if draw:
                        self.match_winner = None
                        if not dont_assign_draw:
                            self.match_draw = True
                    else:
                        self.match_winner = self.players[1]

        # Flags match as complete
        if not dont_assign_complete:
            self.match_complete = True
        return self.match_winner

    # region Scoring
    def score(
        self,
        score_p1: StrictInt = Field(default=0),
        score_p2: StrictInt = Field(default=0),
    ) -> list[StrictInt]:
        # No arguments call resets scores to zeroes
        self.match_score = [score_p1, score_p2]
        return self.match_score

    def score_player(
        self,
        player_slot: StrictInt = Field(default=-1),
        score: StrictInt = Field(default=0),
    ) -> StrictInt:
        if self._validate_player_slot(player_slot):
            self.match_score[player_slot] = score

        else:
            print("Operation unsucessful")

        return self.match_score[player_slot]

    # endregion

    # region Player management
    def change_player(
        self,
        player_slot: StrictInt = Field(default=-1),
        player: Union[BasePlayer, BaseTeam, list[BasePlayer], None] = Field(
            default=None
        ),
    ):
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

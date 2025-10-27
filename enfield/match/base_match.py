from enfield import BasePlayer, BaseTeam
from enfield.messages import GenericSuccess, GenericError
from typing import Annotated, Union
from datetime import datetime
from pydantic import BaseModel, Field, StrictInt, StrictBool

# Suggestion for self:
# - Make player numbering 0/1 instead of natural number 1/2?
# - Find a way to effectively store players (dict, NamedTuple)


class BaseMatch(BaseModel):
    # region Variables

    players: list[Union[BasePlayer, BaseTeam, None]] = Field(
        default=[]
    )

    match_score: list[StrictInt] = Field(alias="scores", default=[0, 0])

    match_winner: Union[BasePlayer, BaseTeam, list[BasePlayer], None] = Field(
        alias="winner", default=None
    )
    
    match_datetime: datetime = Field(validation_alias='datetime', default=datetime(2025, 11, 25))

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
        dont_assign_winner: StrictBool = False,
        dont_assign_draw: StrictBool = False,
        dont_assign_complete: StrictBool = False,
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
        p1: int = 0,
        p2: int = 0,
        override: StrictBool = False
    ) -> list[StrictInt]:
        score_cache = self.match_score
        
        # Override switch off: Do not write scores if args are 0
        if not override:
            score_cache[0] = p1 if not p1 == 0 else score_cache[0]
            score_cache[1] = p2 if not p2 == 0 else score_cache[1]

        # Override switch on: Write anyway
        if override:
            score_cache[0] = p1
            score_cache[1] = p2

        self.match_score = score_cache
        return self.match_score

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
            GenericSuccess()

        else:
            GenericError()

        return self.players[player_slot]

    def remove_player(self, player_slot: StrictInt, player):
        if self._validate_player_slot(player_slot):
            self.players[player_slot - 1] = None

        else:
            GenericError()

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

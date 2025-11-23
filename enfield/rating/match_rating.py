from enfield import BasePlayer, BaseTeam, BaseMatch, UserSettings
from .base_rating import BaseRating
from pydantic import Field

# TODO #1: New method? apply_new_rating
# TODO #2: Fix this shit?

class MatchRating():
    
    base_match : BaseMatch | None = None
    base_rating : BaseRating | None
    
    def __init__(self, base_match : BaseMatch | None = None):
        self.base_match = base_match
        self._entities = self._retrieve_entities()
        self._ratings = self._retrieve_old_ratings()
        self._match_winner = self._find_winner_index()

        # super().__init__(self._ratings[0], self._ratings[1], self._match_winner)
        # MatchRating.__init__(self, base_match=base_match)

    def _retrieve_entities(self) -> list:
        if isinstance(self.base_match, BaseMatch):
            return self.base_match.players
        else:
            return []

    def _find_winner_index(self) -> int:
        if isinstance(self.base_match, BaseMatch): 
            return self.base_match.players.index(self.base_match.match_winner)
        else:
            return -1

    def _retrieve_old_ratings(self) -> list:

        rating_queue: list = []
        for entity in self._entities:
            if isinstance(entity, BasePlayer):
                rating_queue.append(entity.player_rating)
            elif isinstance(entity, BaseTeam):
                rating_queue.append(entity.team_rating)
            else:
                rating_queue.append(UserSettings.player_default_rating)

        return rating_queue

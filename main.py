from enfield.base_entities import BasePlayer
from enfield.base_entities.base_entity import BaseEntity
from enfield.match.base_match import BaseMatch
from enfield.messages import GenericError

player1 = BasePlayer(name="thinkpad")
# player2 = BasePlayer(entity_name="framework")

# player.override_rating()

# print(player.player_rating)

# match = BaseMatch(players=[player1, player2])

# print(match.model_dump())

print(player1.entity_name)
# print(match.model_dump)
# print(GenericError())
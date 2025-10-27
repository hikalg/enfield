from enfield.base_entities import BasePlayer
from enfield.base_entities.base_entity import BaseEntity
from enfield.match.base_match import BaseMatch
from enfield.messages import GenericError

# from enfield 

player1 = BasePlayer(name="thinkpad")
player2 = BasePlayer(name="framework")

match1 = BaseMatch(players=[player1, player2], scores=[2, 1])

# print(match1.match_score)
# match1.score(p1=2, p2=4)
match1.score(p2=6, override=True)
# print(match1.score(p1=8, reset=False))

# print(match1.score(reset=True))

# match1.end_match()
# print(match1.match_winner)

# player2 = BasePlayer(entity_name="framework")

# player.override_rating()

# print(player.player_rating)

# match = BaseMatch(players=[player1, player2])

# print(match.model_dump())

# print(player1.entity_name)
# print(player2.entity_name)

# print(match.model_dump)
# print(GenericError())
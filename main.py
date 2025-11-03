from enfield import BasePlayer, BaseTeam, BaseRating, UserSettings, BaseMatch

# from enfield 

player1 = BasePlayer(name="thinkpad", player_rating=2000)
player2 = BasePlayer(name="framework", player_rating=1600)
match1 = BaseMatch(players=[player1, player2], scores=[1, 2])
match1.end_match()

# rating1 = BaseRating(match1)

rating1 = BaseRating(1500, 1700, 0)

print(rating1._final_ratings)
print(rating1.get_final_ratings())

# print(match1.match_score)
# match1.score(p1=2, p2=4)
# match1.score(p2=6, override=True)
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
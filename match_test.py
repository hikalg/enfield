from enfield import BasePlayer, BaseMatch

# region Setup
# initialises matches
match1 = BaseMatch(players=[BasePlayer(), BasePlayer()])
match2 = BaseMatch(players=[BasePlayer(), BasePlayer()], scores=[1, 2])

match1.score(p1=1, p2=2)
match2.score(p1=6, p2=6)

assert match1.match_score == [1, 2]
assert match2.match_score == [6, 6]
from enfield import BaseRating, Result

# rating1 = BaseRating(1000, 1200, Result.P1)
# rating2 = BaseRating(1200, 1000, Result.P1)
# rating3 = BaseRating(1000, 1000, Result.P1)
# rating4 = BaseRating(2100, 1200, Result.P1)

# print(rating1)
# print(rating2)
# print(rating3)
# print(rating4)

set_list = [
    BaseRating(1000, 1200, Result.P1), # Normal rating diff P2
    BaseRating(1200, 1000, Result.P1), # Normal rating diff P1
    BaseRating(1000, 1050, Result.P1), # Close distance P2
    BaseRating(1050, 1000, Result.P1), # Close distance P1
    BaseRating(1000, 1000, Result.P1), # Same rating
    BaseRating(2100, 1200, Result.P1), # Far distance P1
    BaseRating(1200, 2100, Result.P1), # Far distance P2
    BaseRating(4500, 1000, Result.P1), #  SUPER Far distance P2
    BaseRating(1000, 4500, Result.P1), #  SUPER Far distance P2
]

for x in set_list: print(x)

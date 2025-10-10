from .meta_settings import MetaSettings
from .player_settings import PlayerSettings
from .rating_settings import RatingSettings

# the big meeg
class Settings(MetaSettings, PlayerSettings, RatingSettings):
    pass
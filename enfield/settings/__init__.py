from .meta_settings import MetaSettings
from .player_settings import PlayerSettings
from .rating_settings import RatingSettings
from .entity_settings import EntitySettings

# the big meeg
class Settings(MetaSettings, PlayerSettings, RatingSettings, EntitySettings):
    pass

settings = Settings() # initialises default settings
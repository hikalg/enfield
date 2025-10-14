from .meta_settings import MetaSettings
from .player_settings import PlayerSettings
from .rating_settings import RatingSettings
from .entity_settings import EntitySettings
from pydantic_extra_types.timezone_name import TimeZoneName
from pydantic_extra_types.country import CountryAlpha2


# the big meeg
class Settings(MetaSettings, PlayerSettings, RatingSettings, EntitySettings):
    pass


settings = Settings(
    # # --------------
    # # Meta Settings
    # meta_name="enfield",
    # meta_disciplines=[],
    # # --------------
    # # Entity Settings
    # entity_default_name="player",
    # entity_default_country=CountryAlpha2("AU"),
)

from typing import Annotated
from pydantic import Field, Strict
from pydantic.types import StringConstraints
from pydantic_extra_types.country import CountryAlpha2
from pydantic_extra_types.timezone_name import TimeZoneName
from pydantic_settings import BaseSettings


# settings constants
ENTITY_DEFAULT_NAME : str = "player"

ENTITY_DEFAULT_DESCRIPTION : str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In at semper arcu. Phasellus a laoreet turpis."

ENTITY_DEFAULT_COUNTRY : CountryAlpha2 = "AU" # type: ignore

ENTITY_DEFAULT_TIMEZONE : TimeZoneName = "Australia/Sydney" # type: ignore

class EntitySettings(BaseSettings):
    entity_default_name: Annotated[
        str,
        Strict(),
        Field(alias="p_name_def", default="player"),
        StringConstraints(
            min_length=2, max_length=16, strip_whitespace=True, to_lower=True
        ),
    ] = ENTITY_DEFAULT_NAME

    entity_default_description: Annotated[
        str,
        Strict(),
        Field(alias="e_desc_def", default=""),
        StringConstraints(max_length=2048),
    ] = ENTITY_DEFAULT_DESCRIPTION

    entity_default_country: Annotated[
        CountryAlpha2, Field(alias="e_country_def", default="AU")
    ] = ENTITY_DEFAULT_COUNTRY

    entity_default_timezone: Annotated[
        TimeZoneName, Field(alias="e_timezone_default", default="Australia/Sydney")
    ] = ENTITY_DEFAULT_TIMEZONE



from typing import Annotated
from pydantic import Field, Strict
from pydantic.types import StringConstraints
from pydantic_extra_types.country import CountryAlpha2
from pydantic_extra_types.timezone_name import TimeZoneName
from pydantic_settings import BaseSettings


# Default settings constants - used as fallback
NAME: str = "player"

DESCRIPTION: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In at semper arcu. Phasellus a laoreet turpis."

COUNTRY: CountryAlpha2 = "AU"  # type: ignore

TIMEZONE: TimeZoneName = "Australia/Sydney"  # type: ignore


class EntitySettings(BaseSettings):
    entity_default_name: Annotated[
        str,
        Strict(),
        StringConstraints(
            min_length=2, max_length=16, strip_whitespace=True, to_lower=True
        ),
    ] = Field(title="Entity Name (Default)", default=NAME)

    entity_default_description: Annotated[
        str,
        Strict(),
        StringConstraints(max_length=2048),
    ] = Field(title="Entity Descripition (Default)", default=DESCRIPTION)

    entity_default_country: CountryAlpha2 = Field(
        title="Entity Country (Default)", default=COUNTRY
    )

    entity_default_timezone: TimeZoneName = Field(
        title="Entity Timezone (Default)", default=TIMEZONE
    )

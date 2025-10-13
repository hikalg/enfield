from enfield.settings import settings
from typing import Annotated
from pydantic import BaseModel, Field, Strict
from pydantic.types import StringConstraints
from pydantic_extra_types.country import CountryAlpha2
from pydantic_extra_types.timezone_name import TimeZoneName

# settings = Settings()


class BaseEntity(BaseModel):
    entity_name: Annotated[
        str,
        Strict(),
        Field(alias="e_name", default=settings.entity_default_name),
        StringConstraints(
            min_length=2, max_length=16, strip_whitespace=True, to_lower=True
        ),
    ] = settings.entity_default_name

    entity_description: Annotated[
        str,
        Strict(),
        Field(alias="e_desc", default=settings.entity_default_description),
        StringConstraints(max_length=2048),
    ] = settings.entity_default_description

    entity_country: Annotated[
        CountryAlpha2, Field(alias="e_country_def", default="AU")
    ] = settings.entity_default_country

    entity_timezone: Annotated[
        TimeZoneName, Field(alias="e_tz", default=settings.entity_default_timezone)
    ] = settings.entity_default_timezone

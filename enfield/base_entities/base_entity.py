from enfield.settings import Settings
from typing import Annotated
from pydantic import BaseModel, Field, Strict
from pydantic.types import StringConstraints
from pydantic_extra_types.country import CountryAlpha2
from pydantic_extra_types.timezone_name import TimeZoneName

settings = Settings()


class BaseEntity(BaseModel):
    entity_name: Annotated[
        str,
        Strict(),
        StringConstraints(
            min_length=0, max_length=16, to_lower=True
        ),
    ] = Field(alias="name", default=settings.entity_default_name)

    entity_description: Annotated[
        str,
        Strict(),
        StringConstraints(max_length=2048),
    ] = Field(alias="desc", default=settings.entity_default_description)

    entity_country: CountryAlpha2 = Field(
        alias="country", default=settings.entity_default_country
    )

    entity_timezone: TimeZoneName = Field(
        alias="e_tz", default=settings.entity_default_timezone
    )

    # def __init__ (self, name):
    #     self.entity_name = name

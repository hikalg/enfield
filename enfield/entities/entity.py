from enfield.settings import Settings
from typing import Annotated
from pydantic import (
    BaseModel,
    Field,
    Strict
)
from pydantic.types import StringConstraints
from pydantic_extra_types.country import CountryAlpha2
from pydantic_extra_types.timezone_name import TimeZoneName

class Entity(BaseModel):
    entity_name: Annotated[
        str,
        Strict(),
        Field(alias="e_name", default=Settings().entity_default_name),
        StringConstraints(
            min_length=2, max_length=16, strip_whitespace=True, to_lower=True
        )
    ] = Settings().entity_default_name

    entity_description: Annotated[
        str,
        Strict(),
        Field(alias="e_desc", default=Settings().entity_default_description),
        StringConstraints(max_length=2048)
    ] = Settings().entity_default_description
    
    entity_country: Annotated[
        CountryAlpha2, Field(alias="e_country_def", default="AU")
    ] = Settings().entity_default_country
    
    def rename(self, name : str = "") -> None:
        if not name:
            print("Name not provided")
        
        self.entity_name = name
        
    def recountry(self, country : str = "") -> None:
        self.entity_country = CountryAlpha2(country)

test = Entity()

test.recountry("US")
        

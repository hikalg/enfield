from typing import Annotated
from pydantic import Field
from pydantic.types import StringConstraints
from pydantic_settings import BaseSettings

# These settings are metadata of


class MetaSettings(BaseSettings):
    meta_name: Annotated[
        str,
        Field(alias="metaname", default="enfield"),
        StringConstraints(
            min_length=4, max_length=64, strip_whitespace=True, to_lower=True
        ),
    ] = "enfield"

    meta_discipline: Annotated[
        str,
        Field(alias="discipline", default="discipline"),
        StringConstraints(strip_whitespace=True),
    ] = "enfield"

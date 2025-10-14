from typing import Annotated
from pydantic import Field, StrictStr
from pydantic.types import StringConstraints
from pydantic_settings import BaseSettings

# These settings are metadata of


class MetaSettings(BaseSettings):
    meta_name: Annotated[
        StrictStr,
        StringConstraints(
            min_length=4, max_length=64, strip_whitespace=True, to_lower=True
        ),
    ] = Field(default="enfield")

    meta_disciplines: list[StrictStr] = Field(default=["chess", "checkers", "monopoly"])

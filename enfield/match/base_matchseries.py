from enfield import BasePlayer, BaseTeam, BaseMatch
from enfield.messages import GenericSuccess, GenericError
from pydantic import BaseModel, Field, StrictInt, StrictBool
from typing import Annotated

class BaseMatchSeries():
    matches : list[BaseMatch] = Field(default=[])

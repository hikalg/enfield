# Enfield

A player management and skill rating library written in Python.

Designed for competitive physical and electronic sports disciplines.

> [!NOTE]  
> Planned features will be implemented in the near future. (Can't tell you when)

> [!CAUTION]
> Features might not work as expected.

## Features

* Entity (players, teams) management with easy to integrate models and detailed metadata (including timezones and languages)

* Match management with support for match collections

* Automatic rating calculation using a custom algorithm

* Data validation with Pydantic

* Configurable settings for every component

## Requirements
* Python version `3.13` or greater

* [uv](https://github.com/astral-sh/uv) dependency manager

**The following is managed by `uv`:**

* [Pydantic](https://github.com/pydantic/pydantic)

* [Pydantic Settings](https://github.com/pydantic/pydantic-settings)

* [Pydantic Extra Types](https://github.com/pydantic/pydantic)

* [Typing Extensions](https://github.com/python/typing_extensions)

* [Pycountry](https://github.com/pycountry/pycountry)

* [Tzdata](https://github.com/python/tzdata)

## Usage
* Import Enfield in your project:

```py
# Import everything?cl
import enfield
# Or just some bits?
from enfield import BasePlayer, Match
```

* Create your first player:
```
player = BasePlayer()
```

## License
MIT License.


from typing import Annotated, Literal, Sequence

import annotated_types
from pydantic import Field

from .values_map import AnyValue, AnyValuesMap, One, ValuesMap, NonEmptyStr
from enum import StrEnum


class AttributeKind(StrEnum):
    LOCATION = "LOCATION"
    AREA = "AREA"
    MAX_POWER_CONSUMPTION = "MAX_POWER_CONSUMPTION"
    MAX_POWER_EXPORT = "MAX_POWER_EXPORT"
    DESCRIPTION = "DESCRIPTION"


Location = ValuesMap[
    Literal[AttributeKind.LOCATION],
    tuple[float, float],
]
"""
> Describes a single geographic point. Values[] contains 2 floats, generally
> representing longitude and latitude. Demand Response programs may define
> their own use of these fields.
"""

Area = ValuesMap[
    Literal[AttributeKind.AREA],
    Annotated[Sequence[AnyValue], annotated_types.Len(min_length=1)],
]
"""
> Describes a geographic area. Values[] contains application specific data.
> Demand Response programs may define their own use of these fields, such
> as GeoJSON polygon data.
"""
MaxPowerConsumption = ValuesMap[
    Literal[AttributeKind.MAX_POWER_CONSUMPTION], One[float]
]
"""
> Values contains a floating point number describing the maximum
> consumption, in kiloWatts.
"""
MaxPowerExport = ValuesMap[Literal[AttributeKind.MAX_POWER_EXPORT], One[float]]
"""
> Values contains a floating point number describing the maximum power the
> device can export, in kiloWatts.
"""
Description = ValuesMap[Literal[AttributeKind.DESCRIPTION], One[NonEmptyStr]]
"""
> Free-form text tersely describing a ven or resource.
"""

Attribute = (
    Annotated[
        Location | Area | MaxPowerConsumption | MaxPowerExport | Description,
        Field(discriminator="type"),
    ]
    | AnyValuesMap
)

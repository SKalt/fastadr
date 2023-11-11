from enum import StrEnum
from typing import Annotated, Literal

from pydantic import Field

from .values_map import AnyValue, AnyValuesMap, AtLeastOne, NonEmptyStr, One, ValuesMap


class TargetKind(StrEnum):
    POWER_SERVICE_LOCATION = "POWER_SERVICE_LOCATION"
    SERVICE_AREA = "SERVICE_AREA"
    GROUP = "GROUP"
    RESOURCE_NAME = "RESOURCE_NAME"
    VEN_NAME = "VEN_NAME"
    EVENT_NAME = "EVENT_NAME"
    PROGRAM_NAME = "PROGRAM_NAME"


PowerServiceLocation = ValuesMap[
    Literal[TargetKind.POWER_SERVICE_LOCATION],
    AtLeastOne[AnyValue],  # <-- TODO: narrow
]
"""
> A Power Service Location is a utility named specific location in geography or
> the distribution system, usually the point of service to a customer site
"""

ServiceArea = ValuesMap[Literal[TargetKind.SERVICE_AREA], One[NonEmptyStr]]  # Q: arity?
"""
> A Service Area is a utility named geographic region. Target values array
> contains a string representing a service area name
"""

Group = ValuesMap[Literal[TargetKind.GROUP], One[NonEmptyStr]]
"""
> Target values array contains a string representing a group
"""

ResourceName = ValuesMap[Literal[TargetKind.RESOURCE_NAME], One[NonEmptyStr]]
"""
> Target values array contains a string representing a resource name
"""
VenName = ValuesMap[Literal[TargetKind.VEN_NAME], One[NonEmptyStr]]
"""
> Target values array contains a string representing a VEN name
"""
EventName = ValuesMap[Literal[TargetKind.EVENT_NAME], One[NonEmptyStr]]
"""
> Target values array contains a string representing an event name
"""
ProgramName = ValuesMap[Literal[TargetKind.PROGRAM_NAME], One[NonEmptyStr]]
"""
> Target values array contains a string representing a program name
"""

Target = (
    Annotated[
        PowerServiceLocation
        | ServiceArea
        | Group
        | ResourceName
        | VenName
        | EventName
        | ProgramName,
        Field(discriminator="type"),
    ]
    | AnyValuesMap
)

from typing import Annotated, Generic, Sequence, TypeVar
import annotated_types

from pydantic import BaseModel
from .scalar import ShortStr


class Point(BaseModel):  # <-- only ever found inside ValuesMap
    """
    A pair of floats typically used as a point on a 2 dimensional grid.
    """

    x: float | None = None
    """A value on an x axis."""
    y: float | None = None
    """A value on a y axis."""


Type = TypeVar("Type", bound=ShortStr, covariant=True)
AnyValue = int | float | str | bool | Point
Values = TypeVar("Values", bound=Sequence[AnyValue], covariant=True)
Value = TypeVar("Value", bound=AnyValue)
MaybeOne = Annotated[Sequence[Value], annotated_types.Len(min_length=0, max_length=1)]
One = Annotated[Sequence[Value], annotated_types.Len(min_length=1, max_length=1)]
AtLeastOne = Annotated[Sequence[Value], annotated_types.Len(min_length=1)]
NonEmptyStr = Annotated[str, annotated_types.Len(1, 1024 * 1024)]
"""A non-empty string of at most 1MB of UTF-8 encoded text."""


# TODO: make generic over length, too.
class ValuesMap(BaseModel, Generic[Type, Values]):
    """
    Represents one or more values associated with a type.
    E.g. a type of PRICE contains a single float value.
    """

    type: Type
    """
    Enumerated or private string signifying the nature of values.
    E.G. "PRICE" indicates value is to be interpreted as a currency.
    """

    values: Values
    """
    The value associated with the type.
    """


AnyValuesMap = ValuesMap[str, Sequence[AnyValue]]

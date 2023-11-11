from typing import Generic, TypeVar

from pydantic import BaseModel


class Point(BaseModel):
    """
    A pair of floats typically used as a point on a 2 dimensional grid.
    """

    x: float | None = None
    """A value on an x axis."""
    y: float | None = None
    """A value on a y axis."""


Type = TypeVar("Type", bound=str)
AnyValue = int | float | str | bool | Point
Value = TypeVar("Value", bound=AnyValue)


# TODO: make generic over length, too.
class ValuesMap(BaseModel, Generic[Type, Value]):
    """
    Represents one or more values associated with a type.
    E.g. a type of PRICE contains a single float value.
    """

    type: Type
    """
    Enumerated or private string signifying the nature of values.
    E.G. "PRICE" indicates value is to be interpreted as a currency.
    """
    values: list[Value]
    """
    The value associated with the type.
    """


AnyValuesMap = ValuesMap[str, AnyValue]

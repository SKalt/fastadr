from datetime import datetime, timedelta
from typing import Annotated

import annotated_types
from pydantic import Strict, StringConstraints


ShortStr = Annotated[str, StringConstraints(min_length=1, max_length=128), Strict()]
Duration = Annotated[timedelta, str, Strict()]
"""duration in ISO 8601 format"""

DateTime = Annotated[datetime, str, Strict()]
"""datetime in ISO 8601 format"""

HTTPStatusCode = Annotated[int, annotated_types.Ge(100), annotated_types.Lt(600)]

ObjectID = Annotated[
    str, StringConstraints(pattern="^[a-zA-Z0-9_-]*$", min_length=1, max_length=128)
]
"""URL safe VTN assigned object ID."""

Percent = Annotated[int, annotated_types.Ge(0), annotated_types.Le(100), Strict()]

Int32 = Annotated[int, annotated_types.Ge(-2147483648), annotated_types.Le(2147483647)]

# from datetime import timedelta
# Duration = Annotated[timedelta]
# """duration in ISO 8601 format""" # e.g. PT1H
from datetime import datetime, timedelta
from enum import Enum, StrEnum
from typing import Annotated, Any, Generic, Literal, Optional, Sequence, TypeVar, Union

import annotated_types
from pydantic import (
    BaseModel,
    Field,
    PositiveInt,
    StrictFloat,
    StringConstraints,
    Strict,
)
from pydantic_core import Url
from .values_map import AnyValuesMap
from .event_types import EventValues
from .report_types import ReportValues
from .resource_types import Attribute  # FIXME: circular import
from .target_types import Target


class OAuthScopes(StrEnum):
    # See page 10, section 7, "EndPoints" in file://./../spec/2_OpenADR%203.0%20Definition%20v3.0.0.pdf
    read_all = "read_all"
    """VENs and BL can read all resources"""
    write_programs = "write_programs"
    """Only BL can write to programs"""
    write_events = "write_events"
    """Only BL can write to events"""
    write_reports = "write_reports"
    """only VENs can write to reports"""
    write_subscriptions = "write_subscriptions"
    """VENs and BL can write to subscriptions"""
    write_vens = "write_vens"
    """VENS and BL can write to vens and resources"""


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


class Problem(BaseModel):
    """reusable error response. From https://opensource.zalando.com/problem/schema.yaml."""

    type: Url = Url("about:blank")  # really a URI
    """
    An absolute URI that identifies the problem type.
    When dereferenced, it SHOULD provide human-readable documentation for the problem type
    (e.g., using HTML).
    """

    title: str
    """
    A short, summary of the problem type. Written in english and readable
    for engineers (usually not suited for non technical stakeholders and
    not localized); example: Service Unavailable.
    """

    status: HTTPStatusCode
    """
    The HTTP status code generated by the origin server for this occurrence
    of the problem.
    """

    detail: str
    """
    A human readable explanation specific to this occurrence of the
    problem.
    """

    instance: Url
    """
    An absolute URI that identifies the specific occurrence of the problem.
    It may or may not yield further information if dereferenced.
    """


class IntervalPeriod(BaseModel):
    """
    Defines temporal aspects of intervals.
    A duration of default null indicates infinity.
    A randomizeStart of default null indicates no randomization.
    """

    start: Optional[DateTime]
    """The start time of an interval or set of intervals."""
    duration: Optional[Duration] = None
    """The duration of an interval or set of intervals."""
    randomizeStart: Optional[Duration] = None
    """a randomization time that may be applied to start."""


Values = TypeVar("Values", bound=AnyValuesMap, contravariant=True)


class Interval(BaseModel, Generic[Values]):
    """
    An object defining a temporal window and a list of valuesMaps.
    if intervalPeriod present may set temporal aspects of interval or override event.intervalPeriod.
    """

    id: Int32
    """
    A client generated number assigned an interval object. Not a sequence number.
    """

    intervalPeriod: IntervalPeriod = Field(
        default_factory=lambda: IntervalPeriod(start=None)
    )
    """Defines default start and durations of intervals."""
    # TODO: clarify default value for omissible non-null intervalPeriod

    payloads: Sequence[Values]
    """A list of valuesMap objects."""


class ReportResource(BaseModel):
    """Report data associated with a resource."""

    resourceName: Optional[ShortStr] = None
    """
    User generated identifier. A value of AGGREGATED_REPORT indicates an aggregation of more that one resource's data
    """
    intervalPeriod: Optional[IntervalPeriod] = None
    intervals: Sequence[Interval[Any]]  # FIXME: what kind of values are allowed here?
    """A list of interval objects."""


class ObjectTypes(Enum):
    PROGRAM = "PROGRAM"
    EVENT = "EVENT"
    REPORT = "REPORT"
    SUBSCRIPTION = "SUBSCRIPTION"
    VEN = "VEN"
    RESOURCE = "RESOURCE"
    EVENT_PAYLOAD_DESCRIPTOR = "EVENT_PAYLOAD_DESCRIPTOR"


class ReportDescriptor(BaseModel):
    """
    An object that may be used to request a report from a VEN.
    See OpenADR REST User Guide for detailed description of how configure a report request.
    """

    payloadType: ShortStr
    """
    Enumerated or private string signifying the nature of values.
    """
    readingType: Optional[str] = None
    """
    Enumerated or private string signifying the type of reading.
    """
    targets: Sequence[ReportValues] | None = None  # Q: what's the inner kind?
    """A list of valuesMap objects."""
    aggregate: bool = False
    """
    True if report should aggregate results from all targeted resources.
    False if report includes results for each resource.
    """
    startInterval: Int32 = -1
    """
    The interval on which to generate a report.
    -1 indicates generate report at end of last interval.
    """
    numIntervals: Int32 = -1
    """
    The number of intervals to include in a report.
    -1 indicates that all intervals are to be included.
    """
    historical: bool = True
    """
    True indicates report on intervals preceding startInterval.
    False indicates report on intervals following startInterval (e.g. forecast).
    """
    frequency: Int32 = -1
    """
    Number of intervals that elapse between reports.
    -1 indicates same as numIntervals.
    """
    repeat: Int32 = 1
    """
    Number of times to repeat report.
    1 indicates generate one report.
    -1 indicates repeat indefinitely.
    """


# TODO: make generic over what kind of `valuesMaps` are allowed?
class Resource(BaseModel):
    """
    A resource is an energy device or system subject to control by a VEN.
    """

    id: ObjectID = ""  # FIXME: sensible default
    createdDateTime: Optional[DateTime] = None
    modificationDateTime: Optional[DateTime] = None
    objectType: Literal["RESOURCE"]
    """Used as discriminator, e.g. notification.object"""
    resourceName: Optional[ShortStr] = None
    """
    User generated identifier, resource may be configured with identifier out-of-band.
    """
    venID: ObjectID = ""  # FIXME: sensible default
    attributes: Sequence[Attribute] = Field(default_factory=lambda: [])
    """A list of valuesMap objects describing attributes."""


class HTTPMethod(StrEnum):
    """
    > HTTP defines a set of request methods to indicate the desired action to be performed for a given resource.
    >
    > -- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

    OpenADR 3 enumerates a subset of all HTTP methods, omitting `PATCH`,
    `HEAD`, `CONNECT`, and `OPTIONS`.
    """

    GET = "GET"
    """
    > Requests a representation of the specified resource. Requests using GET should only retrieve data.
    >
    > -- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods#get
    """

    POST = "POST"
    """
    > submits an entity to the specified resource, often causing a change in state or side effects on the server.
    >
    > -- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods#post
    """

    PUT = "PUT"
    """
    > replaces all current representations of the target resource with the request payload.
    >
    > -- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods#put
    """

    DELETE = "DELETE"
    """
    > deletes the specified resource.
    >
    > -- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods#delete
    """
    # see note in ANNOTATED.yaml asking about "PATCH"


class ObjectOperationSub(BaseModel):
    objects: list[ObjectTypes]
    operations: list[HTTPMethod]
    callbackUrl: Url
    """User provided webhook URL."""
    bearerToken: Optional[str] = None
    """
    User provided token.
    To avoid custom integrations, callback endpoints
    should accept the provided bearer token to authenticate VTN requests.
    """


# TODO: make generic over what kinds of `valuesMaps` are allowed?
class Subscription(BaseModel):
    """
    An object created by a client to receive notification of operations on objects.
    Clients may subscribe to be notified when a type of object is created,
    updated, or deleted.
    """

    id: ObjectID = ""  # FIXME: what's a reasonable default for a field that isn't required, must be 1-128 chars long, and cannot be none?
    createdDateTime: Optional[DateTime] = None
    modificationDateTime: Optional[DateTime] = None
    objectType: Literal["SUBSCRIPTION"]
    clientName: Optional[ShortStr] = None
    programID: Optional[ObjectID] = None
    objectOperations: Sequence[ObjectOperationSub]
    """list of objects and operations to subscribe to."""
    targets: Sequence[Target] | None = None
    """A list of valuesMap objects. Used by server to filter callbacks."""


class Report(BaseModel):
    """report object."""

    id: ObjectID = ""  # FIXME: what's a reasonable default for a field that isn't required, must be 1-128 chars long, and cannot be none?
    createdDateTime: Optional[DateTime] = None
    modificationDateTime: Optional[DateTime] = None
    objectType: Literal["REPORT"]
    programID: ObjectID
    eventID: ObjectID
    clientName: Optional[ShortStr] = None
    """
    User generated identifier; may be VEN ID provisioned during program enrollment.
    """
    reportName: Optional[str] = None
    """User defined string for use in debugging or User Interface."""
    payloadDescriptors: Optional[list[ReportDescriptor]] = None
    """A list of reportPayloadDescriptors."""
    resources: list[ReportResource]
    """
    A list of objects containing report data for a set of resources.
    """


class Event(BaseModel):
    """
    Event object to communicate a Demand Response request to VEN.
    If intervalPeriod is present, sets start time and duration of intervals.
    """

    id: ObjectID = ""
    "VTN provisioned ID of this object instance."

    createdDateTime: Optional[DateTime] = None
    "VTN-provisioned on object creation."

    modificationDateTime: Optional[DateTime] = None
    "VTN-provisioned on object modification."

    objectType: Literal["EVENT"]
    "Used as discriminator, e.g. notification.object"

    programID: ObjectID
    "ID attribute of program object this event is associated with."

    eventName: Optional[str] = None
    """User defined string for use in debugging or User Interface."""

    priority: Optional[PositiveInt] = None
    """
    Relative priority of event. A lower number is a higher priority.
    """

    targets: Sequence[Target] | None = None  # Q: what's the inner kind?
    """A list of valuesMap objects."""

    reportDescriptors: Optional[list[ReportDescriptor]] = None
    """A list of reportDescriptor objects. Used to request reports from VEN."""

    payloadDescriptors: Optional[list["EventPayloadDescriptor"]] = None
    """A list of payloadDescriptor objects."""

    intervalPeriod: Optional[IntervalPeriod] = None
    """Defines default start and durations of intervals."""

    intervals: list[Interval[EventValues]]
    """A list of interval objects."""


class ProgramDescription(BaseModel):
    URL: Url
    """A human or machine readable program description"""


# PayloadType = TypeVar("PayloadType", str, Enum)

# TODO: make generic over payloadType, objectType


class EventPayloadDescriptor(BaseModel):
    """
    Contextual information used to interpret event valuesMap values.
    E.g. a PRICE payload simply contains a price value, an
    associated descriptor provides necessary context such as units and currency.
    """

    objectType: Literal["EVENT_PAYLOAD_DESCRIPTOR"]
    """Used as discriminator, e.g. program.payloadDescriptors"""
    payloadType: ShortStr
    """Enumerated or private string signifying the nature of values."""
    units: Optional[str] = None
    """Units of measure."""
    currency: Optional[str] = None
    """Currency of price payload."""


# TODO: make generic over payloadType, readingType
class ReportPayloadDescriptor(BaseModel):
    """
    Contextual information used to interpret report payload values.
    E.g. a USAGE payload simply contains a usage value, an
    associated descriptor provides necessary context such as units and data quality.
    """

    objectType: Literal["REPORT_PAYLOAD_DESCRIPTOR"]
    """Used as discriminator, e.g. program.payloadDescriptors"""

    payloadType: ShortStr
    """Enumerated or private string signifying the nature of values."""

    units: Optional[str] = None
    """Units of measure."""

    readingType: Optional[str] = None
    """Enumerated or private string signifying the type of reading."""

    accuracy: Optional[StrictFloat] = None
    """A quantification of the accuracy of a set of payload values."""
    # FIXME: ^`"format": "float"` missing from generated json schema

    confidence: Optional[Percent] = None
    """A quantification of the confidence in a set of payload values."""


# TODO: make generic over what kinds of `valuesMaps` are allowed?
class Program(BaseModel):
    """
    Provides program specific metadata from VTN to VEN.
    """

    id: ObjectID = ""  # FIXME: what's a reasonable default for a field that isn't required, must be 1-128 chars long, and cannot be none?
    "VTN provisioned ID of this object instance."

    programName: str
    """Short name to uniquely identify program."""

    programLongName: Optional[str] = None
    """Long name of program for human readability."""

    createDateTime: Optional[DateTime] = None
    "VTN provisioned on object creation."

    modificationDateTime: Optional[DateTime] = None
    "VTN provisioned on object modification."

    objectType: Literal["PROGRAM"] = ObjectTypes.PROGRAM.value
    "Used as discriminator, e.g. notification.object"

    retailerName: Optional[str] = None
    "Short name of energy retailer providing the program."

    retailerLongName: Optional[str] = None
    "Long name of energy retailer for human readability."

    programType: Optional[ShortStr] = None
    "A program defined categorization."

    country: Optional[str] = None
    "Alpha-2 code per ISO 3166-1."

    principalSubdivision: Optional[str] = None
    "Coding per ISO 3166-2. E.g. state in US."

    timeZoneOffset: Optional[Duration] = None
    "Number of hours different from UTC for the standard time applicable to the program."

    intervalPeriod: Optional[IntervalPeriod] = None
    "The temporal span of the program, could be years long."

    programDescriptions: Optional[list[ProgramDescription]] = None
    bindingEvents: bool = False
    """True if events are fixed once transmitted."""

    localPrice: bool = False
    """True if events have been adapted from a grid event."""

    payloadDescriptors: Optional[
        list[ReportPayloadDescriptor | EventPayloadDescriptor]
    ] = None
    """A list of payloadDescriptors"""

    targets: Sequence[Target] | None = None
    """A list of valuesMap objects."""


# TODO: make generic over what kinds of `valuesMaps` are allowed?
class VEN(BaseModel):
    """VEN represents a client with the ven role."""

    id: ObjectID = ""  # FIXME: reasonable default.
    # ^ if the `id`` key is present, then the value must be present
    creationDateTime: Optional[DateTime] = None
    modificationDateTime: Optional[DateTime] = None
    objectType: Literal["VEN"] = ObjectTypes.VEN.value
    venName: Optional[ShortStr] = None
    """
    User generated identifier, may be VEN identifier provisioned during program enrollment.
    """
    attributes: Sequence[Attribute] = Field(default_factory=lambda: [])
    """ A list of valuesMap objects describing attributes."""
    targets: Sequence[Target] | None = Field(default_factory=lambda: [])
    """A list of valuesMap objects describing target criteria."""
    resources: Optional[list[Resource]] = None


# TODO: make generic over what kinds of `valuesMaps` are allowed?
class Notification(BaseModel):
    """
    VTN generated object included in request to subscription callbackUrl.
    """

    objectType: ObjectTypes
    operation: HTTPMethod
    """
    The operation on on object that triggered the notification.
    """
    targets: Sequence[Target] | None = None
    """
    A list of valuesMap objects.
    """
    object: Union[Program, Event, Report, Subscription, Resource, VEN] = Field(
        ..., discriminator="objectType"
    )
    """
    the object that is the subject of the notification.
    """

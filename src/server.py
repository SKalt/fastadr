# from datetime import timedelta
# Duration = Annotated[timedelta]
# """duration in ISO 8601 format""" # e.g. PT1H
from datetime import datetime, timedelta
from enum import Enum
from typing import Annotated, Literal, Optional, TypeVar, Union

import annotated_types
from pydantic import BaseModel, StringConstraints
from pydantic_core import Url


class OAuthScopes(Enum):
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

Duration = Annotated[str, timedelta] # FIXME: validate ISO 8601 format
"""duration in ISO 8601 format"""

DateTime = Annotated[str, datetime]
"""datetime in ISO 8601 format"""

HTTPStatusCode = Annotated[int, annotated_types.Ge(100), annotated_types.Lt(600)]

ObjectID = Annotated[str, StringConstraints(pattern="^[a-zA-Z0-9_-]*$")]
"""URL safe VTN assigned object ID."""
# TODO: shouldn't ObjectID have at least one character?

Percent = Annotated[int, annotated_types.Ge(0), annotated_types.Le(100)]

class Problem(BaseModel):
    """reusable error response. From https://opensource.zalando.com/problem/schema.yaml."""
    type: Url = Url("about:blank") # really a URI
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


class ReportResource(BaseModel):
    """Report data associated with a resource."""
    resourceName: Optional[str] = None
    """
    User generated identifier. A value of AGGREGATED_REPORT indicates an aggregation of more that one resource's data
    """
    intervalPeriod: Optional["IntervalPeriod"] = None
    intervals: list["Interval"]
    """A list of interval objects."""


class ObjectTypes(Enum):
    PROGRAM = "PROGRAM"
    EVENT = "EVENT"
    REPORT = "REPORT"
    SUBSCRIPTION = "SUBSCRIPTION"
    VEN = "VEN"
    RESOURCE = "RESOURCE"
    # EVENT_PAYLOAD_DESCRIPTOR = "EVENT_PAYLOAD_DESCRIPTOR"


class Point(BaseModel):
    """
    A pair of floats typically used as a point on a 2 dimensional grid.
    """
    x: Optional[float] = None
    """A value on an x axis."""
    y: Optional[float] = None
    """A value on a y axis."""


class ValuesMap(BaseModel):
    """
    Represents one or more values associated with a type.
    E.g. a type of PRICE contains a single float value.
    """
    type: str
    """
    Enumerated or private string signifying the nature of values.
    E.G. "PRICE" indicates value is to be interpreted as a currency.
    """
    values: list[int | float | str | bool | Point]
    """
    The value associated with the type.
    """


class ReportDescriptor(BaseModel):
    """
    An object that may be used to request a report from a VEN.
    See OpenADR REST User Guide for detailed description of how configure a report request.
    """
    payloadType: str
    """
    Enumerated or private string signifying the nature of values.
    """
    readingType: Optional[str] = None
    """
    Enumerated or private string signifying the type of reading.
    """
    targets: Optional[list[ValuesMap]] = None
    """A list of valuesMap objects."""
    aggregate: bool = False
    """
    True if report should aggregate results from all targeted resources.
    False if report includes results for each resource.
    """
    startInterval: Optional[int] = -1
    """
    The interval on which to generate a report.
    -1 indicates generate report at end of last interval.
    """
    numIntervals: int = -1
    """
    The number of intervals to include in a report.
    -1 indicates that all intervals are to be included.
    """
    historical: bool = True
    """
    True indicates report on intervals preceding startInterval.
    False indicates report on intervals following startInterval (e.g. forecast).
    """
    frequency: Optional[int] = -1
    """
    Number of intervals that elapse between reports.
    -1 indicates same as numIntervals.
    """
    repeat: int = 1
    """
    Number of times to repeat report.
    1 indicates generate one report.
    -1 indicates repeat indefinitely.
    """


class IntervalPeriod(BaseModel):
    """
    Defines temporal aspects of intervals.
    A duration of default null indicates infinity.
    A randomizeStart of default null indicates no randomization.
    """
    start: DateTime
    randomizeStart: Optional[Duration] = None


class Interval(BaseModel):
    """
    An object defining a temporal window and a list of valuesMaps.
    if intervalPeriod present may set temporal aspects of interval or override event.intervalPeriod.
    """
    id: int
    """
    A client generated number assigned an interval object. Not a sequence number.
    """
    intervalPeriod: Optional[IntervalPeriod]
    """Defines default start and durations of intervals."""
    payloads: list[ValuesMap]
    """A list of valuesMap objects."""


class Resource(BaseModel):
    """
    A resource is an energy device or system subject to control by a VEN.
    """
    id: Optional[ObjectID]
    createdDateTime: Optional[DateTime]
    modificationDateTime: Optional[DateTime]
    objectType: Literal["RESOURCE"] = ObjectTypes.RESOURCE.value
    """Used as discriminator, e.g. notification.object"""
    resourceName: Optional[str| None] = None
    """
    User generated identifier, resource may be configured with identifier out-of-band.
    """
    venID: Optional[ObjectID]
    attributes: Optional[list[ValuesMap]]
    """A list of valuesMap objects describing attributes."""


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class Notification(BaseModel):
    """
    VTN generated object included in request to subscription callbackUrl.
    """
    objectType: ObjectTypes
    operation: HTTPMethod
    """
    The operation on on object that triggered the notification.
    """
    targets: Optional[list[ValuesMap]] = None
    """
    A list of valuesMap objects.
    """
    object: Union["Program", "Event", "Report", "Subscription", Resource , "VEN"]
    """
    the object that is the subject of the notification.
    """


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

class Subscription(BaseModel):
    """
    An object created by a client to receive notification of operations on objects.
    Clients may subscribe to be notified when a type of object is created,
    updated, or deleted.
    """
    id: Optional[ObjectID]
    createdDateTime: Optional[DateTime]
    modificationDateTime: Optional[DateTime]
    objectType: Literal["SUBSCRIPTION"] = ObjectTypes.SUBSCRIPTION.value
    clientName: Optional[str] = None
    programID: Optional[ObjectID] = None
    objectOperations: list[ObjectOperationSub]
    """list of objects and operations to subscribe to."""
    targets: Optional[list[ValuesMap]] = None
    """A list of valuesMap objects. Used by server to filter callbacks."""


class Report(BaseModel):
    """report object."""
    id: Optional[ObjectID]
    createdDateTime: Optional[DateTime]
    modificationDateTime: Optional[DateTime]
    objectType: Literal["REPORT"] = ObjectTypes.REPORT.value
    programID: ObjectID
    eventID: ObjectID
    clientName: Optional[str] = None
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
    id: Optional[ObjectID] = None
    createdDateTime: Optional[DateTime] = None
    modificationDateTime: Optional[DateTime] = None
    objectType: Literal["EVENT"] = ObjectTypes.EVENT.value
    programID: ObjectID
    eventName: Optional[str] = None
    """User defined string for use in debugging or User Interface."""
    priority: Optional[int] = None
    """
    Relative priority of event. A lower number is a higher priority.
    """
    targets: Optional[list[ValuesMap]] = None
    """A list of valuesMap objects."""
    reportDescriptors: Optional[list[ReportDescriptor]] = None
    """A list of reportDescriptor objects. Used to request reports from VEN."""
    payloadDescriptors: Optional[list["EventPayloadDescriptor"]] = None
    """A list of payloadDescriptor objects."""
    intervalPeriod: Optional[IntervalPeriod] = None
    intervals: list[Interval]
    """A list of interval objects."""


class ProgramDescription(BaseModel):
    url: Url
    """A human or machine readable program description"""

PayloadType = TypeVar("PayloadType", str, Enum)

# TODO: make generic over payloadType, objectType
class EventPayloadDescriptor(BaseModel):
    """
    Contextual information used to interpret event valuesMap values.
    E.g. a PRICE payload simply contains a price value, an
    associated descriptor provides necessary context such as units and currency.
    """
    objectType: str = "EVENT_PAYLOAD_DESCRIPTOR"
    """Used as discriminator, e.g. program.payloadDescriptors"""
    payloadType: str
    """Enumerated or private string signifying the nature of values."""
    units: str = "KWH"
    """Units of measure."""
    currency: str = "USD"
    """Currency of price payload."""


# TODO: make generic over payloadType, readingType
class ReportPayloadDescriptor(BaseModel):
    """
    Contextual information used to interpret report payload values.
    E.g. a USAGE payload simply contains a usage value, an
    associated descriptor provides necessary context such as units and data quality.
    """
    objectType: str = "REPORT_PAYLOAD_DESCRIPTOR"
    """Used as discriminator, e.g. program.payloadDescriptors"""
    payloadType: str
    """Enumerated or private string signifying the nature of values."""
    units: str = "KWH"
    """Units of measure."""
    readingType: str = "DIRECT_READ"
    """Enumerated or private string signifying the type of reading."""
    accuracy: float = 0.0
    """A quantification of the accuracy of a set of payload values."""
    confidence: Percent = 100
    """A quantification of the confidence in a set of payload values."""

class Program(BaseModel):
    """
    Provides program specific metadata from VTN to VEN.
    """
    id: Optional[ObjectID]
    programName: str
    """Short name to uniquely identify program."""
    programLongName: Optional[str] = None
    """Long name of program for human readability."""
    createDateTime: Optional[DateTime] = None
    modificationDateTime: Optional[DateTime] = None
    objectType: Literal["PROGRAM"] = ObjectTypes.PROGRAM.value
    retailerName: Optional[str] = None
    """
    Short name of energy retailer providing the program.
    """
    retailerLongName: Optional[str] = None
    """
    Long name of energy retailer for human readability.
    """
    programType: Optional[str] = None
    """
    A program defined categorization.
    """
    country: Optional[str] = None
    """Alpha-2 code per ISO 3166-1."""
    principalSubdivision: Optional[str] = None
    """Coding per ISO 3166-2. E.g. state in US."""
    timeZoneOffset: Optional[Duration] = None
    intervalPeriod: Optional[IntervalPeriod] = None
    programDescriptions: Optional[list[ProgramDescription]] = None
    bindingEvents: bool = False
    """True if events are fixed once transmitted."""
    localPrice: bool = False
    """True if events have been adapted from a grid event."""
    payloadDescriptors: Optional[list[ ReportPayloadDescriptor | EventPayloadDescriptor ]] = None
    """A list of payloadDescriptors"""
    targets: Optional[list[ValuesMap]] = None
    """A list of valuesMap objects."""


class VEN(BaseModel):
    """VEN represents a client with the ven role."""
    id: Optional[ObjectID]
    creationDateTime: Optional[DateTime]
    modificationDateTime: Optional[DateTime]
    objectType: Literal["VEN"] = ObjectTypes.VEN.value
    venName: Optional[str] = None
    """
    User generated identifier, may be VEN identifier provisioned during program enrollment.
    """
    attributes: list[ValuesMap]
    """ A list of valuesMap objects describing attributes."""
    targets: Optional[list[ValuesMap]] = None
    """A list of valuesMap objects describing target criteria."""
    resources: Optional[list[Resource]] = None
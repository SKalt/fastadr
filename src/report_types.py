from enum import StrEnum
from typing import Annotated, Literal, Sequence

from pydantic import Field
from .values_map import AnyValue, ValuesMap, AnyValuesMap, One


class ReportKind(StrEnum):
    READING = "READING"
    USAGE = "USAGE"
    DEMAND = "DEMAND"
    SETPOINT = "SETPOINT"
    DELTA_USAGE = "DELTA_USAGE"
    BASELINE = "BASELINE"
    OPERATING_STATE = "OPERATING_STATE"
    UP_REGULATION_AVAILABLE = "UP_REGULATION_AVAILABLE"
    DOWN_REGULATION_AVAILABLE = "DOWN_REGULATION_AVAILABLE"
    REGULATION_SETPOINT = "REGULATION_SETPOINT"
    STORAGE_USABLE_CAPACITY = "STORAGE_USABLE_CAPACITY"
    STORAGE_CHARGE_LEVEL = "STORAGE_CHARGE_LEVEL"
    STORAGE_MAX_DISCHARGE_POWER = "STORAGE_MAX_DISCHARGE_POWER"
    STORAGE_MAX_CHARGE_POWER = "STORAGE_MAX_CHARGE_POWER"
    SIMPLE_LEVEL = "SIMPLE_LEVEL"
    USAGE_FORECAST = "USAGE_FORECAST"
    STORAGE_DISPATCH_FORECAST = "STORAGE_DISPATCH_FORECAST"
    LOAD_SHED_DELTA_AVAILABLE = "LOAD_SHED_DELTA_AVAILABLE"
    GENERATION_DELTA_AVAILABLE = "GENERATION_DELTA_AVAILABLE"
    DATA_QUALITY = "DATA_QUALITY"
    IMPORT_RESERVATION_CAPACITY = "IMPORT_RESERVATION_CAPACITY"
    IMPORT_RESERVATION_FEE = "IMPORT_RESERVATION_FEE"
    EXPORT_RESERVATION_CAPACITY = "EXPORT_RESERVATION_CAPACITY"
    EXPORT_RESERVATION_FEE = "EXPORT_RESERVATION_FEE"


Reading = ValuesMap[Literal[ReportKind.READING], One[float]]
"""
> An instantaneous data point, as from a meter. Same as pulse count. Payload
> value is a float and units are defined in payloadDescriptor.
"""
Usage = ValuesMap[Literal[ReportKind.USAGE], One[float]]
"""
> Energy usage over an interval. Payload value is a float and units are defined in
> payloadDescriptor.
"""

Demand = ValuesMap[Literal[ReportKind.DEMAND], One[float]]
"""
> Power usage for an interval, i.e. Real Power. Payload value is a float, units
> defined in payloadDescriptor. Reading type indicates MEAN, PEAK,
> FORECAST
"""

Setpoint = ValuesMap[Literal[ReportKind.SETPOINT], Sequence[AnyValue]]
"""
> Current control setpoint of a resource, see CONTROL_SETPOINT event
> payloadType above. Payload values are determined by application.
"""
DeltaUsage = ValuesMap[Literal[ReportKind.DELTA_USAGE], One[float]]
"""
> Change in usage as compared to a baseline. Payload value is a float and units
> are defined in payloadDescriptor.
"""

Baseline = ValuesMap[Literal[ReportKind.BASELINE], Sequence[AnyValue]]
"""
> Indicates energy or power consumption in the absence of load control.
> Payload value is determined by reading type which may indicate usage or
> demand.
"""


class OperatingState(StrEnum):
    NORMAL = "NORMAL"
    """
    > Resource is operating normally. No Demand Response directives are
    > currently being followed.
    """
    ERROR = "ERROR"
    """
    > Resource has self-reported an error or is not addressable by VEN.
    """
    IDLE_NORMAL = "IDLE_NORMAL"
    """
    > CTA-2045 device "Indicates that no demand response event is in effect
    > and the SGD has no/insignificant energy consumption."
    """
    RUNNING_NORMAL = "RUNNING_NORMAL"
    """
    > CTA-2045 device "Indicates that no demand response event is in effect
    > and the SGD has significant energy consumption."
    """
    RUNNING_CURTAILED = "RUNNING_CURTAILED"
    """
    > CTA-2045 device "Indicates that a curtailment type demand response
    > event is in effect and the SGD has significant energy consumption."
    """
    RUNNING_HEIGHTENED = "RUNNING_HEIGHTENED"
    """
    > CTA-2045 device "Indicates that a heightened-operation type of demand
    > response event is in effect and the SGD has significant energy
    > consumption."
    """
    IDLE_CURTAILED = "IDLE_CURTAILED"
    """
    > CTA-2045 device "Indicates that a curtailment type demand response
    > event is in effect and the SGD has no/insignificant energy consumption."
    """
    SGD_ERROR_CONDITION = "SGD_ERROR_CONDITION"
    """
    > CTA-2045 device "Indicates that the SGD is not operating because it
    > needs maintenance support or is in some way disabled (i.e. no response
    > to the grid)."
    """
    IDLE_HEIGHTENED = "IDLE_HEIGHTENED"
    """
    > CTA-2045 device "Indicates that a heightened-operation type of demand
    > response event is in effect and the SGD has no/insignificant energy
    > consumption."
    """
    IDLE_OPTED_OUT = "IDLE_OPTED_OUT"
    """
    > CTA-2045 device "Indicates that the SGD is presently opted out of any
    > demand response events and the SGD has no/insignificant energy
    > consumption."
    """
    RUNNING_OPTED_OUT = "RUNNING_OPTED_OUT"
    """
    > CTA-2045 device "Indicates that the SGD is presently opted out of any
    > demand response events and the SGD has significant energy
    > consumption."
    """


OperatingStateReport = ValuesMap[
    Literal[ReportKind.OPERATING_STATE], Sequence[OperatingState]
]
"""
> Payload values array includes a list of operating state enumerations, see
> below
"""
UpRegulationAvailable = ValuesMap[
    Literal[ReportKind.UP_REGULATION_AVAILABLE], One[float]
]
"""
> Up Regulation capacity available for dispatch, in real power. Payload value is a
> float, units defined in payloadDescriptor. Reading type indicates MEAN, PEAK,
> FORECAST
"""

DownRegulationAvailable = ValuesMap[
    Literal[ReportKind.DOWN_REGULATION_AVAILABLE], One[float]
]
"""
> Down Regulation capacity available for dispatch, in real power. Payload value
> is a float, units defined in payloadDescriptor. Reading type indicates MEAN,
> PEAK, FORECAST.
"""

RegulationSetpoint = ValuesMap[Literal[ReportKind.REGULATION_SETPOINT], One[float]]
"""
> Regulation setpoint as instructed as part of regulation services. Payload value
> is a float, units defined in payloadDescriptor. Reading type indicates MEAN,
> PEAK, FORECAST.
"""
StorageUsableCapacity = ValuesMap[
    Literal[ReportKind.STORAGE_USABLE_CAPACITY], One[float]
]
"""
> Usable energy that the storage device can hold when fully charged. Payload
> value is a float, units of energy defined in payloadDescriptor.
"""
StorageChargeLevel = ValuesMap[Literal[ReportKind.STORAGE_CHARGE_LEVEL], One[float]]
"""
> Current storage charge level expressed as a percentage, where 0% is empty
> and 100% is full. Payload value is a float, units of PERCENT defined in
> payloadDescriptor
"""

StorageMaxDischargePower = ValuesMap[
    Literal[ReportKind.STORAGE_MAX_DISCHARGE_POWER], One[float]
]
"""
> The maximum sustainable power that can be discharged into an electricity
> network (injection). Payload value is a float, units of power defined in
> payloadDescriptor.
"""

StorageMaxChargePower = ValuesMap[
    Literal[ReportKind.STORAGE_MAX_CHARGE_POWER], One[float]
]
"""
> The maximum sustainable power that can be charged from an electricity
> network (load). Payload value is a float, units of power defined in
> payloadDescriptor.
"""

SimpleLevel = ValuesMap[Literal[ReportKind.SIMPLE_LEVEL], One[Literal[0, 1, 2, 3]]]
"""
> Simple level that a VEN resource is operating at for each Interval. Payload
> value is an integer 0, 1, 2, 3 corresponding to values in SIMPLE events.
"""

UsageForecast = ValuesMap[Literal[ReportKind.USAGE_FORECAST], One[float]]
"""
> Payload values array contains a single float indicating expected resource
> usage for the associated interval. Units of energy defined in payloadDescriptor.
"""

StorageDispatchForecast = ValuesMap[
    Literal[ReportKind.STORAGE_DISPATCH_FORECAST], One[float]
]
"""
> Payload values array contains a single float indicating expected stored energy
> that could be dispatched for the associated interval
"""
LoadShedDeltaAvailable = ValuesMap[
    Literal[ReportKind.LOAD_SHED_DELTA_AVAILABLE], One[float]
]
"""
> Payload values array contains a single float indicating expected increase or
> decrease in load by a resource for the associated interval.
"""
GenerationDeltaAvailable = ValuesMap[
    Literal[ReportKind.GENERATION_DELTA_AVAILABLE], One[float]
]
"""
> Payload values array contains a single float indicating expected generation by
> a resource for the associated interval
"""


class DataQualityLevel(StrEnum):
    OK = "OK"
    """
    > There are no known reasons to doubt the validity of the data.
    """
    MISSING = "MISSING"
    """
    > The data item is unavailable for this interval.
    """
    ESTIMATED = "ESTIMATED"
    """
    > This data item has been estimated from other relevant information such as adjacent
    > intervals.
    """
    BAD = "BAD"
    """
    > There is a data item but it is known or suspected to be erroneous
    """


DataQualityReport = ValuesMap[Literal[ReportKind.DATA_QUALITY], One[DataQualityLevel]]
"""
> Payload values array contains a string indicating data quality of companion
> report payload in the same interval. Strings may be one of enumerated Data
> Quality enumerations
"""

ImportReservationCapacity = ValuesMap[
    Literal[ReportKind.IMPORT_RESERVATION_CAPACITY],
    Sequence[float],  # <- Q: shouldn't this be nonempty?
]
"""
> Amount of additional import capacity requested. Payload values are a float.
"""

ImportReservationFee = ValuesMap[Literal[ReportKind.IMPORT_RESERVATION_FEE], One[float]]
"""
> Amount per unit of import capacity that the VEN is willing to pay for the
> requested reservation. Payload value is a float with currency defined in payloadDescriptor.
"""
# Q: "a float": just one, right? 0, 2+ are invalid?

ExportReservationCapacity = ValuesMap[
    Literal[ReportKind.EXPORT_RESERVATION_CAPACITY], One[float]
]
"""
> Amount of additional export capacity requested. Payload values are a float
"""
ExportReservationFee = ValuesMap[Literal[ReportKind.EXPORT_RESERVATION_FEE], One[float]]
"""
> Amount per unit of export capacity that the VEN is willing to pay for the
> requested reservation. Payload value is a float with currency defined in
> payloadDescriptor.
"""


class ReadingType(StrEnum):
    DIRECT_READ = "DIRECT_READ"
    """
    > Payload values have been determined by direct measurement from a resource.
    """
    ESTIMATED = "ESTIMATED"
    """
    > Payload value is an estimate where no Direct Read was available for the
    > interval, but sufficient other data exist to make a reasonable estimate.
    """
    SUMMED = "SUMMED"
    """> Payload value is the sum of multiple data sources"""
    MEAN = "MEAN"
    """> Payload value represents the mean measurements over an interval"""
    PEAK = "PEAK"
    """> Payload value represents the highest measurement over an interval"""
    FORECAST = "FORECAST"
    """
    > Payload value is a forecast of future values, not a measurement or estimate of
    > actual data
    """
    AVERAGE = "AVERAGE"
    """
    > Payload value represents the average of measurements over an interval.
    """


# class ResourceNameKind(StrEnum):
#     AGGREGATED_REPORT = "AGGREGATED_REPORT"
#     """
#     > A report contains a list of resources, each of which may contain a list of
#     > intervals containing reporting data. Each item in the resource list contains a
#     > resourceName attribute. This resourceName indicates the the interval data
#     > is the aggregate of data from more than one resource.
#     """


class TargetKind(StrEnum):
    POWER_SERVICE_LOCATION = "POWER_SERVICE_LOCATION"
    """
    > A Power Service Location is a utility named specific location in geography or
    > the distribution system, usually the point of service to a customer site
    """
    SERVICE_AREA = "SERVICE_AREA"
    """
    > A Service Area is a utility named geographic region. Target values array
    > contains a string representing a service area name
    """
    GROUP = "GROUP"
    """
    > Target values array contains a string representing a group
    """
    RESOURCE_NAME = "RESOURCE_NAME"
    """
    > Target values array contains a string representing a resource name
    """
    VEN_NAME = "VEN_NAME"
    """
    > Target values array contains a string representing a VEN name
    """
    EVENT_NAME = "EVENT_NAME"
    """
    > Target values array contains a string representing an event name
    """
    PROGRAM_NAME = "PROGRAM_NAME"
    """
    > Target values array contains a string representing a program name
    """


class Unit(StrEnum):
    KWH = "KWH"
    """> kilowatt-hours (kWh)"""
    GHG = "GHG"
    """> g/kWh"""
    VOLTS = "VOLTS"
    """> volts (V)"""
    AMPS = "AMPS"
    """> Current (A)"""
    CELSIUS = "CELSIUS"
    """> Temperature (C)"""
    FAHRENHEIT = "FAHRENHEIT"
    """> Temperature (F)"""
    PERCENT = "PERCENT"
    """%"""
    KW = "KW"
    KVAH = "KVAH"
    """
    > kilovolt-ampere hours (kVAh)
    """
    KVAR = "KVAR"
    """
    > kilovolt-ampere reactive (kVAR)
    """
    KVARH = "KVARH"
    """
    > kilovolt-ampere reactive hours (kVARh)
    """
    KVA = "KVA"
    """
    > kilovolt-amperes (kVA)
    """


PredefinedReport = Annotated[
    Reading
    | Usage
    | Demand
    | Setpoint
    | DeltaUsage
    | Baseline
    | OperatingStateReport
    | UpRegulationAvailable
    | DownRegulationAvailable
    | RegulationSetpoint
    | StorageUsableCapacity
    | StorageChargeLevel
    | StorageMaxDischargePower
    | StorageMaxChargePower
    | SimpleLevel
    | UsageForecast
    | StorageDispatchForecast
    | LoadShedDeltaAvailable
    | GenerationDeltaAvailable
    | DataQualityReport
    | ImportReservationCapacity
    | ImportReservationFee
    | ExportReservationCapacity
    | ExportReservationFee,
    Field(discriminator="type"),
]

ReportValues = PredefinedReport | AnyValuesMap

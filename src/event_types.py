# see Definitions, section 10.2, page 15
# TODO: consider using typing.NewType to ensure values are correctly interpreted
from typing import Annotated, Literal
import annotated_types
from pydantic import Field
from .values_map import ValuesMap, AnyValue, AnyValuesMap
from .values_map import Point


Portion = Annotated[float, annotated_types.Ge(0.0), annotated_types.Le(1.0)]
HumanReadableStr = Annotated[str, annotated_types.Len(1, 1024 * 1024)]
"""A non-empty string of at most 1MB of UTF-8 encoded text."""


Simple = ValuesMap[Literal["SIMPLE"], Literal[0, 1, 2, 3]]
"""
> An indication of the level of a basic demand response signal. Payload
> value is an integer of 0, 1, 2, or 3.
> Note: An example mapping is normal operations, moderate load shed,
> high load shed, and emergency load shed
> -- Definitions, section 10.2, page 17
"""
Price = ValuesMap[Literal["PRICE"], float]
"""
> The price of energy. Payload value is a float. Units and currency
> defined in associated eventPayloadDescriptor.
"""
Charge = ValuesMap[Literal["CHARGE_STATE_SETPOINT"], AnyValue]
"""
> The state of charge of an energy storage resource. Payload value is
> indicated by units in associated eventPayloadDescriptor.
> Note: Common units are percentage and kWh
"""
DispatchSetpoint = ValuesMap[Literal["DISPATCH_SETPOINT_RELATIVE"], float]
"""
> The relative change of consumption by a resource. Payload value is a
> float and is indicated by units in associated eventPayloadDescriptor.
> Note: This is used to dispatch a resource's load
"""
ControlSetpoint = ValuesMap[Literal["CONTROL_SETPOINT"], AnyValue]
"""
> Resource dependent setting. Payload value type depends on
> application.
"""
ExportPrice = ValuesMap[Literal["EXPORT_PRICE"], float]
"""
> The price of energy exported (usually to the grid). Payload value is
> float and units and currency are defined in associated
> eventPayloadDescriptor.
> Note: Can be used for any form of energy.
"""
GreenhouseGas = ValuesMap[Literal["GHG"], float]
"""
> An estimate of marginal GreenHouse Gas emissions, in g/kWh.
> Payload value is float.
"""
Curve = ValuesMap[Literal["CURVE"], Point]
"""
> Payload values array contains a series of one or more pairs of floats
> representing a 2D point.
> Note: May be used to represent a curve of values, e.g. VoltVar values.
"""
OptimumLoadShape = ValuesMap[Literal["OLS"], Portion]
"""
> Optimum Load Shape. Payload values array contains a list of values
> 0.0 to 1.0 representing percentage of usage over the set of intervals in
> the event.
> Note: See ANSI-SCTE 267
"""
ImportCapacitySubscription = ValuesMap[Literal["IMPORT_CAPACITY_SUBSCRIPTION"], float]
"""
> The amount of import capacity a customer has subscribed to in
> advance. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor.
"""
ImportCapacityReservation = ValuesMap[Literal["IMPORT_CAPACITY_RESERVATION"], float]
"""
> The amount of additional import capacity that a customer has been
> granted by the VTN. Payload is a float, and meaning is indicated by
> units in associated eventPayloadDescriptor.
"""
ImportCapacityReservationFee = ValuesMap[
    Literal["IMPORT_CAPACITY_RESERVATION_FEE"], float
]
"""
> The cost per unit of power of extra import capacity available for
> reservation. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor.
"""
ImportCapacityAvailable = ValuesMap[Literal["IMPORT_CAPACITY_AVAILABLE"], float]
"""
> The amount of extra import capacity available for reservation to the
> customer. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor.
"""

ImportCapacityPrice = ValuesMap[Literal["IMPORT_CAPACITY_AVAILABLE_PRICE"], float]
"""
> The cost per unit of power of extra import capacity available for
> reservation. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor.
"""
ExportCapacitySubscription = ValuesMap[Literal["EXPORT_CAPACITY_SUBSCRIPTION"], float]
"""
> The amount of export capacity a customer has subscribed to in
> advance. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor
"""
ExportCapacityReservation = ValuesMap[Literal["EXPORT_CAPACITY_RESERVATION"], float]
"""
> The amount of additional export capacity that a customer has been
> granted by the VTN. Payload is a float, and meaning is indicated by
> units in associated eventPayloadDescriptor
"""
ExportCapacityReservationFee = ValuesMap[
    Literal["EXPORT_CAPACITY_RESERVATION_FEE"], float
]
"""
> The cost per unit of power of extra export capacity available for
> reservation. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor
"""
ExportCapacityAvailable = ValuesMap[Literal["EXPORT_CAPACITY_AVAILABLE"], float]
"""
> The amount of extra export capacity available for reservation to the
> customer. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor.
"""
ImportCapacityLimit = ValuesMap[Literal["IMPORT_CAPACITY_LIMIT"], float]
"""
> The cost per unit of power of extra export capacity available for
> reservation. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor
"""
ExportCapacityLimit = ValuesMap[Literal["EXPORT_CAPACITY_LIMIT"], float]
"""
> The maximum export level for the site. Payload is a float and meaning
> is indicated by units in associated eventPayloadDescriptor
"""
GridEmergencyAlert = ValuesMap[Literal["ALERT_GRID_EMERGENCY"], HumanReadableStr]
"""
> There is an imminent risk of the grid failing to continue supplying
> power to some customers, maintaining operational parameters (e.g.
> voltage), or ceasing to operate at all. Payload value contains a
> human-readable string describing the alert.
"""
BlackStartAlert = ValuesMap[Literal["ALERT_BLACK_START"], HumanReadableStr]
"""
> The grid is in the process of resuming full operation. Devices should
> minimize electricity use until the event is cleared. Payload value
> contains a human-readable string describing the alert.
"""
PossibleOutageAlert = ValuesMap[Literal["ALERT_POSSIBLE_OUTAGE"], HumanReadableStr]
"""
> Customers may lose grid power in the coming hours or days.
> Note: An example of this from California is Public Service Power
> Shutoffs (usually from fire risk). Payload value contains a
> human-readable string describing the alert
"""
FlexAlert = ValuesMap[Literal["ALERT_FLEX_ALERT"], HumanReadableStr]
"""
> Power supply will be scarce during the event. Devices should seek to
> shift load to times before or after the event. Devices that can shed
> should do so during the event. Payload value contains a
> human-readable string describing the alert.
> Note: See: https://flexalert.org
"""
FireAlert = ValuesMap[Literal["ALERT_FIRE"], HumanReadableStr]
"""
> There is a substantial risk of fire in the area which could interrupt
> electricity supply in addition to being a danger to life and property.
> Payload value contains a human-readable string describing the alert.
"""
FreezingAlert = ValuesMap[Literal["ALERT_FREEZING"], HumanReadableStr]
"""
> There is (or is forecast to be) temperatures low enough to be of
> concern. Payload value contains a human-readable string describing
> the alert
"""
WindAlert = ValuesMap[Literal["ALERT_WIND"], HumanReadableStr]
"""
> There is (or is forecast to be) wind speeds high enough to be of
> concern. Includes hurricanes. Payload value contains a
> human-readable string describing the alert.
"""
TsunamiAlert = ValuesMap[Literal["ALERT_TSUNAMI"], HumanReadableStr]
"""
> Tsunami waves expected to hit the coastline. Payload value contains a
> human-readable string describing the alert.
"""
AirQualityAlert = ValuesMap[Literal["ALERT_AIR_QUALITY"], HumanReadableStr]
"""
> Air quality is or is forecast to be. Payload value contains a
> human-readable string describing the alert
"""
OtherAlert = ValuesMap[Literal["ALERT_OTHER"], HumanReadableStr]
"""
No specific definition. See associated text data element. Payload value
contains a human-readable string describing the alert
"""

Reboot = ValuesMap[Literal["REBOOT"], Literal[0, 1]]
"""
> Pass through for resources that support [CTA-2045B]. Payload value 0
> = SOFT, 1 = HARD. See [CTA-2045B] for definitions
"""

OverrideStatus = ValuesMap[Literal["CTA2045_SET_OVERRIDE_STATUS"], Literal[0, 1]]
"""
> Pass through CTA-2045 Override status: 0 = No Override, 1 =
> Override. See [CTA-2045B]
"""
PredefinedEvent = Annotated[
    Simple
    | Price
    | Charge
    | DispatchSetpoint
    | ControlSetpoint
    | ExportPrice
    | GreenhouseGas
    | Curve
    | OptimumLoadShape
    | ImportCapacitySubscription
    | ImportCapacityReservation
    | ImportCapacityReservationFee
    | ImportCapacityAvailable
    | ImportCapacityPrice
    | ExportCapacitySubscription
    | ExportCapacityReservation
    | ExportCapacityReservationFee
    | ExportCapacityAvailable
    | ImportCapacityLimit
    | ExportCapacityLimit
    | GridEmergencyAlert
    | BlackStartAlert
    | PossibleOutageAlert
    | FlexAlert
    | FireAlert
    | FreezingAlert
    | WindAlert
    | TsunamiAlert
    | AirQualityAlert
    | OtherAlert
    | Reboot
    | OverrideStatus,
    Field(discriminator="type"),
]
EventValues = PredefinedEvent | AnyValuesMap

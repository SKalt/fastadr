# see Definitions, section 10.2, page 15
# TODO: consider using typing.NewType to ensure values are correctly interpreted
from enum import StrEnum
from typing import Annotated, Literal, Sequence
import annotated_types
from pydantic import Field
from .values_map import (
    MaybeOne,
    One,
    ValuesMap,
    AnyValue,
    AnyValuesMap,
    NonEmptyStr,
)
from .values_map import Point


Portion = Annotated[float, annotated_types.Ge(0.0), annotated_types.Le(1.0)]


class EventKind(StrEnum):
    # TODO: document where these come from and where they occur
    SIMPLE = "SIMPLE"
    PRICE = "PRICE"
    CHARGE_STATE_SETPOINT = "CHARGE_STATE_SETPOINT"
    DISPATCH_SETPOINT_RELATIVE = "DISPATCH_SETPOINT_RELATIVE"
    CONTROL_SETPOINT = "CONTROL_SETPOINT"
    EXPORT_PRICE = "EXPORT_PRICE"
    GHG = "GHG"
    CURVE = "CURVE"
    OLS = "OLS"
    IMPORT_CAPACITY_SUBSCRIPTION = "IMPORT_CAPACITY_SUBSCRIPTION"
    IMPORT_CAPACITY_RESERVATION = "IMPORT_CAPACITY_RESERVATION"
    IMPORT_CAPACITY_RESERVATION_FEE = "IMPORT_CAPACITY_RESERVATION_FEE"
    IMPORT_CAPACITY_AVAILABLE = "IMPORT_CAPACITY_AVAILABLE"
    IMPORT_CAPACITY_AVAILABLE_PRICE = "IMPORT_CAPACITY_AVAILABLE_PRICE"
    EXPORT_CAPACITY_SUBSCRIPTION = "EXPORT_CAPACITY_SUBSCRIPTION"
    EXPORT_CAPACITY_RESERVATION = "EXPORT_CAPACITY_RESERVATION"
    EXPORT_CAPACITY_RESERVATION_FEE = "EXPORT_CAPACITY_RESERVATION_FEE"
    EXPORT_CAPACITY_AVAILABLE = "EXPORT_CAPACITY_AVAILABLE"
    IMPORT_CAPACITY_LIMIT = "IMPORT_CAPACITY_LIMIT"
    EXPORT_CAPACITY_LIMIT = "EXPORT_CAPACITY_LIMIT"
    ALERT_GRID_EMERGENCY = "ALERT_GRID_EMERGENCY"
    ALERT_BLACK_START = "ALERT_BLACK_START"
    ALERT_POSSIBLE_OUTAGE = "ALERT_POSSIBLE_OUTAGE"
    ALERT_FLEX_ALERT = "ALERT_FLEX_ALERT"
    ALERT_FIRE = "ALERT_FIRE"
    ALERT_FREEZING = "ALERT_FREEZING"
    ALERT_WIND = "ALERT_WIND"
    ALERT_TSUNAMI = "ALERT_TSUNAMI"
    ALERT_AIR_QUALITY = "ALERT_AIR_QUALITY"
    ALERT_OTHER = "ALERT_OTHER"
    REBOOT = "REBOOT"
    CTA2045_SET_OVERRIDE_STATUS = "CTA2045_SET_OVERRIDE_STATUS"


Simple = ValuesMap[Literal[EventKind.SIMPLE], One[Literal[0, 1, 2, 3]]]
"""
> An indication of the level of a basic demand response signal. Payload
> value is an integer of 0, 1, 2, or 3.
> Note: An example mapping is normal operations, moderate load shed,
> high load shed, and emergency load shed
> -- Definitions, section 10.2, page 17
"""
Price = ValuesMap[Literal[EventKind.PRICE], One[float]]
"""
> The price of energy. Payload value is a float. Units and currency
> defined in associated eventPayloadDescriptor.
"""
Charge = ValuesMap[Literal[EventKind.CHARGE_STATE_SETPOINT], Sequence[AnyValue]]
"""
> The state of charge of an energy storage resource. Payload value is
> indicated by units in associated eventPayloadDescriptor.
> Note: Common units are percentage and kWh
"""
DispatchSetpoint = ValuesMap[Literal[EventKind.DISPATCH_SETPOINT_RELATIVE], One[float]]
"""
> The relative change of consumption by a resource. Payload value is a
> float and is indicated by units in associated eventPayloadDescriptor.
> Note: This is used to dispatch a resource's load
"""
ControlSetpoint = ValuesMap[Literal[EventKind.CONTROL_SETPOINT], Sequence[AnyValue]]
"""
> Resource dependent setting. Payload value type depends on
> application.
"""
ExportPrice = ValuesMap[
    Literal[EventKind.EXPORT_PRICE], Sequence[float]
]  # <-- Q: arity?
"""
> The price of energy exported (usually to the grid). Payload value is
> float and units and currency are defined in associated
> eventPayloadDescriptor.
> Note: Can be used for any form of energy.
"""
GreenhouseGas = ValuesMap[Literal[EventKind.GHG], One[float]]
"""
> An estimate of marginal GreenHouse Gas emissions, in g/kWh.
> Payload value is float.
"""
Curve = ValuesMap[
    Literal[EventKind.CURVE],
    Annotated[Sequence[Point], annotated_types.Len(min_length=1)],
]
"""
> Payload values array contains a series of one or more pairs of floats
> representing a 2D point.
> Note: May be used to represent a curve of values, e.g. VoltVar values.
"""
OptimumLoadShape = ValuesMap[Literal[EventKind.OLS], Sequence[Portion]]
"""
> Optimum Load Shape. Payload values array contains a list of values
> 0.0 to 1.0 representing percentage of usage over the set of intervals in
> the event.
> Note: See ANSI-SCTE 267
"""
ImportCapacitySubscription = ValuesMap[
    Literal[EventKind.IMPORT_CAPACITY_SUBSCRIPTION], One[float]
]
"""
> The amount of import capacity a customer has subscribed to in
> advance. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor.
"""
ImportCapacityReservation = ValuesMap[
    Literal[EventKind.IMPORT_CAPACITY_RESERVATION], One[float]
]
"""
> The amount of additional import capacity that a customer has been
> granted by the VTN. Payload is a float, and meaning is indicated by
> units in associated eventPayloadDescriptor.
"""
ImportCapacityReservationFee = ValuesMap[
    Literal[EventKind.IMPORT_CAPACITY_RESERVATION_FEE], One[float]
]
"""
> The cost per unit of power of extra import capacity available for
> reservation. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor.
"""
ImportCapacityAvailable = ValuesMap[
    Literal[EventKind.IMPORT_CAPACITY_AVAILABLE], One[float]
]
"""
> The amount of extra import capacity available for reservation to the
> customer. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor.
"""

ImportCapacityPrice = ValuesMap[
    Literal[EventKind.IMPORT_CAPACITY_AVAILABLE_PRICE], One[float]
]
"""
> The cost per unit of power of extra import capacity available for
> reservation. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor.
"""
ExportCapacitySubscription = ValuesMap[
    Literal[EventKind.EXPORT_CAPACITY_SUBSCRIPTION], One[float]
]
"""
> The amount of export capacity a customer has subscribed to in
> advance. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor
"""
ExportCapacityReservation = ValuesMap[
    Literal[EventKind.EXPORT_CAPACITY_RESERVATION], One[float]
]
"""
> The amount of additional export capacity that a customer has been
> granted by the VTN. Payload is a float, and meaning is indicated by
> units in associated eventPayloadDescriptor
"""
ExportCapacityReservationFee = ValuesMap[
    Literal[EventKind.EXPORT_CAPACITY_RESERVATION_FEE], One[float]
]
"""
> The cost per unit of power of extra export capacity available for
> reservation. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor
"""
ExportCapacityAvailable = ValuesMap[
    Literal[EventKind.EXPORT_CAPACITY_AVAILABLE], One[float]
]
"""
> The amount of extra export capacity available for reservation to the
> customer. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor.
"""
ImportCapacityLimit = ValuesMap[Literal[EventKind.IMPORT_CAPACITY_LIMIT], One[float]]
"""
> The cost per unit of power of extra export capacity available for
> reservation. Payload is a float, and meaning is indicated by units in
> associated eventPayloadDescriptor
"""
ExportCapacityLimit = ValuesMap[Literal[EventKind.EXPORT_CAPACITY_LIMIT], One[float]]
"""
> The maximum export level for the site. Payload is a float and meaning
> is indicated by units in associated eventPayloadDescriptor
"""
GridEmergencyAlert = ValuesMap[
    Literal[EventKind.ALERT_GRID_EMERGENCY], MaybeOne[NonEmptyStr]
]
"""
> There is an imminent risk of the grid failing to continue supplying
> power to some customers, maintaining operational parameters (e.g.
> voltage), or ceasing to operate at all. Payload value contains a
> human-readable string describing the alert.
"""
BlackStartAlert = ValuesMap[Literal[EventKind.ALERT_BLACK_START], MaybeOne[NonEmptyStr]]
"""
> The grid is in the process of resuming full operation. Devices should
> minimize electricity use until the event is cleared. Payload value
> contains a human-readable string describing the alert.
"""
PossibleOutageAlert = ValuesMap[
    Literal[EventKind.ALERT_POSSIBLE_OUTAGE], MaybeOne[NonEmptyStr]
]
"""
> Customers may lose grid power in the coming hours or days.
> Note: An example of this from California is Public Service Power
> Shutoffs (usually from fire risk). Payload value contains a
> human-readable string describing the alert
"""
FlexAlert = ValuesMap[Literal[EventKind.ALERT_FLEX_ALERT], MaybeOne[NonEmptyStr]]
"""
> Power supply will be scarce during the event. Devices should seek to
> shift load to times before or after the event. Devices that can shed
> should do so during the event. Payload value contains a
> human-readable string describing the alert.
> Note: See: https://flexalert.org
"""
FireAlert = ValuesMap[Literal[EventKind.ALERT_FIRE], MaybeOne[NonEmptyStr]]
"""
> There is a substantial risk of fire in the area which could interrupt
> electricity supply in addition to being a danger to life and property.
> Payload value contains a human-readable string describing the alert.
"""
FreezingAlert = ValuesMap[Literal[EventKind.ALERT_FREEZING], MaybeOne[NonEmptyStr]]
"""
> There is (or is forecast to be) temperatures low enough to be of
> concern. Payload value contains a human-readable string describing
> the alert
"""
WindAlert = ValuesMap[Literal[EventKind.ALERT_WIND], MaybeOne[NonEmptyStr]]
"""
> There is (or is forecast to be) wind speeds high enough to be of
> concern. Includes hurricanes. Payload value contains a
> human-readable string describing the alert.
"""
TsunamiAlert = ValuesMap[Literal[EventKind.ALERT_TSUNAMI], MaybeOne[NonEmptyStr]]
"""
> Tsunami waves expected to hit the coastline. Payload value contains a
> human-readable string describing the alert.
"""
AirQualityAlert = ValuesMap[Literal[EventKind.ALERT_AIR_QUALITY], MaybeOne[NonEmptyStr]]
"""
> Air quality is or is forecast to be. Payload value contains a
> human-readable string describing the alert
"""
OtherAlert = ValuesMap[Literal[EventKind.ALERT_OTHER], MaybeOne[NonEmptyStr]]
"""
No specific definition. See associated text data element. Payload value
contains a human-readable string describing the alert
"""

Reboot = ValuesMap[Literal[EventKind.REBOOT], One[Literal[0, 1]]]  # Q: arity?
"""
> Pass through for resources that support [CTA-2045B]. Payload value 0
> = SOFT, 1 = HARD. See [CTA-2045B] for definitions
"""

OverrideStatus = ValuesMap[
    Literal[EventKind.CTA2045_SET_OVERRIDE_STATUS], One[Literal[0, 1]]  # Q: arity?
]
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

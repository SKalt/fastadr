import annotated_types
from fastapi import APIRouter
from typing import (
    Annotated,
    Any,
    Callable,
    ParamSpec,
    Concatenate,
    NamedTuple,
    Optional,
    TypeVar,
)

from pydantic_core import Url

from .errors import (
    EventNotFound,
    OpenADR3Exception,
    ProgramNotFound,
    ReportNotFound,
    SubscriptionNotFound,
)
from .types.schemata import (
    VEN,
    Event,
    Int32,
    ObjectID,
    ObjectTypes,
    Program,
    Problem,
    Report,
    Resource,
    Subscription,
)

api = APIRouter()

PositiveInt32 = Annotated[Int32, annotated_types.Ge(0)]
"""A positive signed integer. NOT to be confused with an unsigned integer."""

LimitTo50 = Annotated[PositiveInt32, annotated_types.Le(50)]
"""An integer between 0 and 50, inclusive."""


Params = ParamSpec("Params")
Result = TypeVar("Result")
Fn = TypeVar("Fn", bound=Callable[..., Any])
AccessToken = dict[str, list[str]]  # FIXME: define realistic JWT type


def check_auth(
    scopes: list[str],
) -> Callable[
    [Callable[Params, Result]], Callable[Concatenate[AccessToken, Params], Result]
]:
    def decorator(
        fn: Callable[Params, Result],
    ) -> Callable[Concatenate[AccessToken, Params], Result]:
        def ident(
            access_token: AccessToken, /, *args: Params.args, **kwargs: Params.kwargs
        ) -> Any:
            # FIXME: actually check scopes
            # See also: https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/
            # TODO: use fastapi.Depends to do this automatically
            return fn(*args, **kwargs)

        return ident

    return decorator


# TODO: yield JSONResponses whenever a ValidationError or OpenADR3Exception is raised
# from fastapi.responses import JSONResponse
# def _from_problem(problem: _Problem) -> JSONResponse:
#     return JSONResponse(
#         status_code=problem.status,
#         content=problem.model_dump_json(),
#     )


class Backend(NamedTuple):
    programs: dict[str, Program]
    reports: dict[str, Report]
    events: dict[str, Event]
    subscriptions: dict[str, Subscription]
    vens: dict[str, VEN]
    resources: dict[str, dict[str, Resource]]

    def get_program(self, programID: str) -> Program | None:
        return self.programs.get(programID)

    def set_program(self, program: Program) -> None:
        if program.id:
            raise ValueError("Program already has an ID.")  # FIXME: raise a Problem
            # FIXME: understand how ids are owned -- is the api acting as the VTN
            # or the VEN?
        else:
            program.id = str(len(self.programs) + 1)  # TODO: nicer id generation
        self.programs[program.programName] = program

    def delete_program(self, program_id: str) -> Program | None:
        return self.programs.pop(program_id, None)

    def search_programs(
        self,
        *,
        targetValues: list[str],
        targetType: str,
        skip: PositiveInt32,
        limit: Annotated[PositiveInt32, annotated_types.Le(50)],
    ) -> list[Program]:
        results: list[Program] = []
        # TODO: filtering
        for program in self.programs.values():
            if program.programType == targetType:
                ...
            if program.targets or []:
                ...
        return results


DB = Backend(
    programs={}, reports={}, events={}, subscriptions={}, vens={}, resources={}
)


def search_all_programs(
    targetType: str = "",
    targetValues: Optional[list[str]] = None,
    skip: PositiveInt32 = 0,
    limit: LimitTo50 = 50,  # TODO: sensible default value?
    # TODO: implement OAuth2 authentication
    # authorization: Optional[Auth] = None,
) -> list[Program]:
    """
    List all programs known to the server.
    Use skip and pagination query params to limit response size.

    :param targetType: Indicates targeting type, e.g. GROUP
    :param targetValues: List of target values, e.g. group names
    :param skip: Skip this many programs.
    :param limit: Limit the response to this many programs.
    """
    if targetValues is None:
        targetValues = []

    # TODO: actually retrieve programs
    return DB.search_programs(
        targetType=targetType,
        targetValues=targetValues,
        skip=skip,
        limit=limit,
    )


def create_program(program: Program) -> Program:
    """
    Create a new program in the server.
    """
    program.programName
    assert program.id == "", "Program must not have a pre-existing ID."
    DB.set_program(program)  # infallible
    return program


def search_program_by_program_id(programID: ObjectID) -> Program:
    """
    Get a specific program by ID.

    :param programID: ID of the program to retrieve.
    """
    if (program := DB.get_program(programID)) is not None:
        return program
    else:
        raise ProgramNotFound(programID)


def update_program(program: Program, programID: ObjectID) -> Program:
    # some servers might NOT want to allow updating a program's ID:
    # if program.id and program.id != programID:
    #     raise OpenADR3Exception(
    #         Problem(
    #             status=400,
    #             title="Program ID Mismatch",
    #             detail=f"ID in payload ({program.id}) does not match URL: {programID}",
    #             instance=Url("/TODO"),  # FIXME: use a valid URL
    #         )
    #     )
    DB.set_program(program)  # infallible
    return program


def delete_program(programID: ObjectID) -> Program:
    """
    Delete an existing program with the programID in path.
    """
    if (program := DB.delete_program(programID)) is not None:
        return program
    else:
        raise ProgramNotFound(program_id=programID, status=404)


def search_all_reports(
    programID: ObjectID = "",
    clientName: str = "",
    eventID: ObjectID = "",
    skip: PositiveInt32 = 0,
    limit: PositiveInt32 = 50,
) -> list[Report]:
    """
    List all reports known to the server.
    May filter results by programID and clientName as query param.
    Use skip and pagination query params to limit response size.


    """
    # TODO: filter on eventID, too
    results: list[Report] = []
    for report in DB.reports.values():
        if programID and report.programID == programID:
            if skip > 0:
                skip -= 1
                continue
            results.append(report)
            if len(results) >= limit:
                break
        elif clientName and report.clientName == clientName:
            if skip > 0:
                skip -= 1
                continue
            results.append(report)
            if len(results) >= limit:
                break
        elif not clientName and not programID:
            if skip > 0:
                skip -= 1
                continue
            results.append(report)
            if len(results) >= limit:
                break
    return results


def create_report(report: Report) -> Report:
    """Create a new report in the server."""
    if not report.id:
        # make one?
        report.id = str(len(DB.reports) + 1)
        # FIXME: this logic belongs in the database interface
    DB.reports[report.id] = report
    return report


def search_reports_by_report_id(reportID: ObjectID) -> Report:
    """
    Fetch the report specified by the reportID in path.
    """
    if (report := DB.reports.get(reportID)) is not None:
        return report
    else:
        raise ReportNotFound(reportID, status=404)


def update_report(report: Report, reportID: ObjectID) -> Report:
    """
    Update the report specified by the reportID in path.
    """
    # if report.id and report.id != reportID:
    #     raise OpenADR3Exception(
    #         Problem(
    #             status=400,
    #             title="Report ID Mismatch",
    #             detail=f"ID in payload ({report.id}) does not match URL: {reportID}",
    #             instance=Url("/TODO"),  # FIXME: use a valid URL
    #         )
    #     )
    DB.reports[reportID] = report
    return report


def delete_report(reportID: ObjectID) -> Report:
    """
    Delete the program specified by the reportID in path.
    """
    if (report := DB.reports.pop(reportID, None)) is not None:
        return report
    else:
        raise ReportNotFound(reportID, status=404)


def search_all_events(
    programID: Optional[ObjectID] = None,
    targetType: Optional[str] = None,
    targetValues: Optional[list[str]] = None,
    skip: PositiveInt32 = 0,
    limit: LimitTo50 = 50,
) -> list[Event]:
    """
    List all events known to the server. May filter results by programID query param.
    Use skip and pagination query params to limit response size.
    """
    results: list[Event] = []
    DB.events.values()  # FIXME: implement
    return results


def create_event(event: Event) -> Event:
    # HACK: for compatibility reasons, check name unique:
    if event.eventName not in {e.eventName for e in DB.events.values()}:
        raise OpenADR3Exception(
            problem=Problem(
                status=409,
                title="Event name conflict",
                detail=f"An event named {event.eventName} must be unique.",
                instance=Url("/TODO"),
            )
        )
    DB.events[event.id] = event
    return event


def search_events_by_id(eventID: ObjectID) -> Event:
    "Fetch event associated with the eventID in path."
    if (event := DB.events.get(eventID)) is not None:
        return event
    else:
        raise EventNotFound(eventID, status=404)


def update_event(eventID: ObjectID, event: Event) -> Event:
    """Update the event specified by the eventID in path."""
    DB.events[eventID] = event  # FIXME: handle conflicts, id generation, etc
    return event


def delete_event(eventID: ObjectID) -> Event:
    """Delete the event specified by the eventID in path."""
    if (event := DB.events.pop(eventID, None)) is not None:
        return event
    else:
        raise EventNotFound(eventID, status=404)


def register_program_paths():
    # /programs (GET, POST) ####################################################
    api.get(
        "/programs",
        summary="searches all programs",
        operation_id="searchAllPrograms",
        tags=["programs"],
    )(search_all_programs)
    api.post(
        "/programs",
        summary="Create a program",
        operation_id="createProgram",
        tags=["programs"],
        status_code=201,
    )(create_program)

    # /programs/{programID} (GET, PUT, DELETE) #################################
    api.get(
        "/programs/{programID}",
        summary="Get a specific program by ID.",
        operation_id="searchProgramByProgramId",
        tags=["programs"],
    )(search_program_by_program_id)
    api.put(
        "/programs/{programID}",
        summary="Update a program",
        operation_id="updateProgram",
        tags=["programs"],
    )(update_program)
    api.delete(
        "/programs/{programID}",
        summary="delete a program",
        tags=["programs"],
    )(delete_program)


def register_report_paths():
    # /reports (GET, POST) #####################################################
    api.get(
        "/reports",
        tags=["reports"],
        summary="searches all reports",
        operation_id="searchAllReports",
        status_code=201,
    )(search_all_reports)
    api.post(
        "/reports",
        summary="add a report",
        tags=["reports"],
        operation_id="createReport",
    )(create_report)

    # /reports/{reportID} (GET, PUT, DELETE) ###################################
    api.get(
        "/reports/{reportID}",
        summary="searches reports by reportID",
        operation_id="searchReportsByReportID",
        tags=["reports"],
    )(search_reports_by_report_id)
    api.put(
        "/reports/{reportID}",
        summary="update a report",
        operation_id="updateReport",
        tags=["reports"],
    )(update_report)
    api.delete(
        "/reports/{reportID}",
        summary="delete a report",
        operation_id="deleteReport",
        tags=["reports"],
    )(delete_report)


def register_event_paths():
    # /events (GET, POST) ######################################################
    api.get(
        "/events",
        operation_id="searchAllEvents",
        summary="searches all events",
        tags=["events"],
    )(search_all_events)
    api.put(
        "/events",
        summary="searches all events",
        operation_id="createEvent",
        tags=["events"],
    )(create_event)

    # /events/{eventID} (GET, PUT, DELETE) #####################################
    api.get(
        "/events/{eventID}",
        operation_id="searchEventsByID",
        summary="search events by ID",
        tags=["events"],
    )(search_events_by_id)
    api.put(
        "/events/{eventID}",
        summary="update an event",
        operation_id="updateEvent",
        tags=["events"],
        status_code=201,
    )(update_event)
    api.delete(
        "/events/{eventID}",
        summary="delete an event",
        operation_id="deleteEvent",
        tags=["events"],
    )(delete_event)


def search_subscriptions(
    programID: ObjectID,
    clientName: str,
    targetType: str,
    targetValues: list[str],
    objects: list[ObjectTypes],
    skip: PositiveInt32,
    limit: PositiveInt32,
) -> list[Subscription]:
    """
    List all subscriptions.
    May filter results by programID and clientID as query params.
    May filter results by objects as query param. See objectTypes schema.
    Use skip and pagination query params to limit response size.
    """
    results: list[Subscription] = []
    for sub in DB.subscriptions.values():
        if programID and sub.programID == programID:
            if skip > 0:
                skip -= 1
                continue
            results.append(sub)
        elif clientName and sub.clientName == clientName:
            if skip > 0:
                skip -= 1
                continue
            results.append(sub)
        elif not clientName and not programID:
            if skip > 0:
                skip -= 1
                continue
            results.append(sub)
        else:
            continue

        if len(results) >= limit:
            break
    return results


def create_subscription(subscription: Subscription) -> Subscription:
    """Create a new subscription in the server."""
    if not subscription.id:
        # make one?
        subscription.id = str(len(DB.subscriptions) + 1)
    DB.subscriptions[subscription.id] = subscription
    return subscription


def search_subscription_by_id(subscriptionID: ObjectID) -> Subscription:
    """
    Return the subscription specified by subscriptionID specified in path.
    """
    if (sub := DB.subscriptions.get(subscriptionID)) is not None:
        return sub
    else:
        raise SubscriptionNotFound(subscriptionID, status=404)


def update_subscription(subscriptionID: ObjectID, subscription: Subscription) -> None:
    """
    Update the subscription specified by subscriptionID specified in path.
    """
    DB.subscriptions[subscriptionID] = (
        subscription  # FIXME: handle conflicts, id generation, etc
    )


def delete_subscription(subscriptionID: ObjectID) -> Subscription:
    if (sub := DB.subscriptions.pop(subscriptionID, None)) is not None:
        return sub
    else:
        raise SubscriptionNotFound(subscriptionID, status=404)


def register_subscription_paths():
    # /subscriptions (GET, POST): ##############################################
    api.get(
        "/subscriptions",
        summary="search subscriptions",
        operation_id="searchSubscriptions",
        tags=["subscriptions"],
    )(search_subscriptions)
    api.post(
        "/subscriptions",
        summary="create subscription",
        operation_id="createSubscription",
        tags=["subscriptions"],
        status_code=201,
    )(create_subscription)

    # /subscriptions/{subscriptionID} (GET, PUT, DELETE): ######################
    api.get(
        "/subscriptions/{subscriptionID}",
        operation_id="searchSubscriptionByID",
        summary="search subscriptions by ID",
        tags=["subscriptions"],
    )(search_subscription_by_id)
    api.put(
        "/subscriptions/{subscriptionID}",
        operation_id="updateSubscription",
        summary="update subscription",
        tags=["subscriptions"],
    )(update_subscription)
    api.delete(
        "/subscriptions/{subscriptionID}",
        operation_id="deleteSubscription",
        summary="delete subscription",
        tags=["subscriptions"],
    )(delete_subscription)


def search_vens(
    skip: PositiveInt32,
    targetType: Optional[str],
    venName: Optional[str],
    targetValues: Optional[list[str]],
    limit: Optional[LimitTo50] = None,
) -> list[VEN]:
    """
    List all vens.
    Use skip and pagination query params to limit response size.

    """
    results: list[VEN] = []
    # TODO: implement filtering
    # DB.vens.values()
    return results


def create_ven(ven: VEN) -> VEN:
    """Create a new ven in the server."""
    if not ven.id:
        # make one?
        ven.id = str(len(DB.vens) + 1)
    DB.vens[ven.id] = ven
    DB.resources[ven.id] = {}
    return ven


def search_ven_by_id(venID: ObjectID) -> VEN:
    """
    Return the ven specified by venID specified in path.
    """
    if (ven := DB.vens.get(venID)) is not None:
        return ven
    else:
        raise VenNotFound(venID, status=404)


def update_ven(venID: ObjectID, ven: VEN) -> VEN:
    """
    Update the ven specified by venID specified in path.
    """
    if not ven.id:
        ven.id = venID
    elif ven.id != venID:
        pass  # TODO: handle conflicts

    DB.vens[venID] = ven  # FIXME: handle conflicts, id generation, etc
    return ven


def delete_ven(venID: ObjectID) -> VEN:
    """
    Delete the ven specified by venID specified in path.
    """
    if (ven := DB.vens.pop(venID, None)) is not None:
        DB.resources.pop(venID, None)  # delete all associated resources
        return ven
    else:
        raise VenNotFound(venID, status=404)


def search_ven_resources(
    venID: ObjectID,
    resourceName: Optional[str],
    targetType: Optional[str],
    targetValues: Optional[list[str]],
    skip: Optional[PositiveInt32],
    limit: LimitTo50,  # FIXME: what's `style: form` in FastAPI?
) -> list[Resource]:
    """
    Return the ven resources specified by venID specified in path.
    """
    if (resources := DB.resources.get(venID)) is not None:
        return [*resources.values()]  # TODO: actually filter resources
    else:
        raise VenNotFound(venID, status=404)
    ...  # TODO: implement


def create_resource(venID: ObjectID, resource: Resource) -> Resource:
    """Create a new resource"""
    if (resources := DB.resources.get(venID)) is None:
        raise VenNotFound(venID, status=404)
    if not resource.id:
        # make one? # FIXME: make unique
        resource.id = str(len(DB.resources[venID]) + 1)
    # FIXME: check for conflicts on resource.id
    resources[resource.id] = resource  # persist the resource
    return resource


def search_ven_resource_by_id(venID: ObjectID, resourceID: ObjectID) -> Resource:
    """
    Return the ven resource specified by venID and resourceID specified in path.
    """
    if (resources := DB.resources.get(venID)) is None:
        raise VenNotFound(venID, status=404)
    if (resource := resources.get(resourceID)) is not None:
        return resource
    else:
        raise VenNotFound(venID, status=404)


def delete_ven_resource(venID: ObjectID, resourceID: ObjectID) -> Resource:
    """
    Delete the ven resource specified by venID and resourceID specified in path.
    """
    if (resources := DB.resources.get(venID)) is None:
        raise VenNotFound(venID, status=404)
    if (resource := resources.pop(resourceID, None)) is not None:
        return resource
    else:
        raise VenNotFound(venID, status=404)


def register_ven_paths():
    # /vens: (GET, POST) #######################################################
    api.get("/vens", operation_id="searchVens", summary="search vens", tags=["vens"])(
        search_vens
    )
    api.post("/vens", operation_id="createVen", summary="create ven", tags=["vens"])(
        create_ven
    )

    # /vens/{venID} (GET, PUT, DELETE): ########################################
    api.get(
        "/vens/{venID}",
        operation_id="searchVenByID",
        summary="search vens by ID",
        tags=["vens"],
    )(search_ven_by_id)
    api.put(
        "/vens/{venID}", operation_id="updateVen", summary="update VEN", tags=["vens"]
    )(update_ven)
    api.delete(
        "/vens/{venID}",
        operation_id="deleteVen",
        summary="delete a specific VEN",
        tags=["vens"],
    )(delete_ven)

    # /vens/{venID}/resources (GET, POST): #####################################
    api.get(
        "/vens/{venID}/resources",
        operation_id="searchVenResources",
        summary="",
        tags=["vens"],
    )(search_ven_resources)
    api.post(
        "/vens/{venID}/resources",
        operation_id="createResource",
        summary="",
        tags=["vens"],
    )(create_resource)

    # /vens/{venID}/resources/{resourceID} (GET, PUT, DELETE): #################
    api.get(
        "/vens/{venID}/resources/{resourceID}",
        operation_id="searchVenResourceByID",
        summary="search VEN resources by ID",
        tags=["vens"],
    )(search_ven_resource_by_id)
    api.put(
        "/vens/{venID}/resources/{resourceID}",
        operation_id="updateVenResource",
        summary="update VEN resource",
        tags=["vens"],
        status_code=201,
    )(create_resource)
    api.delete(
        "/vens/{venID}/resources/{resourceID}",
        operation_id="deleteVenResource",
        summary="delete VEN resource",
        tags=["vens"],
    )(delete_ven_resource)


def fetch_token(identity: str) -> str:
    """
    Return an access token based on clientID and clientSecret.
    """
    return "password123"  # FIXME: implement


def register_paths():
    register_program_paths()
    register_report_paths()
    register_event_paths()
    register_ven_paths()
    # TODO: don't include OAuth2 **access server** functionality in the **resource server**
    api.post("/auth/token", operation_id="fetchToken", summary="fetch an access token")(
        fetch_token
    )

from .types.schemata import Problem, HTTPStatusCode, Url


class OpenADR3Exception(Exception):
    def __init__(self, problem: Problem) -> None:
        self.problem = problem
        super().__init__(problem.detail)


class ProgramNotFound(OpenADR3Exception):
    def __init__(self, program_id: str, status: HTTPStatusCode = 404) -> None:
        super().__init__(
            Problem(
                status=status,
                title="Program Not Found",
                detail=f"Program with ID {program_id} not found.",
                instance=Url("/TODO"),  # FIXME: use a valid URL
            )
        )


class EventNotFound(OpenADR3Exception):
    def __init__(self, event_id: str, status: HTTPStatusCode = 404) -> None:
        super().__init__(
            Problem(
                status=status,
                title="Event Not Found",
                detail=f"Event with ID {event_id} not found.",
                instance=Url("/TODO"),  # FIXME: use a valid URL
            )
        )


# TODO: class Conflict(OpenADR3Exception):?


class ReportNotFound(OpenADR3Exception):
    def __init__(self, report_id: str, status: HTTPStatusCode = 404) -> None:
        super().__init__(
            Problem(
                status=status,
                title="Report Not Found",
                detail=f"Report with ID {report_id} not found.",
                instance=Url("/TODO"),  # FIXME: use a valid URL
            )
        )


class SubscriptionNotFound(OpenADR3Exception):
    def __init__(self, subscription_id: str, status: HTTPStatusCode = 404) -> None:
        super().__init__(
            Problem(
                status=status,
                title="Subscription Not Found",
                detail=f"Subscription with ID {subscription_id} not found.",
                instance=Url("/TODO"),  # FIXME: use a valid URL
            )
        )


class VenNotFound(OpenADR3Exception):
    def __init__(self, ven_id: str, status: HTTPStatusCode = 404) -> None:
        super().__init__(
            Problem(
                status=status,
                title="VEN Not Found",
                detail=f"VEN with ID {ven_id} not found.",
                instance=Url("/TODO"),  # FIXME: use a valid URL
            )
        )

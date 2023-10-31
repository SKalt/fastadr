import json
from pathlib import Path
import yaml
from pydantic import TypeAdapter, ValidationError
from pydantic_core import Url
import pytest
from typing import Any, Protocol
from src.schemata import (
    Duration,
    DateTime,
    ObjectID,
    Percent,
    IntervalPeriod,
    ProgramDescription,
    VEN,
    Program,
    Report,
    Event,
    Subscription,
    Resource,
    Interval,
    ValuesMap,
    Point,
    EventPayloadDescriptor,
    ReportPayloadDescriptor,
    ReportDescriptor,
    Notification,
    # ObjectTypes: not testing enum
    # Problem: not testing since the server will only ever send it, not receive it
)


_this_dir = Path(__file__).parent
REPO_ROOT = _this_dir.parent
FIXTURES_DIR = Path(__file__).parent / "examples"


def get_json(file: Path) -> str:
    """Load a YAML file, then dump it as JSON"""
    with open(file) as f:
        return json.dumps(yaml.safe_load(f))


class Validator(Protocol):
    def model_validate_json(self, json_data: str | bytes) -> Any:
        ...


def _check_valid_document(model: Validator, file: Path):
    try:
        model.model_validate_json(get_json(file))
    except ValidationError as e:
        e.add_note(f"file: {file.relative_to(REPO_ROOT)}")
        raise e


# note: I'm using a custom check instead of pydantic.raises(ValidationError) in order to
# ensure that the file name is included in the error message
def _check_invalid(model: Validator, file: Path):
    try:
        model.model_validate_json(get_json(file))
        assert False, f"expected {file.relative_to(REPO_ROOT)} to be invalid"
    except ValidationError:
        pass  # expected


def _get_examples(example_dir: Path, *, ok: bool) -> list[Path]:
    d = example_dir / ("valid" if ok else "invalid")
    assert d.exists() and d.is_dir()
    examples = [f for f in d.glob("*.yaml")]
    assert len(examples) > 0
    return examples


def _get_valid_examples(example_dir: Path) -> list[Path]:
    return _get_examples(example_dir, ok=True)


def _get_invalid_examples(example_dir: Path) -> list[Path]:
    return _get_examples(example_dir, ok=False)


_DurationValidator = TypeAdapter(Duration)


@pytest.mark.parametrize(
    "iso_8601_duration",
    [
        "PT1H",
    ],
)
def test_duration(iso_8601_duration: str):
    assert _DurationValidator.json_schema() == {"format": "duration", "type": "string"}
    _DurationValidator.validate_json('"' + iso_8601_duration + '"')


@pytest.mark.parametrize(
    "iso_8601_interval",
    [
        "2007-03-01T13:00:00Z/2008-05-11T15:30:00Z",
        "2007-03-01T13:00:00Z/P1Y2M10DT2H30M",
        "P1Y2M10DT2H30M/2008-05-11T15:30:00Z",
    ],
)
def test_duration_does_not_accept_iso8601_intervals(iso_8601_interval: str):
    with pytest.raises(ValidationError):
        _DurationValidator.validate_json('"' + iso_8601_interval + '"')


def test_ints_not_accepted_as_duration():
    with pytest.raises(ValidationError):
        _DurationValidator.validate_json("1.0")


def test_datetime():
    validator = TypeAdapter(DateTime)
    validator.validate_json('"2021-01-01T00:00:00Z"')
    with pytest.raises(ValidationError):
        # Datetime shouldn't accept integers
        validator.validate_json("0")


def test_object_id():
    validator = TypeAdapter(ObjectID)
    validator.validate_json('"snake_case"')
    validator.validate_json('"camelCase"')
    validator.validate_json('"PascalCase"')
    validator.validate_json('"kebab-case"')
    validator.validate_json('"UPPERCASE"')
    validator.validate_json('"lowercase"')
    validator.validate_json('"number_1"')
    with pytest.raises(ValidationError):
        # must be at least 1 character long
        validator.validate_json('""')
    with pytest.raises(ValidationError):
        # must be less than 128 characters long
        validator.validate_json('"' + "a" * 129 + '"')
    with pytest.raises(ValidationError):
        # ObjectID shouldn't accept spaces
        validator.validate_json('"no way"')
    with pytest.raises(ValidationError):
        # ObjectID shouldn't accept punctuation
        validator.validate_json("nope!")
    with pytest.raises(ValidationError):
        # ObjectID shouldn't accept punctuation
        validator.validate_json('"nope!"')
    with pytest.raises(ValidationError):
        # ObjectID shouldn't accept integers
        validator.validate_json("0")


def test_percent():
    validator = TypeAdapter(Percent)
    validator.validate_json("0")
    validator.validate_json("50")
    validator.validate_json("100")
    with pytest.raises(ValidationError):
        # Percent shouldn't accept strings
        validator.validate_json('"50"')
    with pytest.raises(ValidationError):
        # Percent shouldn't accept floats(???)
        validator.validate_json("50.0")


def test_program_description():
    ProgramDescription(URL=Url("https://example.com"))
    with pytest.raises(ValidationError):
        # ProgramDescription shouldn't accept malformed, scheme-less urls
        ProgramDescription.model_validate_json('{"URL": "example.com"}')
    with pytest.raises(ValidationError):
        # ProgramDescription shouldn't accept lower-case "url" keys
        ProgramDescription.model_validate_json('{"url": "https://example.com"}')
    assert ProgramDescription.model_json_schema() == {
        "required": ["URL"],
        "title": "ProgramDescription",
        "type": "object",
        "properties": {
            "URL": {
                "format": "uri",
                "type": "string",
                "minLength": 1,
                "title": "Url",
            }
        },
    }


def test_interval_period():
    # valid: just a start time
    start = DateTime(year=2049, month=3, day=1, hour=0)
    IntervalPeriod(start=start)
    IntervalPeriod(
        start=DateTime(year=2049, month=3, day=1, hour=0),
        duration=Duration(hours=1),
        randomizeStart=None,
    )
    IntervalPeriod(
        start=DateTime(year=2049, month=3, day=1, hour=0),
        duration=None,
        randomizeStart=Duration(hours=1),
    )
    IntervalPeriod(
        start=DateTime(year=2049, month=3, day=1, hour=0),
        duration=Duration(hours=1),
        randomizeStart=Duration(hours=1),
    )


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "ven"))
def test_valid_ven(f: Path):
    _check_valid_document(VEN, f)


@pytest.mark.parametrize("f", _get_invalid_examples(FIXTURES_DIR / "ven"))
def test_invalid_ven(f: Path):
    _check_invalid(VEN, f)


def test_weird_ven():
    # weird-yet-valid cases:
    VEN(objectType="VEN")  # all defaults -- many of which are surprisingly null/None
    VEN(venName=None, objectType="VEN")  # - venName is required, but can be null/None
    VEN(venName="", objectType="VEN")  # - venName is required, but can be empty string


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "program"))
def test_valid_program(f: Path):
    _check_valid_document(Program, f)


@pytest.mark.parametrize("f", _get_invalid_examples(FIXTURES_DIR / "program"))
def test_invalid_program(f: Path):
    _check_invalid(Program, f)


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "report"))
def test_report(f: Path):
    _check_valid_document(Report, f)


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "event"))
def test_valid_event(f: Path):
    _check_valid_document(Event, f)


# TODO: generate interesting invalid event examples
# @pytest.mark.parametrize("f", get_invalid_examples(FIXTURES_DIR / "event"))
# def test_invalid_event(f: Path):
#     check_invalid(Event, f)


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "subscription"))
def test_valid_subscription(f: Path):
    _check_valid_document(Subscription, f)


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "resource"))
def test_valid_resource(f: Path):
    _check_valid_document(Resource, f)


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "interval"))
def test_valid_interval(f: Path):
    _check_valid_document(Interval, f)


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "valuesMap"))
def test_valid_valuesMap(f: Path):
    _check_valid_document(ValuesMap, f)


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "point"))
def test_valid_point(f: Path):
    _check_valid_document(Point, f)


@pytest.mark.parametrize(
    "f", _get_valid_examples(FIXTURES_DIR / "eventPayloadDescriptor")
)
def test_valid_eventPayloadDescriptor(f: Path):
    _check_valid_document(EventPayloadDescriptor, f)


@pytest.mark.parametrize(
    "f", _get_valid_examples(FIXTURES_DIR / "reportPayloadDescriptor")
)
def test_valid_reportPayloadDescriptor(f: Path):
    _check_valid_document(ReportPayloadDescriptor, f)


@pytest.mark.parametrize(
    "f", _get_invalid_examples(FIXTURES_DIR / "reportPayloadDescriptor")
)
def test_invalid_reportPayloadDescriptor(f: Path):
    _check_invalid(ReportPayloadDescriptor, f)


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "reportDescriptor"))
def test_valid_reportDescriptor(f: Path):
    _check_valid_document(ReportDescriptor, f)


@pytest.mark.parametrize("f", _get_valid_examples(FIXTURES_DIR / "notification"))
def test_valid_notification(f: Path):
    _check_valid_document(Notification, f)


@pytest.mark.parametrize("f", _get_invalid_examples(FIXTURES_DIR / "notification"))
def test_invalid_notification(f: Path):
    _check_invalid(Notification, f)

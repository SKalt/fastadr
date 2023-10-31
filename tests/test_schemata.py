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
from datetime import timedelta


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


def check_valid(model: Validator, file: Path):
    try:
        model.model_validate_json(get_json(file))
    except ValidationError as e:
        e.add_note(f"file: {file.relative_to(REPO_ROOT)}")
        raise e


# note: I'm using a custom check instead of pydantic.raises(ValidationError) in order to
# ensure that the file name is included in the error message
def check_invalid(model: Validator, file: Path):
    try:
        model.model_validate_json(get_json(file))
        assert False, f"expected {file.relative_to(REPO_ROOT)} to be invalid"
    except ValidationError:
        pass  # expected


def get_examples(example_dir: Path, *, ok: bool) -> list[Path]:
    d = example_dir / ("valid" if ok else "invalid")
    assert d.exists() and d.is_dir()
    examples = [f for f in d.glob("*.yaml")]
    assert len(examples) > 0
    return examples


def get_valid_examples(example_dir: Path) -> list[Path]:
    return get_examples(example_dir, ok=True)


def get_invalid_examples(example_dir: Path) -> list[Path]:
    return get_examples(example_dir, ok=False)


def test_duration():
    validator = TypeAdapter(Duration)
    assert validator.json_schema() == {"format": "duration", "type": "string"}
    val = validator.validate_json('"PT1H"')
    assert val == timedelta(hours=1)
    with pytest.raises(ValidationError):
        # Duration shouldn't accept integers
        # FIXME: nicer error message specifying ISO-8601 format
        validator.validate_json("3600")


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


def test_ven():
    examples_dir = FIXTURES_DIR / "VEN"
    assert examples_dir.exists() and examples_dir.is_dir()
    valid_examples = [f for f in (examples_dir / "valid").glob("*.yaml")]
    assert len(valid_examples)
    for f in valid_examples:
        try:
            VEN.model_validate_json(get_json(f))
        except ValidationError as e:
            e.add_note(f"file: {f.relative_to(REPO_ROOT)}")
            raise e
    # weird-yet-valid cases:
    VEN(objectType="VEN")  # all defaults -- many of which are surprisingly null/None
    VEN(venName=None, objectType="VEN")  # - venName is required, but can be null/None
    VEN(venName="", objectType="VEN")  # - venName is required, but can be empty string
    invalid_examples = [f for f in (examples_dir / "invalid").glob("*.yaml")]
    assert len(invalid_examples) > 0
    for f in invalid_examples:
        with pytest.raises(ValidationError):
            VEN.model_validate_json(get_json(f))


program_examples_dir = FIXTURES_DIR / "program"


@pytest.mark.parametrize("f", get_valid_examples(program_examples_dir))
def test_valid_program(f: Path):
    check_valid(Program, f)


@pytest.mark.parametrize("f", get_invalid_examples(program_examples_dir))
def test_invalid_program(f: Path):
    check_invalid(Program, f)


@pytest.mark.parametrize("f", get_valid_examples(FIXTURES_DIR / "report"))
def test_report(f: Path):
    check_valid(Report, f)


@pytest.mark.parametrize("f", get_valid_examples(FIXTURES_DIR / "event"))
def test_valid_event(f: Path):
    check_valid(Event, f)


# @pytest.mark.parametrize("f", get_invalid_examples(FIXTURES_DIR / "event"))
# def test_invalid_event(f: Path):
#     check_invalid(Event, f)


@pytest.mark.parametrize("f", get_valid_examples(FIXTURES_DIR / "subscription"))
def test_valid_subscription(f: Path):
    check_valid(Subscription, f)


@pytest.mark.parametrize("f", get_valid_examples(FIXTURES_DIR / "resource"))
def test_valid_resource(f: Path):
    check_valid(Resource, f)


@pytest.mark.parametrize("f", get_valid_examples(FIXTURES_DIR / "interval"))
def test_valid_interval(f: Path):
    check_valid(Interval, f)


@pytest.mark.parametrize("f", get_valid_examples(FIXTURES_DIR / "valuesMap"))
def test_valid_valuesMap(f: Path):
    check_valid(ValuesMap, f)


@pytest.mark.parametrize("f", get_valid_examples(FIXTURES_DIR / "point"))
def test_valid_point(f: Path):
    check_valid(Point, f)


@pytest.mark.parametrize(
    "f", get_valid_examples(FIXTURES_DIR / "eventPayloadDescriptor")
)
def test_valid_eventPayloadDescriptor(f: Path):
    check_valid(EventPayloadDescriptor, f)


@pytest.mark.parametrize(
    "f", get_valid_examples(FIXTURES_DIR / "reportPayloadDescriptor")
)
def test_valid_reportPayloadDescriptor(f: Path):
    check_valid(ReportPayloadDescriptor, f)


@pytest.mark.parametrize(
    "f", get_invalid_examples(FIXTURES_DIR / "reportPayloadDescriptor")
)
def test_invalid_reportPayloadDescriptor(f: Path):
    check_invalid(ReportPayloadDescriptor, f)


@pytest.mark.parametrize("f", get_valid_examples(FIXTURES_DIR / "reportDescriptor"))
def test_valid_reportDescriptor(f: Path):
    check_valid(ReportDescriptor, f)


@pytest.mark.parametrize("f", get_valid_examples(FIXTURES_DIR / "notification"))
def test_valid_notification(f: Path):
    check_valid(Notification, f)


@pytest.mark.parametrize("f", get_invalid_examples(FIXTURES_DIR / "notification"))
def test_invalid_notification(f: Path):
    check_invalid(Notification, f)

import json
from pathlib import Path
from yaml import safe_load
from pydantic import TypeAdapter, ValidationError
from pydantic_core import Url
import pytest
from src.schemata import (
    Duration,
    DateTime,
    ObjectID,
    Percent,
    IntervalPeriod,
    ProgramDescription,
    VEN,
    # Program
    # Report
    # Event
    # Subscription
    # Resource
    # Interval
    # ValuesMap
    # Point
    # EventPayloadDescriptor
    # ReportPayloadDescriptor
    # ReportDescriptor
    # ObjectID
    # Notification
    # ObjectTypes
    # DateTime
    # Duration
    # Problem
)
from datetime import timedelta

FIXTURES_DIR = Path(__file__).parent / "fixtures"


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
    ven_examples_dir = FIXTURES_DIR / "VEN"
    for i in (ven_examples_dir / "valid").glob("*.yaml"):
        doc = json.dumps(safe_load(i.read_text()))  # strip comments
        VEN.model_validate_json(doc)
    # weird-yet valid cases:
    VEN(objectType="VEN")  # all defaults -- many of which are surprisingly null/None
    VEN(venName=None, objectType="VEN")  # - venName is required, but can be null/None
    VEN(venName="", objectType="VEN")    # - venName is required, but can be empty string
    for i in (ven_examples_dir / "invalid").glob("*.yaml"):
        with pytest.raises(ValidationError):
            doc = json.dumps(safe_load(i.read_text()))  # strip comments
            VEN.model_validate_json(doc)

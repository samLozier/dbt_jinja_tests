"""Test fixtures for use with manifest.json validation."""
import json
import typing
from pathlib import Path

import pytest


@pytest.fixture
def manifest_json() -> typing.Any:
    """Loads the full manifest json from  jaffleshop for use in tests."""
    return json.loads(Path(Path(__file__).parent / "manifest.json").read_text())


@pytest.fixture
def single_dbt_model_json(manifest_json: dict) -> typing.Any:  # type: ignore [type-arg]
    """Returns a single model from the broader set contained in manifest.json."""
    keys = list(manifest_json["nodes"].keys())
    return manifest_json["nodes"][keys[0]]

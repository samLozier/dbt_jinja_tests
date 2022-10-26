"""Test fixtures for use with manifest.json validation."""
import json
from pathlib import Path

import pytest


@pytest.fixture
def manifest_json() -> dict[str, dict]:
    """Loads the full manifest json from  jaffleshop for use in tests."""
    return json.loads(Path(Path(__file__).parent / "manifest.json").read_text())


@pytest.fixture
def single_dbt_model_json(manifest_json: dict) -> dict[str, dict]:
    """Returns a single model from the broader set contained in manifest.json."""
    keys = list(manifest_json["nodes"].keys())
    return manifest_json["nodes"][keys[0]]

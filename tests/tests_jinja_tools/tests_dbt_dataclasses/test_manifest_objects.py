"""Tests around the validation of manifest.json."""
from src.dbt_jinja_tests.jinja_tools.dbt_dataclasses.model_config import DbtModel


def test_load_manifest_json(single_dbt_model_json: dict) -> None:
    """Basic smoke test for the maifest loaders."""
    dbt_obj = DbtModel(**single_dbt_model_json)
    assert dbt_obj.columns

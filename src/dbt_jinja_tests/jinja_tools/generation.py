"""Load and validate and parse a manifest.json file."""
import json
from pathlib import Path

from .dbt_dataclasses.model_config import DbtModel
from .dbt_dataclasses.model_config import ModelType


class ManifestHandler:
    """Basic class for loading, validating and parsing a manifest file."""

    def __int__(
        self,
        manifest_path: Path,
    ) -> None:
        """Loads and validates a manifest file."""
        self.manifest_path = manifest_path
        if self.manifest_path.exists() or self.manifest_path.suffix != ".json":
            raise ValueError(
                "manifest_path error. Was an existing manifest.json path supplied?"
            )
        self.raw_manifest = self._read_json(self.manifest_path)

    @staticmethod
    def _read_json(json_path: Path) -> dict[any]:
        return json.loads(json_path.read_text())

    def load_models(self) -> dict[str, DbtModel]:
        """Loads the manifest nodes as individual pydnatic validated models."""
        models = {}
        for node_name, node_vals in self.raw_manifest.get("nodes", {}).items():
            model = {
                node_name: DbtModel(
                    compiled=node_vals["compiled"],
                    resource_type=ModelType(node_vals["resource_type"]),
                )
            }
            models.update(model)
        return models

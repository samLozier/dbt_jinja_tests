from pathlib import Path
import json
from .dbt_dataclasses.model_config import (
    DbtModel,
    DbtColumn,
    SqlFilePath,
    RootPath,
    ModelType,
)


class ManifestHandler:
    def __int__(
        self,
        manifest_path: Path,
    ):
        self.manifest_path = manifest_path
        if self.manifest_path.exists() or self.manifest_path.suffix != ".json":
            raise ValueError(
                f"manifest_path error. Was an existing manifest.json path supplied?"
            )
        self.raw_manifest = self._read_json(self.manifest_path)

    @staticmethod
    def _read_json(json_path: Path) -> str:
        return json.loads(json_path.read_text())

    def load_models(self) -> list[DbtModel]:
        models = {}
        for node_name, node_vals in self.raw_manifest.get("nodes", {}).items():
            model = {
                node_name: DbtModel(
                    compiled=node_vals["compiled"],
                    resource_type=ModelType(node_vals["resource_type"]),
                )
            }

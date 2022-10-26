"""Pydnatic models, dtypes, and dataclasses to load manifest.json files."""
from enum import Enum
from pathlib import Path
from typing import Dict
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import validator


class ModelType(str, Enum):
    """Basic Dataclass that contains valid dbtmaterialization targets."""

    model = "model"
    view = "view"
    incremental = "incremental"


def filepath_validator(filepath: Path) -> Path:
    """Runs several tests against paths supplied from the manfiest.

    Is the file valid, it exists?
    Could be expanded to check the overlap with the cwd.
    """
    if not filepath.is_file() and filepath.exists() and filepath.suffix == ".sql":
        raise ValueError
    return filepath


def folder_path_validator(folderpath: Path) -> Path:
    """Basic Validator to check validity of folder paths."""
    if not folderpath.is_dir() or not folderpath.exists():
        raise ValueError
    return folderpath


# class ColumnDatatype(Enum):
#     pass


class DbtColumn(BaseModel):
    """Nested dbt column spec.

    Once types are qualified in the Column Datatype, switch to
    that for the enum purpose.
    """

    name: str
    description: str
    meta: dict  # type: ignore[type-arg]
    data_type: Union[str, None]  # Optional[ColumnDatatype]
    quote: Optional[str]


class DbtColumnDict(BaseModel):
    """The Column dict as supplied by manifest.json."""

    columns: Union[None, Dict[str, DbtColumn]]


class DbtModel(BaseModel):
    """The types for the base object from manifest.json.

    Includes validators for path rows.
    """

    compiled: bool
    resource_type: ModelType
    depends_on: dict  # type: ignore[type-arg]
    unique_id: str
    root_path: Path
    path: Path
    original_file_path: Path
    name: str
    alias: str
    refs: list[Optional[list[str]]]
    sources: list[str]
    columns: Union[None, dict[str, DbtColumn]]

    @validator("path")
    def path_validate(cls, v: Path) -> Path:  # noqa
        """Validate filepath."""
        return filepath_validator(v)

    @validator("original_file_path")
    def original_file_path_validate(cls, v: Path) -> Path:  # noqa
        """Validate OG file path."""
        return filepath_validator(v)

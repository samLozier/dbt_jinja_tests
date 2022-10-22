from enum import Enum
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


class ModelType(Enum):
    MODEL = 'model'
    VIEW = 'view'
    INCREMENTAL = 'incremental'


@dataclass
class BasePathCls:

    path: Path

    def __int__(self, path: [Path, str]):
        if isinstance(path, Path):
            self.path = path
        else:
            self.path = Path(path)
        if not self.path.exists():
            raise ValueError


@dataclass
class RootPath(BasePathCls):
    root_path: Path

    def __init__(self, base_path: [Path, str]):
        super(base_path).__init__()
        self.base_path = self.path
        if not self.base_path.is_dir():
            raise ValueError


@dataclass
class SqlFilePath(BasePathCls):
    file_path: Path

    def __init__(self, file_path: [Path, str]):
        super(file_path).__init__()
        self.file_path = self.path
        if (
            not self.file_path.is_file()
            and self.file_path.exists()
            and self.file_path.suffix == ".sql"
        ):
            raise ValueError


class ColumnDatatype(Enum):
    pass


@dataclass
class DbtColumn:
    name: str
    description: str
    meta: dict
    data_type: str  # Optional[ColumnDatatype]
    quote: Optional[str]


@dataclass
class DbtModel:
    compiled: bool
    resource_type: ModelType
    depends_on: dict
    unique_id: str
    root_path: RootPath
    path: SqlFilePath
    original_file_path: SqlFilePath
    name: str
    alias: str
    refs: [str]
    sources: [str]
    columns: dict[str:DbtColumn]

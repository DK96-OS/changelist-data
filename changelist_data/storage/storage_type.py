""" The Options for Changelists data Storage.
"""
from enum import Enum
from pathlib import Path


class StorageType(Enum):
    CHANGELISTS = "changelists"
    WORKSPACE = "workspace"


CHANGELISTS_FILE_PATH_STR = '.changelists/data.xml'
WORKSPACE_FILE_PATH_STR = '.idea/workspace.xml'


def get_default_file(storage_type: StorageType) -> str:
    if storage_type == StorageType.CHANGELISTS:
        return CHANGELISTS_FILE_PATH_STR
    if storage_type == StorageType.WORKSPACE:
        return WORKSPACE_FILE_PATH_STR
    # Add New Enums Here:
    raise ValueError(f"Invalid Argument: {storage_type}")


def get_default_path(storage_type: StorageType) -> Path:
    return Path(get_default_file(storage_type))

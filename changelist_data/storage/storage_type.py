""" The Options for Changelists data Storage.
"""
from enum import Enum
from pathlib import Path


class StorageType(Enum):
    CHANGELISTS = "changelists"
    WORKSPACE = "workspace"


CHANGELISTS_FILE_PATH_STR = '.changelists/data.xml'
WORKSPACE_FILE_PATH_STR = '.idea/workspace.xml'


def get_default_path(storage_type: StorageType) -> Path:
    if storage_type == StorageType.CHANGELISTS:
        return Path(CHANGELISTS_FILE_PATH_STR)
    if storage_type == StorageType.WORKSPACE:
        return Path(WORKSPACE_FILE_PATH_STR)
    # Add New Enums Here:
    raise ValueError(f"Invalid Argument: {storage_type}")

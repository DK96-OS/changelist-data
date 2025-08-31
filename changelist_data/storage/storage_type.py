""" The Options for Changelists data Storage.
"""
from enum import Enum
from pathlib import Path


class StorageType(Enum):
    """ The Type of Storage File to be used by Changelists.
    """
    CHANGELISTS = "changelists"
    WORKSPACE = "workspace"


CHANGELISTS_FILE_PATH_STR = '.changelists/data.xml'
WORKSPACE_FILE_PATH_STR = '.idea/workspace.xml'


def get_default_file(storage_type: StorageType) -> str:
    """ Get the Default File Location for this Storage Type, as a String.

**Parameters:**
 - storage_type (StorageType): The enum describing which Storage to use.

**Returns:**
 str - The file location as a string.
    """
    if storage_type == StorageType.CHANGELISTS:
        return CHANGELISTS_FILE_PATH_STR
    if storage_type == StorageType.WORKSPACE:
        return WORKSPACE_FILE_PATH_STR
    # Add New Enums Here:
    raise ValueError(f"Invalid Argument: {storage_type}")


def get_default_path(storage_type: StorageType) -> Path:
    """ Get the Default File Path for this Storage Type.

**Parameters:**
 - storage_type (StorageType): The enum describing which Storage to use.

**Returns:**
 Path - The file Path object.
    """
    return Path(get_default_file(storage_type))

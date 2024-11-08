""" Testing Storage of Changelists XML Files.
"""
from pathlib import Path

from changelist_data.storage import StorageType
from changelist_data.storage.storage_type import CHANGELISTS_FILE_PATH_STR, get_default_path, WORKSPACE_FILE_PATH_STR


def test_get_default_path_changelist():
    assert Path(CHANGELISTS_FILE_PATH_STR) == get_default_path(StorageType.CHANGELISTS)


def test_get_default_path_workspace():
    assert Path(WORKSPACE_FILE_PATH_STR) == get_default_path(StorageType.WORKSPACE)

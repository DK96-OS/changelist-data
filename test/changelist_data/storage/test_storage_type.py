""" Testing Storage of Changelists XML Files.
"""
import pytest
from pathlib import Path

from changelist_data.storage import StorageType, storage_type
from changelist_data.storage.storage_type import CHANGELISTS_FILE_PATH_STR, get_default_path, WORKSPACE_FILE_PATH_STR


def test_get_default_path_changelist():
    assert Path(CHANGELISTS_FILE_PATH_STR) == get_default_path(StorageType.CHANGELISTS)


def test_get_default_path_workspace():
    assert Path(WORKSPACE_FILE_PATH_STR) == get_default_path(StorageType.WORKSPACE)


def test_get_default_file_invalid_arg_raises_value_error():
    with pytest.raises(ValueError, match="Invalid Argument: "):
        storage_type.get_default_file('hellow')
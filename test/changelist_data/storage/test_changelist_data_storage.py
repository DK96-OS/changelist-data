""" Testing Changelist Data Storage Class and Methods.
"""
import tempfile
from pathlib import Path
import pytest

import changelist_data.xml.changelists
from changelist_data.changelist import Changelist
from changelist_data.storage import StorageType, ChangelistDataStorage, load_storage


@pytest.fixture
def temp_dir():
    dir = tempfile.TemporaryDirectory()
    yield dir
    dir.cleanup()


@pytest.fixture
def temp_file(temp_dir):
    file = temp_dir.name + "/test_xml.xml"
    yield Path(file)


def test_write_to_storage_changelists_file_does_not_exist_returns_true(temp_file):
    temp_file.touch()
    result = load_storage(StorageType.CHANGELISTS, temp_file)
    assert isinstance(result, ChangelistDataStorage)
    assert result.storage_type == StorageType.CHANGELISTS
    assert len(result.get_changelists()) == 0
    #
    assert result.write_to_storage()
    assert len(temp_file.read_text()) > 0


def test_write_to_storage_after_update_changelists_file_does_not_exist_returns_true(temp_file):
    temp_file.touch()
    storage = load_storage(StorageType.CHANGELISTS, temp_file)
    #
    storage.update_changelists([Changelist('id', 'name', [])])
    assert storage.write_to_storage()
    #
    result = changelist_data.xml.changelists.read_xml(temp_file.read_text())
    assert len(result) == 1
    assert result[0].id == 'id'
    assert result[0].name == 'name'
    assert len(result[0].changes) == 0

""" Testing Storage of Workspace XML Files.
"""
import tempfile
from pathlib import Path
import pytest

from changelist_data.storage import changelists_storage, storage_type, StorageType
from changelist_data.xml.changelists import new_tree
from test.changelist_data.xml.changelists import provider


@pytest.fixture
def temp_dir():
    tdir = tempfile.TemporaryDirectory()
    yield tdir
    tdir.cleanup()


@pytest.fixture
def temp_file(temp_dir):
    file = temp_dir.name + "/test_xml.xml"
    yield Path(file)


def test_read_file_empty_returns_new_tree(temp_file):
    temp_file.write_text("")
    result = changelists_storage.read_file(temp_file)
    assert len(result) == 0


def test_read_file_invalid_xml_raises_exit(temp_file):
    temp_file.write_text("invalid xml")
    try:
        changelists_storage.read_file(temp_file)
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_read_file_none_returns_empty_list():
    result = changelists_storage.read_file(None)
    assert len(result) == 0


def test_read_file_no_cl(temp_file):
    temp_file.write_text(provider.get_no_changelist_xml())
    result = changelists_storage.read_file(temp_file)
    assert len(result) == 0


def test_read_file_simple_cl(temp_file):
    temp_file.write_text(provider.get_simple_changelist_xml())
    result = changelists_storage.read_file(temp_file)
    assert len(result) == 1


def test_read_file_multi_cl(temp_file):
    temp_file.write_text(provider.get_multi_changelist_xml())
    result = changelists_storage.read_file(temp_file)
    assert len(result) == 2


def test_load_file_invalid_xml_raises_exit(temp_file):
    temp_file.write_text("invalid xml")
    try:
        changelists_storage.load_file(temp_file)
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_load_file_none_returns_new_tree(temp_file):
    temp_file.write_text(provider.get_no_changelist_xml())
    result = changelists_storage.load_file(None)
    assert result.get_changelists() == new_tree().get_changelists()


def test_load_file_no_cl(temp_file):
    temp_file.write_text(provider.get_no_changelist_xml())
    result = changelists_storage.load_file(temp_file)
    assert len(result.get_changelists()) == 0


def test_load_file_simple_cl(temp_file):
    temp_file.write_text(provider.get_simple_changelist_xml())
    result = changelists_storage.load_file(temp_file)
    assert len(result.get_changelists()) == 1


def test_load_file_multi_cl(temp_file):
    temp_file.write_text(provider.get_multi_changelist_xml())
    result = changelists_storage.load_file(temp_file)
    assert len(result.get_changelists()) == 2


def test_write_file_none_tree(temp_file):
    temp_file.write_text("")
    changelists_storage.write_file(None, temp_file)
    # Read from Temp
    result = changelists_storage.read_file(temp_file)
    assert len(result) == 0


def test_write_file_no_cl(temp_file):
    temp_file.write_text(provider.get_no_changelist_xml())
    tree = changelists_storage.load_file(temp_file)
    changelists_storage.write_file(tree, temp_file)
    # Read from Temp
    result = changelists_storage.read_file(temp_file)
    assert len(result) == 0


def test_write_file_simple_cl(temp_file):
    temp_file.write_text(provider.get_simple_changelist_xml())
    tree = changelists_storage.load_file(temp_file)
    changelists_storage.write_file(tree, temp_file)
    # Read from Temp
    result = changelists_storage.read_file(temp_file)
    assert len(result) == 1


def test_write_file_multi_cl(temp_file):
    temp_file.write_text(provider.get_multi_changelist_xml())
    tree = changelists_storage.load_file(temp_file)
    changelists_storage.write_file(tree, temp_file)
    # Read from Temp
    result = changelists_storage.read_file(temp_file)
    assert len(result) == 2


def test_write_file_empty_default_changelist(temp_file):
    temp_file.write_text('')
    #
    tree = changelists_storage.load_file(
        storage_type.get_default_path(StorageType.CHANGELISTS)
    )
    changelists_storage.write_file(tree, temp_file)
    # Read from Temp
    result = changelists_storage.read_file(temp_file)
    assert len(result) == 0


def test_write_file_new_tree_empty():
    tree = new_tree()
    tree.write_tree(
        storage_type.get_default_path(StorageType.CHANGELISTS)
    )
    # Read from File
    result = changelists_storage.read_file(
        storage_type.get_default_path(StorageType.CHANGELISTS)
    )
    assert len(result) == 0

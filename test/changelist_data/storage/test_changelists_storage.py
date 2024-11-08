""" Testing Storage of Workspace XML Files.
"""
import tempfile
from pathlib import Path
import pytest

from changelist_data.storage import changelists_storage
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

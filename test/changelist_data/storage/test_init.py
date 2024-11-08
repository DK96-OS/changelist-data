""" Testing Changelist Data Storage Package Methods.
"""
import tempfile
from pathlib import Path
from unittest.mock import Mock

import pytest

import changelist_data.xml.changelists
from changelist_data.storage import read_storage, load_storage, StorageType
from test.changelist_data.xml.changelists import provider as changelists_provider
from test.changelist_data.xml.workspace import provider as workspace_provider


@pytest.fixture
def temp_dir():
    dir = tempfile.TemporaryDirectory()
    yield dir
    dir.cleanup()


@pytest.fixture
def temp_file(temp_dir):
    file = temp_dir.name + "/test_xml.xml"
    yield Path(file)


def test_read_storage_defaults_no_files_exist_returns_empty_list():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        result = read_storage()
    assert len(result) == 0


def test_read_storage_defaults_all_paths_are_dirs_returns_empty_list():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: False)
        result = read_storage()
    assert len(result) == 0


def test_read_storage_default_simple_cl_():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: changelists_provider.get_simple_changelist_xml())
        result = read_storage()
    assert len(result) == 1


def test_read_storage_file_does_not_exist_():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        try:
            read_storage(None, Path("filepath"))
            raises_exit = False
        except SystemExit:
            raises_exit = True
        assert raises_exit


def test_read_storage_changelists_simple_cl_():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: changelists_provider.get_simple_changelist_xml())
        result = read_storage(StorageType.CHANGELISTS, Path("filepath"))
    assert len(result) == 1


def test_read_storage_workspace_simple_cl_():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: workspace_provider.get_simple_changelist_xml())
        result = read_storage(StorageType.WORKSPACE, Path("filepath"))
    assert len(result) == 1


def test_load_storage_changelists_empty_file_raises_exit(temp_file):
    temp_file.write_text("")
    try:
        load_storage(StorageType.CHANGELISTS, temp_file)
        raised_exit = False
    except SystemExit:
        raised_exit = True
    assert raised_exit


def test_load_storage_workspace_empty_file_raises_exit(temp_file):
    temp_file.write_text("")
    try:
        load_storage(StorageType.WORKSPACE, temp_file)
        raised_exit = False
    except SystemExit:
        raised_exit = True
    assert raised_exit


def test_load_storage_changelists_no_changelists(temp_file):
    temp_file.write_text(changelist_data.xml.changelists.EMPTY_CHANGELISTS_DATA)
    load_storage(StorageType.CHANGELISTS, temp_file)


def test_load_storage_workspace_no_changelists(temp_file):
    temp_file.write_text(changelist_data.xml.changelists.EMPTY_CHANGELISTS_DATA)
    load_storage(StorageType.WORKSPACE, temp_file)

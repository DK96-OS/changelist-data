""" Testing Changelist Data Storage load_storage Method.
"""
from pathlib import Path
from unittest.mock import Mock

import pytest

import changelist_data.xml.changelists
from changelist_data.storage import load_storage
from changelist_data.storage.changelist_data_storage import ChangelistDataStorage
from changelist_data.storage.storage_type import StorageType


def test_load_storage_changelists_empty_file_returns_new_tree(temp_file):
    temp_file.write_text("")
    result = load_storage(StorageType.CHANGELISTS, temp_file)
    #
    assert isinstance(result, ChangelistDataStorage)
    assert len(result.get_changelists()) == 0


def test_load_storage_changelists_file_does_not_exist_returns_empty(temp_file):
    temp_file.unlink(missing_ok=True)
    result = load_storage(StorageType.CHANGELISTS, temp_file)
    assert isinstance(result, ChangelistDataStorage)
    assert result.storage_type == StorageType.CHANGELISTS
    assert len(result.get_changelists()) == 0


def test_load_storage_workspace_empty_file_raises_exit(temp_file):
    temp_file.write_text("")
    try:
        load_storage(StorageType.WORKSPACE, temp_file)
        raised_exit = False
    except SystemExit:
        raised_exit = True
    assert raised_exit


def test_load_storage_changelists_no_changelists_returns_empty_storage(temp_file):
    temp_file.write_text(changelist_data.xml.changelists.EMPTY_CHANGELISTS_DATA)
    result = load_storage(StorageType.CHANGELISTS, temp_file)
    assert isinstance(result, ChangelistDataStorage)
    assert len(result.get_changelists()) == 0


def test_load_storage_workspace_no_clm_raises_exit(temp_file, no_clm_workspace_xml):
    temp_file.write_text(no_clm_workspace_xml)
    try:
        result = load_storage(StorageType.WORKSPACE, temp_file)
        assert isinstance(result, ChangelistDataStorage)
        assert len(result.get_changelists()) == 0
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_load_storage_workspace_empty_changelists_returns_empty_storage(temp_file, empty_workspace_xml):
    temp_file.write_text(empty_workspace_xml)
    result = load_storage(StorageType.WORKSPACE, temp_file)
    assert isinstance(result, ChangelistDataStorage)
    assert len(result.get_changelists()) == 0


def test_load_storage_changelists_simple_cl_returns_simple_list(temp_file, simple_changelists_xml):
    temp_file.write_text(simple_changelists_xml)
    result = load_storage(StorageType.CHANGELISTS, temp_file)
    assert len(result.get_changelists()) == 1


def test_load_storage_workspace_simple_cl_returns_simple_list(temp_file, simple_workspace_xml):
    temp_file.write_text(simple_workspace_xml)
    result = load_storage(StorageType.WORKSPACE, temp_file)
    assert len(result.get_changelists()) == 1


def test_load_storage_changelists_multi_cl_returns_multi_list(temp_file, multi_changelists_xml):
    temp_file.write_text(multi_changelists_xml)
    result = load_storage(StorageType.CHANGELISTS, temp_file)
    assert len(result.get_changelists()) == 2


def test_load_storage_workspace_multi_cl_returns_multi_list(temp_file, multi_workspace_xml):
    temp_file.write_text(multi_workspace_xml)
    result = load_storage(StorageType.WORKSPACE, temp_file)
    assert len(result.get_changelists()) == 2


def test_load_storage_none_changelists_simple_cl_returns_simple_list(simple_changelists_xml):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: simple_changelists_xml)
        result = load_storage(None)
    assert len(result.get_changelists()) == 1


def test_load_storage_none_workspace_simple_cl_raises_exit(simple_workspace_xml):
    """ This case raises exit because it checks Changelists default path first.
    Due to MP, it sees that every file exists, but the provider gives Workspace XML format.
    Since it expects Changelists XML, it will exit after parsing xml and searching for changelists tag.
    """
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: simple_workspace_xml)
        try:
            result = load_storage(None)
            assert len(result.get_changelists()) == 1
            raises_exit = False
        except SystemExit:
            raises_exit = True
        assert raises_exit


def test_load_storage_none_with_file_path_raises_exit(temp_file):
    try:
        result = load_storage(None, temp_file)
        assert len(result.get_changelists()) == 1
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit

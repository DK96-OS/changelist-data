""" Testing Changelist Data Storage Package Methods.
"""
from pathlib import Path
from unittest.mock import Mock

import pytest

from changelist_data.storage import generate_changelists_from_storage
from changelist_data.storage.storage_type import StorageType


def test_generate_changelists_from_storage_defaults_no_files_exist_returns_empty_list():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        result = list(generate_changelists_from_storage())
    assert len(result) == 0


def test_generate_changelists_from_storage_defaults_all_paths_are_dirs_returns_empty_list():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: False)
        result = list(generate_changelists_from_storage())
    assert len(result) == 0


def test_generate_changelists_from_storage_default_simple_cl_(simple_changelists_xml):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: simple_changelists_xml)
        result = list(generate_changelists_from_storage())
    assert len(result) == 1


def test_generate_changelists_from_storage_file_does_not_exist_():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        try:
            result = list(generate_changelists_from_storage(None, Path("filepath")))
            raises_exit = False
        except SystemExit:
            raises_exit = True
        assert raises_exit



def test_generate_changelists_from_storage_workspace_simple_cl_returns_simple_list(simple_workspace_xml, simple_cl):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: simple_workspace_xml)
        result = list(generate_changelists_from_storage(StorageType.WORKSPACE, Path("filepath")))
    assert result[0].id == simple_cl.id
    assert len(result) == 1


def test_generate_changelists_from_storage_changelists_simple_cl_returns_simple_list(simple_changelists_xml, simple_cl):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: simple_changelists_xml)
        result = list(generate_changelists_from_storage(StorageType.CHANGELISTS, Path("filepath")))
    assert result[0].id == simple_cl.id
    assert len(result) == 1


def test_generate_changelists_from_storage_changelists_multi_cl_returns_list(multi_changelists_xml):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: multi_changelists_xml)
        result = list(generate_changelists_from_storage(StorageType.CHANGELISTS))
    assert len(result) == 2


def test_generate_changelists_from_storage_workspace_simple_cl_returns_simple_list(simple_workspace_xml, simple_cl):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: simple_workspace_xml)
        result = list(generate_changelists_from_storage(StorageType.WORKSPACE))
    assert result[0].id == simple_cl.id
    assert len(result) == 1


def test_generate_changelists_from_storage_workspace_multi_cl_returns_list(multi_workspace_xml):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: multi_workspace_xml)
        result = list(generate_changelists_from_storage(StorageType.WORKSPACE))
    assert len(result) == 2
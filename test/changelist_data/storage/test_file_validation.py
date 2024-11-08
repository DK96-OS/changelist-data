""" Testing File Validation Methods
"""
from pathlib import Path
from unittest.mock import Mock
import pytest

from changelist_data.storage import StorageType
from changelist_data.storage.file_validation import validate_file_input_text, file_exists, check_if_default_file_exists
from test.changelist_data.xml.changelists import provider


def test_file_exists_does_not_exist_returns_false():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        assert not file_exists(Path('any'))


def test_file_exists_is_not_file_returns_false():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: False)
        assert not file_exists(Path('any'))


def test_file_exists_is_file_returns_true():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        assert file_exists(Path('any'))


def test_check_if_default_file_exists_changelists_does_not_exist_returns_none():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        assert check_if_default_file_exists(StorageType.CHANGELISTS) is None


def test_check_if_default_file_exists_changelists_is_not_file_returns_none():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: False)
        assert check_if_default_file_exists(StorageType.CHANGELISTS) is None


def test_check_if_default_file_exists_changelists_is_file_returns_path():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        assert isinstance(
            check_if_default_file_exists(StorageType.CHANGELISTS), Path
        )


def test_check_if_default_file_exists_workspace_does_not_exist_returns_none():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        assert check_if_default_file_exists(StorageType.WORKSPACE) is None


def test_check_if_default_file_exists_workspace_is_not_file_returns_none():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: False)
        assert check_if_default_file_exists(StorageType.WORKSPACE) is None


def test_check_if_default_file_exists_workspace_is_file_returns_true():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        assert isinstance(
            check_if_default_file_exists(StorageType.WORKSPACE), Path
        )


def test_validate_file_input_text_does_not_exist_raises_exit():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        try:
            validate_file_input_text(Path("file_name"))
            raises_exit = False
        except SystemExit:
            raises_exit = True
        assert raises_exit


def test_validate_file_input_text_is_not_file_raises_exit():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: False)
        try:
            validate_file_input_text(Path("file_name"))
            raises_exit = False
        except SystemExit:
            raises_exit = True
        assert raises_exit


def test_validate_file_input_text_filesize_too_large_raises_exit():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 33 * 1024 ** 3
        c.setattr(Path, 'stat', lambda _: obj)
        try:
            validate_file_input_text(Path("file_name"))
            raises_exit = False
        except SystemExit:
            raises_exit = True
        assert raises_exit


def test_validate_file_input_text_simple_changelist_returns_str():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: provider.get_simple_changelist_xml())
        simple_xml = validate_file_input_text(Path("file_name"))
    assert len(simple_xml) == 240

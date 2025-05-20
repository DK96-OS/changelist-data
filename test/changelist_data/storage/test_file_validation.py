""" Testing File Validation Methods
"""
from pathlib import Path
from unittest.mock import Mock

import pytest

from changelist_data.storage import StorageType
from changelist_data.storage.file_validation import validate_file_input_text, file_exists, check_if_default_file_exists


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


def test_validate_file_input_text_simple_changelist_returns_str(simple_changelists_xml):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: True)
        obj = Mock()
        obj.__dict__["st_size"] = 4 * 1024
        c.setattr(Path, 'stat', lambda _: obj)
        c.setattr(Path, 'read_text', lambda _: simple_changelists_xml)
        simple_xml = validate_file_input_text(Path("file_name"))
    assert len(simple_xml) == 259


def test_validate_file_input_text_file_not_exist(tmp_path):
    file_path = tmp_path / "does_not_exist.txt"
    with pytest.raises(SystemExit, match="File did not exist"):
        validate_file_input_text(file_path)

def test_validate_file_input_text_not_a_file(tmp_path):
    dir_path = tmp_path / "adir"
    dir_path.mkdir()
    with pytest.raises(SystemExit, match="Given Path was not a file"):
        validate_file_input_text(dir_path)

def test_validate_file_input_text_file_deleted_after_check(monkeypatch, tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("content")
    # Simulate deletion after the exists/is_file check, before read_text
    monkeypatch.setattr(Path, "read_text", lambda self: (_ for _ in ()).throw(FileNotFoundError()))
    with pytest.raises(SystemExit, match="Couldn't find the file, after checking that it exists."):
        validate_file_input_text(file_path)

def test_validate_file_input_text_permission_error(monkeypatch, tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("content")
    # Simulate OSError/PermissionError
    def raise_permission_error(self):
        raise PermissionError("No permission")
    monkeypatch.setattr(Path, "read_text", raise_permission_error)
    with pytest.raises(SystemExit, match="IOError occurred while reading Input File"):
        validate_file_input_text(file_path)

def test_validate_file_input_text_unicode_decode_error(monkeypatch, tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("content")
    # Simulate UnicodeDecodeError
    def raise_unicode_error(self):
        raise UnicodeDecodeError("utf-8", b"", 0, 1, "reason")
    monkeypatch.setattr(Path, "read_text", raise_unicode_error)
    with pytest.raises(SystemExit, match="File is not valid text. Unicode decode error."):
        validate_file_input_text(file_path)
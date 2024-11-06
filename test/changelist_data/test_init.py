""" Testing this package's init module
"""
import pytest
from pathlib import Path

from changelist_data import read_default


def test_read_default_no_files_exist():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        try:
            read_default()
            raises_exit = False
        except SystemExit:
            raises_exit = True
        assert raises_exit


def test_read_default_no_paths_are_files():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'is_file', lambda _: False)
        try:
            read_default()
            raises_exit = False
        except SystemExit:
            raises_exit = True
        assert raises_exit

""" Base Data Classes for Changelists and Files.
"""
from pathlib import Path

from changelist_data import storage
from changelist_data.changelist import Changelist
from changelist_data.storage.changelist_data_storage import ChangelistDataStorage


def read_default() -> list[Changelist]:
    """ Tries to Read Changelists, then Workspace.
        Returns Empty List if nothing is found.
    """
    try:
        default_list = storage.read_changelists_storage()
        if len(default_list) > 0:
            return default_list
    except ValueError:
        pass
    try:
        return storage.read_workspace_storage()
    except ValueError:
        return []


def load_default() -> ChangelistDataStorage | None:
    """ Tries to Load Changelists, then Workspace.
        Returns None if nothing is found.
    """
    try:
        default_tree = storage.load_changelists_tree()
        if default_tree is not None:
            return default_tree
    except ValueError:
        pass
    try:
        return storage.load_workspace_tree()
    except ValueError:
        return None


EMPTY_CHANGELISTS_DATA = """<?xml version="1.0" encoding="UTF-8"?>
<changelists></changelists>"""


def write_file(
    tree: ChangelistDataStorage | None,
    file_path: Path = storage.file_validation.get_default_file_path(),
) -> bool:
    """
    """
    if tree is None:
        file_path.write_text(EMPTY_CHANGELISTS_DATA)
        return True
    tree.write_tree(file_path)
    return True

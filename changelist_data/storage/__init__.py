""" Storage option specific methods for read-only and writable access.
"""
from pathlib import Path

from changelist_data.changelist import Changelist
from changelist_data.storage import file_validation
from changelist_data.xml import changelists, workspace
from changelist_data.xml.changelists.changelists_tree import ChangelistsTree
from changelist_data.xml.workspace.workspace_tree import WorkspaceTree


def read_changelists_storage(
    file_path: Path | None = file_validation.find_changelists_storage(),
) -> list[Changelist]:
    """
    """
    if file_path is None:
        return [] # Empty Changelists
    return changelists.read_xml(
        file_validation.validate_file_input_text(file_path)
    )


def read_workspace_storage(
    file_path: Path | None = file_validation.find_workspace_storage(),
) -> list[Changelist]:
    """
    """
    if file_path is None:
        raise ValueError("Workspace File Not Found")
    return workspace.read_xml(
        file_validation.validate_file_input_text(file_path)
    )


def load_changelists_tree(
    file_path: Path | None = file_validation.find_changelists_storage(),
) -> ChangelistsTree:
    """
    """
    if file_path is None:
        return changelists.new_tree()
    return changelists.load_tree(
        file_validation.validate_file_input_text(file_path)
    )


def load_workspace_tree(
    file_path: Path | None = file_validation.find_workspace_storage(),
) -> WorkspaceTree:
    """
    """
    if file_path is None:
        exit("Only use Workspace Tree if a Workspace XML file has been given to you.")
    return workspace.load_tree(
        file_validation.validate_file_input_text(file_path)
    )

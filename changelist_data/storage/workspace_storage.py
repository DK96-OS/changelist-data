""" Storage for Workspace XML Format.
"""
from pathlib import Path

from changelist_data.changelist import Changelist
from changelist_data.storage import file_validation, storage_type
from changelist_data.storage.storage_type import StorageType
from changelist_data.xml.workspace import read_xml, load_xml
from changelist_data.xml.workspace.workspace_tree import WorkspaceTree


def read_file(
    file_path: Path = storage_type.get_default_path(StorageType.WORKSPACE),
) -> list[Changelist]:
    """ Read a Workspace XML Storage File.
        Default file_path is given by StorageType.

    Parameters:
    - file_path (Path): The Path to the File containing Workspace XML.

    Returns:
    list[Changelist] - The list of Changelist data stored in Workspace Storage.
    """
    return read_xml(
        file_validation.validate_file_input_text(file_path)
    )


def load_file(
    file_path: Path = storage_type.get_default_path(StorageType.WORKSPACE),
) -> WorkspaceTree:
    """ Load a Tree from Workspace XML Storage File.

    Parameters:
    - file_path (Path): The Path to the File containing Workspace XML.

    Returns:
    WorkspaceTree - The list of Changelist data stored in Workspace Storage.
    """
    if file_path is None:
        exit("Only use Workspace Tree if a Workspace XML file has been given to you.")
    return load_xml(
        file_validation.validate_file_input_text(file_path)
    )


def write_file(
    tree: WorkspaceTree,
    file_path: Path = storage_type.get_default_path(StorageType.WORKSPACE),
) -> bool:
    """ Write a Changelist Data Storage object to an XML File.

    Parameters:
    - tree (ChangelistDataStorage): The Tree object containing the Changelists.
    - file_path (Path): The File Path to write the XML data to.

    Returns:
    bool - True after the operation succeeds.
    """
    if tree is None or not isinstance(tree, WorkspaceTree):
        return False
    tree.write_tree(file_path)
    return True

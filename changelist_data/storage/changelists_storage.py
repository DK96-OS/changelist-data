""" Storage for Changelists Data XML Format.
"""
from pathlib import Path

from changelist_data.changelist import Changelist
from changelist_data.storage import storage_type, file_validation
from changelist_data.storage.storage_type import StorageType
from changelist_data.xml import changelists
from changelist_data.xml.changelists import ChangelistsTree, EMPTY_CHANGELISTS_DATA


def read_file(
    file_path: Path | None = storage_type.get_default_path(StorageType.CHANGELISTS),
) -> list[Changelist]:
    """ Read a Changelists XML Storage File.
        Default file_path is given by StorageType.
        None file_path returns an empty list.

    Parameters:
    - file_path (Path): The Path to the File containing Changelists XML.

    Returns:
    list[Changelist] - The list of Changelist data stored in Changelists Storage.
    """
    if file_path is None:
        return [] # None Path Given
    if len(file_content := file_validation.validate_file_input_text(file_path)) == 0:
        return [] # Empty Data File
    return changelists.read_xml(file_content)


def load_file(
    file_path: Path | None = storage_type.get_default_path(StorageType.CHANGELISTS),
) -> ChangelistsTree:
    """ Load a Tree from Changelists XML Storage File.
        Default file_path

    Parameters:
    - file_path (Path): The Path to the File containing Changelists XML.

    Returns:
    ChangelistsTree - The list of Changelist data stored in Changelists Storage.
    """
    if file_path is None or\
        not file_validation.file_exists(file_path):
        return changelists.new_tree()
    # Validate File Stats, Read and Parse the XML
    if len(file_content := file_validation.validate_file_input_text(file_path)) == 0:
        return changelists.new_tree() # Empty Data File
    # Parse and wrap XML ElementTree in ChangelistsTree
    return changelists.load_xml(file_content)


def write_file(
    tree: ChangelistsTree | None,
    file_path: Path = storage_type.get_default_path(StorageType.CHANGELISTS),
) -> bool:
    """ Write a Changelist Data Storage object to an XML File.

    Parameters:
    - tree (ChangelistDataStorage): The Tree object containing the Changelists.
    - file_path (Path): The File Path to write the XML data to.

    Returns:
    bool - True after the operation succeeds.
    """
    if tree is None:
        file_path.write_text(EMPTY_CHANGELISTS_DATA)
        return True
    tree.write_tree(file_path)
    return True

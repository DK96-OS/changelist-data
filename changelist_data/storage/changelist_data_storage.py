""" An Abstract Class defining the interface for translation between XML Trees and Changelists.
"""
from dataclasses import dataclass
from pathlib import Path

from changelist_data.changelist import Changelist
from changelist_data.storage.storage_type import StorageType
from changelist_data.xml.base_xml_tree import BaseXMLTree


@dataclass(frozen=True)
class ChangelistDataStorage:
    """ Controller Interface for Data Storage.

    Fields:
    - base_xml_tree (BaseXMLTree): A Wrapper around XML ElementTree, compatible with both xml format Storage Types.
    - storage_type (StorageType): An enum selecting the specific xml format used.
    - update_path (Path): The file Path where Data is read from and written to.
    """
    base_xml_tree: BaseXMLTree
    storage_type: StorageType
    update_path: Path

    def get_changelists(self) -> list[Changelist]:
        return self.base_xml_tree.get_changelists()

    def update_changelists(
        self, changelists: list[Changelist]
    ):
        """ Overwrite the collection of Changelist data in Memory.

        Parameters:
        - changelists (list[Changelist]): The new list of Changelists.
        """
        self.base_xml_tree.update_changelists(changelists)

    def write_to_storage(self) -> bool:
        """ Create or overwrite storage file.
            Ensures parent directories exist.

        Returns:
        bool - True if data was written.
        """
        return self.base_xml_tree.write_tree(self.update_path)

""" An Abstract Class defining the interface for translation between XML Trees and Changelists.
"""
from dataclasses import dataclass
from pathlib import Path

from changelist_data.changelist import Changelist
from changelist_data.storage.storage_type import StorageType
from changelist_data.xml.base_xml_tree import BaseXMLTree


@dataclass(frozen=True)
class ChangelistDataStorage:
    """
    """
    base_xml_tree: BaseXMLTree
    storage_type: StorageType
    update_path: Path

    def get_changelists(self) -> list[Changelist]:
        return self.base_xml_tree.get_changelists()

    def update_changelists(self, changelists: list[Changelist]):
        self.base_xml_tree.update_changelists(changelists)

    def write_to_storage(self) -> bool:
        self.base_xml_tree.write_tree(self.update_path)
        return True

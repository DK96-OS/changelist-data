""" An Abstract Class defining the interface for translation between XML Trees and Changelists.
"""
from abc import ABCMeta, abstractmethod

from changelist_data.changelist import Changelist
from changelist_data.xml.base_xml_tree import BaseXMLTree


class ChangelistDataStorage(BaseXMLTree, metaclass=ABCMeta):

    @abstractmethod
    def get_changelists(self) -> list[Changelist]:
        pass

    @abstractmethod
    def update_changelists(self, changelists: list[Changelist]):
        pass

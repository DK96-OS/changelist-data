""" XML Tree File Writing Abstract Class.
"""
from abc import ABCMeta, abstractmethod
from pathlib import Path
from xml.etree.ElementTree import ElementTree, tostring

from changelist_data.changelist import Changelist


class BaseXMLTree(metaclass=ABCMeta):
    """ A Base Abstract Class providing writing capabilities for an XML Tree class.
    """

    @abstractmethod
    def get_root(self) -> ElementTree:
        raise NotImplementedError

    @abstractmethod
    def get_changelists(self) -> list[Changelist]:
        raise NotImplementedError

    @abstractmethod
    def update_changelists(self, changelists: list[Changelist]):
        raise NotImplementedError

    def write_tree(
        self, path: Path,
    ) -> bool:
        """ Write the Tree as XML to the given Path.
            Ensures that all parent directories exist, and creates the file if necessary.

        Parameters:
        - path (Path): The Path to the File.

        Returns:
        bool - True if data was written to the file.
        """
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        return path.write_bytes(
            tostring(
                element=self.get_root().getroot(),
                encoding='utf-8',
                method='xml',
                xml_declaration=True,
            )
        ) > 0

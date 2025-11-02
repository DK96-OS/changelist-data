""" XML Tree Class for Changelists Data XML.
"""
from typing import Iterable, Generator
from xml.etree.ElementTree import Element, ElementTree, indent

from changelist_data.changelist import Changelist
from changelist_data.xml.base_xml_tree import BaseXMLTree
from changelist_data.xml.changelists import changelists_reader, changelists_writer


class ChangelistsTree(BaseXMLTree):
    """ Manages the Changelists Data XML Element Trees.

**Properties:**
 - xml_root (Element): The XML root element.
 - changelists_element (Element): The Changelists Tag Element.
    """

    def __init__(
        self,
        xml_root: Element,
    ):
        self._xml_root = xml_root
        self.changelists_element = changelists_reader.find_changelists_root(xml_root)

    def get_changelists(self) -> list[Changelist]:
        """ Given the Changelist Manager Element, obtain the list of List Elements.

    **Returns:**
     list[Changelist] - A List containing the Lists.
        """
        return list(self.generate_changelists())

    def generate_changelists(self) -> Generator[Changelist, None, None]:
        """ Generate Changelists from the Tree.

    **Yields:**
     Changelist - The data objects extracted from the Storage XML Tree.
        """
        if self.changelists_element is None:
            exit('XML File does not have a Changelists Element.')
        yield from changelists_reader.generate_changelists(self.changelists_element)

    def get_root(self) -> ElementTree:
        """ Obtain the XML ElementTree Root.

    **Returns:**
     ElementTree - The XML Tree Root Element.
        """
        return ElementTree(self._xml_root)

    def update_changelists(
        self,
        changelists: Iterable[Changelist],
    ):
        """ Update the XML Tree's Changelists.

    **Parameters:**
     - changelists (Iterable[Changelist]): The List or Iterable of Changelists.
        """
        if (clm := self.changelists_element) is None:
            exit('XML File does not have a Changelists Element.')
        # Clear the Changelists Element
        clm.clear() # Need to Restore any Attributes after Clear operation:
        # - No attributes in use by changelists at the moment.
        # Add All Sub Elements
        clm.extend(changelists_writer.write_list_element(x) for x in changelists)
        indent(clm, level=0)
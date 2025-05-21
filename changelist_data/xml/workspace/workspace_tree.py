""" Loads the Workspace file into a Tree with read/write capabilities.
"""
from typing import Iterable, Generator
from xml.etree.ElementTree import Element, ElementTree, indent

from changelist_data.changelist import Changelist
from changelist_data.xml.base_xml_tree import BaseXMLTree
from changelist_data.xml.workspace import workspace_writer, workspace_reader


class WorkspaceTree(BaseXMLTree):
    """ Manages the Workspace XML Element Trees.

**Properties:**
 - xml_root (Element): The XML root element.
 - changelist_manager (Element): The Changelist Manager Component Element.
    """

    def __init__(
        self,
        xml_root: Element,
    ):
        self._xml_root = xml_root
        self.changelist_manager = workspace_reader.find_changelist_manager(xml_root)

    def get_changelists(self) -> list[Changelist]:
        """ Obtain the list of CL Elements.

    **Returns:**
     list[Changelist] - A List containing the Lists.
        """
        return list(self.generate_changelists())

    def generate_changelists(self) -> Generator[Changelist, None, None]:
        if self.changelist_manager is None:
            exit('XML File does not have a Changelists Element.')
        return workspace_reader.generate_changelists(self.changelist_manager)

    def get_root(self) -> ElementTree:
        """ Obtain the XML ElementTree Root.
        """
        return ElementTree(self._xml_root)

    def update_changelists(
        self,
        changelists: Iterable[Changelist],
    ):
        """ Update the XML Tree's Changelist Manager Lists.
        
    **Parameters:**
     - changelists (Iterable[Changelist]): The List or Iterable of Changelists.
        """
        clm = self.changelist_manager
        if clm is None:
            exit('XML File does not have a Changelist Manager.')
        # First obtain all Option Elements
        options = list(clm.findall('option'))
        # Clear the Changelist Manager Tag
        clm.clear() # Need to Add Name Attribute after Clear operation
        clm.attrib['name'] = "ChangeListManager"
        # Add All Sub Elements
        clm.extend(workspace_writer.write_list_element(x) for x in changelists)
        clm.extend(options)
        indent(clm, level=1)
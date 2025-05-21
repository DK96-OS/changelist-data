""" Changelist Data Storage XML Workspace
"""
from typing import Generator

from changelist_data.changelist import Changelist
from changelist_data.xml.workspace import workspace_reader
from changelist_data.xml.workspace.workspace_tree import WorkspaceTree


def read_xml(
    workspace_xml: str
) -> list[Changelist]:
    """ Parse the Workspace XML file and obtain all ChangeList Data in a list.

    Parameters:
     - workspace_xml (str): The contents of the Workspace file, in xml format.
    
    Returns:
     list[Changelist] - The list of Changelists in the workspace file.
    """
    return list(generate_changelists_from_xml(workspace_xml))


def generate_changelists_from_xml(
    workspace_xml: str
) -> Generator[Changelist, None, None]:
    """ Generates Changelist Data from the Given XML String.
 - Parses the XML string using ElementTree.
 - Creates Changelist data objects one at a time from the ElementTree.

**Parameters:**
 - workspace_xml (str): The Workspace xml file contents as a string.

**Yields:**
 Changelist - The Changelist data objects extracted from the XML ElementTree.
    """
    if (cl_manager := workspace_reader.find_changelist_manager(
        workspace_reader.parse_xml(workspace_xml)
    )) is None:
        exit("Changelist Manager was not found in the workspace file.")
    yield from workspace_reader.generate_changelists(cl_manager)



def load_xml(
    workspace_xml: str
) -> WorkspaceTree:
    """ Parse the Workspace XML file into an XML Tree, and Wrap it.

    Parameters:
     - workspace_xml (str): The contents of the Workspace file, in xml format.

    Returns:
     WorkspaceTree - An XML Tree changelists interface.
    """
    return WorkspaceTree(
        workspace_reader.parse_xml(workspace_xml)
    )
""" Changelist Data Storage XML Workspace
"""
from changelist_data.changelist import Changelist
from changelist_data.xml.workspace import workspace_reader
from changelist_data.xml.workspace.workspace_tree import WorkspaceTree


def read_xml(
    workspace_xml: str
) -> list[Changelist]:
    """
    Parse the Workspace XML file and obtain all ChangeList Data in a list.

    Parameters:
    - workspace_xml (str): The contents of the Workspace file, in xml format.
    
    Returns:
    list[Changelist] - The list of Changelists in the workspace file.
    """
    return workspace_reader.read_workspace_xml(workspace_xml)


def load_tree(
    workspace_xml: str
) -> WorkspaceTree:
    """
    Parse the Workspace XML file into an XML Tree, and Wrap it.

    Returns:
    WorkspaceTree - An XML Tree changelists interface.
    """
    return WorkspaceTree(
        workspace_reader.parse_xml(workspace_xml)
    )

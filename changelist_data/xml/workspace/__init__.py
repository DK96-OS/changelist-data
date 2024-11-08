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
    if (cl_manager := workspace_reader.find_changelist_manager(workspace_reader.parse_xml(workspace_xml))) is None:
        exit("ChangeList Manager was not found in the workspace file.")
    return workspace_reader.extract_list_elements(cl_manager)


def load_xml(
    workspace_xml: str
) -> WorkspaceTree:
    """
    Parse the Workspace XML file into an XML Tree, and Wrap it.

    Parameters:
    - workspace_xml (str): The contents of the Workspace file, in xml format.

    Returns:
    WorkspaceTree - An XML Tree changelists interface.
    """
    return WorkspaceTree(
        workspace_reader.parse_xml(workspace_xml)
    )

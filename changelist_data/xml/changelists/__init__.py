""" Changelist Data Storage XML Changelists Data File.
"""
from changelist_data.changelist import Changelist
from changelist_data.xml.changelists import changelists_reader
from changelist_data.xml.changelists.changelists_tree import ChangelistsTree


EMPTY_CHANGELISTS_DATA = """<?xml version="1.0" encoding="UTF-8"?>
<changelists>
</changelists>"""


def read_xml(
    changelists_xml: str
) -> list[Changelist]:
    """
    Parse the ChangeLists XML file and obtain all ChangeList Data in a list.

    Parameters:
    - changelists_xml (str): The contents of the ChangeLists file, in xml format.
    
    Returns:
    list[Changelist] - The list of Changelist objects in the ChangeLists file.
    """
    return changelists_reader.read_xml(changelists_xml)


def load_xml(
    changelists_xml: str
) -> ChangelistsTree:
    """
    Parse the Changelists XML file into an XML Tree, and Wrap it.

    Returns:
    ChangelistsTree - An XML Tree changelists interface.
    """
    return ChangelistsTree(
        changelists_reader.parse_xml(changelists_xml)
    )


def new_tree() -> ChangelistsTree:
    """
    Create a new Changelists XML Tree, and Wrap it.

    Returns:
    ChangelistsTree - An XML Tree changelists interface.
    """
    return ChangelistsTree(
        changelists_reader.parse_xml(EMPTY_CHANGELISTS_DATA)
    )

""" Reads the Workspace File, translates into Changelist Data types.
"""
from xml.etree.ElementTree import Element, ParseError, fromstring

from changelist_data.file_change import FileChange
from changelist_data.changelist import Changelist
from changelist_data.xml import xml_reader


def parse_xml(workspace_xml: str) -> Element:
    """ Parse an XML File. This should be a Workspace XML file.
        Returns the XML Root Element, or raises SystemExit.
    """
    try:
        return fromstring(workspace_xml)
    except ParseError:
        exit("Unable to Parse Workspace XML File.")


def find_changelist_manager(
    xml_root: Element
) -> Element | None:
    """ Find the ChangeList Manager in the XML Element Hierarchy.
        Looks for a Component Tag with the right name attribute.
        Returns None if the Element is not found.
    """
    for elem in xml_reader.filter_by_tag(xml_root, 'component'):
        try:
            if elem.attrib["name"] == 'ChangeListManager':
                return elem
        except KeyError:
            pass
    return None


def extract_list_elements(
    changelist_manager: Element
) -> list[Changelist]:
    """
    Given the Changelist Manager Element, obtain the list of List Elements.

    Parameters:
    - changelist_manager (Element): The ChangeList Manager XML Element.

    Returns:
    list[Element] - A List containing the Lists.
    """
    return [
        Changelist(
            id=xml_reader.get_attr(cl_element, 'id'),
            name=xml_reader.get_attr(cl_element, 'name'),
            changes=_extract_change_data(cl_element),
            comment=xml_reader.get_attr_or(cl_element, 'comment', ''),
            is_default=xml_reader.read_bool_from(cl_element, 'default'),
        ) for cl_element in xml_reader.filter_by_tag(changelist_manager, 'list')
    ]


_PROJECT_DIR_VAR = '$PROJECT_DIR$'
_PROJECT_DIR_LEN = len(_PROJECT_DIR_VAR)


def _filter_project_dir(path_str: str | None) -> str:
    """Filter the ProjectDir string at the beginning of the path.
    """
    if path_str is None:
        return None
    if path_str.startswith(_PROJECT_DIR_VAR):
        return path_str[_PROJECT_DIR_LEN:]
    return path_str


def _extract_change_data(
    list_element: Element,
) -> list[FileChange]:
    """
    Given a ChangeList XML Element, obtain the List of Changes.

    Parameters:
    - list_element (Element):  The Element representing a Changelist.

    Returns:
    list[FileChange] - The list of structured FileChange.
    """
    return [
        FileChange(
            before_path=_filter_project_dir(xml_reader.get_attr(change, 'beforePath')),
            before_dir=xml_reader.convert_bool(xml_reader.get_attr(change, 'beforeDir')),
            after_path=_filter_project_dir(xml_reader.get_attr(change, 'afterPath')),
            after_dir=xml_reader.convert_bool(xml_reader.get_attr(change, 'afterDir')),
        ) for change in filter(lambda x: x.tag == 'change', list_element)
    ]

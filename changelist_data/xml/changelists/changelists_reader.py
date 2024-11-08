""" Reads the Changelists File, translates into Changelists Data types.
"""
from xml.etree.ElementTree import Element, ParseError, fromstring
from changelist_data.changelist import Changelist
from changelist_data.file_change import FileChange
from changelist_data.xml import xml_reader


def parse_xml(changelists_xml: str) -> Element:
    """ Parse an XML File. This should be a Changelists XML file.

    Parameters:
    - changelists_xml (str): The Changelists data in xml format.

    Returns:
    Element - the XML Root Element

    Raises:
    SystemExit - if the xml could not be parsed.
    """
    try:
        return fromstring(changelists_xml)
    except ParseError:
        exit("Unable to Parse Changelists XML File.")


def find_changelists_root(xml_root: Element) -> Element | None:
    """
    Extract the ChangeLists Root XML Element.

    Parameters:
    - xml_root (Element): The parsed xml root.
    
    Returns:
    Element - The XML Changelists element, or None.
    """
    for elem in xml_reader.filter_by_tag(xml_root, 'changelists'):
        return elem
    return None


def extract_list_elements(changelists_element: Element) -> list[Changelist]:
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
        ) for cl_element in xml_reader.filter_by_tag(changelists_element, 'list')
    ]


def _extract_change_data(
    list_element: Element,
) -> list[FileChange]:
    """
    Given a ChangeList XML Element, obtain the List of Changes.

    Parameters:
    - list_element (Element): The Element representing a Changelist.

    Returns:
    list[FileChange] - The list of structured FileChange.
    """
    return [
        FileChange(
            before_path=xml_reader.get_attr(change, 'beforePath'),
            before_dir=xml_reader.convert_bool(xml_reader.get_attr(change, 'beforeDir')),
            after_path=xml_reader.get_attr(change, 'afterPath'),
            after_dir=xml_reader.convert_bool(xml_reader.get_attr(change, 'afterDir')),
        ) for change in filter(lambda x: x.tag == 'change', list_element)
    ]

"""XML Reader Methods.
"""
from typing import Iterator
from xml.etree.ElementTree import Element


def filter_by_tag(element: Element, tag: str) -> Iterator[Element]:
    """
    Obtain all Elements that match a given Tag.
    
    Parameters:
    - element (Element): The element to search within.
    - tag (str): The name of the Tag to filter for.

    Returns:
    list[Element]
    """
    return filter(lambda x: x.tag == tag, element.iter())


def get_attr(element: Element, attr: str) -> str | None:
    """
    Obtain the Attribute from an element safely, returning None.

    Parameters:
    - element (Element): The element to obtain the attribute from.
    - attr (str): The name of the attribute.

    Returns:
    str | None - The value of the attribute, or None.
    """
    return element.attrib[attr] if attr in element.attrib else None


def get_attr_or(element: Element, attr: str, default: str) -> str:
    """
    Obtain the Attribute from an element safely, returning None if not found.

    Parameters:
    - element (Element): The element to obtain the attribute from.
    - attr (str): The name of the attribute.

    Returns:
    str - The value of the attribute in the element, or the default.
    """
    return element.attrib[attr] if attr in element.attrib else default


def read_bool_from(element: Element, attr: str) -> bool:
    """
    Obtain the Attribute from an element safely, returning None if not found.

    Parameters:
    - element (Element): The element to obtain the attribute from.
    - attr (str): The name of the attribute.

    Returns:
    bool - The attribute converted to a boolean.
    """
    value = get_attr_or(element, attr, 'false')
    return value.lower() == 'true'


def convert_bool(attr: str | None) -> bool | None:
    """
    Convert a String attribute to boolean.
    """
    if attr is None:
        return None
    return attr == 'true'
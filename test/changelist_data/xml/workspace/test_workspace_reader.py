"""Testing Changelist Reader Methods.
"""
from changelist_data.xml.workspace.workspace_reader import find_changelist_manager, parse_xml

from test.changelist_data.xml.workspace.provider import get_no_changelist_xml, get_simple_changelist_xml, get_multi_changelist_xml


def test_find_changelist_manager_empty_xml_raises_exit():
    try:
        find_changelist_manager(parse_xml(""))
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_find_changelist_manager_no_changelist_returns_none():
    assert find_changelist_manager(parse_xml(get_no_changelist_xml())) is None


def test_find_changelist_manager_simple_changelist_returns_element():
    element = find_changelist_manager(parse_xml(get_simple_changelist_xml()))
    change_lists = list(element.iter())
    assert len(change_lists) == 3


def test_find_changelist_manager_multi_changelist_returns_element():
    element = find_changelist_manager(parse_xml(get_multi_changelist_xml()))
    change_lists = list(element.iter())
    assert len(change_lists) == 6

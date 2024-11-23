"""Testing Changelist Reader Methods.
"""
import pytest

from changelist_data.xml.workspace.workspace_reader import find_changelist_manager, parse_xml, extract_list_elements

from test.changelist_data.xml.workspace.provider import get_no_changelist_xml, get_simple_changelist_xml, get_multi_changelist_xml


@pytest.fixture()
def simple_clm():
    return find_changelist_manager(parse_xml(get_simple_changelist_xml()))


@pytest.fixture()
def multi_clm():
    return find_changelist_manager(parse_xml(get_multi_changelist_xml()))


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


def test_extract_list_elements_simple_clm_(simple_clm):
    elem = extract_list_elements(simple_clm)
    assert len(elem) == 1
    assert len(elem[0].changes) == 1


def test_extract_list_elements_multi_clm_(multi_clm):
    elem = extract_list_elements(multi_clm)
    assert len(elem) == 2
    assert len(elem[0].changes) == 2
    assert len(elem[1].changes) == 1


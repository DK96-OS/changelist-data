"""Testing Changelist Reader Methods.
"""
import pytest

from changelist_data.xml.workspace.workspace_reader import find_changelist_manager, parse_xml, extract_list_elements


@pytest.fixture()
def simple_clm(simple_workspace_xml):
    return find_changelist_manager(parse_xml(simple_workspace_xml))


@pytest.fixture()
def multi_clm(multi_workspace_xml):
    return find_changelist_manager(parse_xml(multi_workspace_xml))


def test_find_changelist_manager_empty_xml_raises_exit():
    try:
        find_changelist_manager(parse_xml(""))
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_find_changelist_manager_no_changelist_returns_none(no_clm_workspace_xml):
    assert find_changelist_manager(parse_xml(no_clm_workspace_xml)) is None


def test_find_changelist_manager_simple_changelist_returns_element(simple_workspace_xml):
    element = find_changelist_manager(parse_xml(simple_workspace_xml))
    change_lists = list(element.iter())
    assert len(change_lists) == 3


def test_find_changelist_manager_multi_changelist_returns_element(multi_workspace_xml):
    element = find_changelist_manager(parse_xml(multi_workspace_xml))
    change_lists = list(element.iter())
    assert len(change_lists) == 6


def test_extract_list_elements_simple_clm_(simple_clm, simple_cl):
    elem = extract_list_elements(simple_clm)
    assert len(elem) == 1
    assert simple_cl == elem[0]


def test_extract_list_elements_multi_clm_(multi_clm, multi_cl_list):
    assert multi_cl_list == extract_list_elements(multi_clm)

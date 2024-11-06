"""Testing Changelist Reader Methods.
"""
from changelist_foci.workspace.workspace_reader import _extract_changelist_manager, read_workspace_changelists

from test.changelist_data.xml.workspace.provider import get_no_changelist_xml, get_simple_changelist_xml, get_multi_changelist_xml


def test_extract_changelist_manager_empty_xml_returns_none():
    assert _extract_changelist_manager("") is None


def test_extract_changelist_manager_no_changelist_returns_none():
    assert _extract_changelist_manager(get_no_changelist_xml()) is None


def test_extract_changelist_manager_simple_changelist_returns_element():
    element = _extract_changelist_manager(get_simple_changelist_xml())
    change_lists = list(element.iter())
    print(change_lists)


def test_extract_changelist_manager_multi_changelist_returns_element():
    element = _extract_changelist_manager(get_multi_changelist_xml())
    change_lists = list(element.iter())
    print(change_lists)


def test_read_workspace_changelists_empty_raises_error():
    try:
        read_workspace_changelists("")
        assert False
    except SystemExit:
        assert True


def test_read_workspace_changelists_no_change_list_returns_empty_list():
    try:
        read_workspace_changelists(get_no_changelist_xml())
        assert False
    except SystemExit:
        assert True


def test_read_workspace_changelists_simple_returns_single_changelist():
    result = read_workspace_changelists(get_simple_changelist_xml())
    assert 1 == len(result)
    # Check the First and only Changelist
    result_cl = result[0]
    assert result_cl.name == "Simple"
    assert result_cl.comment == "Main Program Files"
    assert result_cl.id == "9f60fda2-421e-4a4b-bd0f-4c8f83a47c88"
    assert not result_cl.is_default
    # Check Length of Changes
    change_length = len(result_cl.changes)
    assert 1 == change_length


def test_read_workspace_changelists_multi_returns_2_changelists():
    result = read_workspace_changelists(get_multi_changelist_xml())
    assert 2 == len(result)
    # Check both ChangeLists
    result_c1, result_c2 = result[0], result[1]
    #
    assert result_c1.name == "Main"
    assert result_c1.comment == "Main Program Files"
    assert result_c1.id == "af84ea1b-1b24-407d-970f-9f3a2835e933"
    assert result_c1.is_default
    #
    assert result_c2.name == "Test"
    assert result_c2.comment == "Test Files"
    assert result_c2.id == "9f60fda2-421e-4a4b-bd0f-4c8f83a47c88"
    assert not result_c2.is_default

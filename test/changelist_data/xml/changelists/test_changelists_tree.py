""" Testing the ChangelistsTree Class.
"""
from changelist_data.xml import changelists


def test_extract_list_elements_simple_returns_list(simple_cl_tree, simple_cl):
    result = simple_cl_tree.get_changelists()
    assert len(result) == 1
    assert simple_cl == result[0]


def test_extract_list_elements_multi_returns_list(multi_cl_tree, multi_cl_list):
    result = multi_cl_tree.get_changelists()
    assert len(result) == 2
    assert multi_cl_list == result


def test_extract_list_elements_no_cl_returns_empty_list(no_cl_tree):
    assert len(no_cl_tree.get_changelists()) == 0


def test_update_changelists_simple_with_empty(simple_cl_tree):
    simple_cl_tree.update_changelists([])
    assert len(simple_cl_tree.get_changelists()) == 0


def test_update_changelists_simple_with_multi(simple_cl_tree, multi_cl_tree):
    simple_cl_tree.update_changelists(
        multi_cl_tree.get_changelists()
    )
    result = simple_cl_tree.get_changelists()
    assert len(result) == 2
    assert result == multi_cl_tree.get_changelists()


def test_update_changelists_multi_with_simple(multi_cl_tree, simple_cl_tree):
    multi_cl_tree.update_changelists(
        simple_cl_tree.get_changelists()
    )
    result = multi_cl_tree.get_changelists()
    assert len(result) == 1
    assert result == simple_cl_tree.get_changelists()


def test_changelists_tree_no_changelists_tag_returns_empty_list(empty_changelists_xml):
    tree = changelists.load_xml(empty_changelists_xml)
    result = tree.get_changelists()
    assert len(result) == 0


def test_get_root_no_cl_manager_returns_root(no_cl_tree):
    assert no_cl_tree.get_root().getroot().tag == 'changelists'


def test_get_root_simple_returns_root(simple_cl_tree):
    assert simple_cl_tree.get_root().getroot().tag == 'changelists'


def test_get_root_multi_returns_root(multi_cl_tree):
    assert multi_cl_tree.get_root().getroot().tag == 'changelists'

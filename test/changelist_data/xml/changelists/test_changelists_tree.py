""" Testing the ChangelistsTree Class.
"""
from xml.etree.ElementTree import fromstring

from changelist_data.changelist import Changelist
from changelist_data.xml import changelists
from changelist_data.xml.changelists.changelists_tree import ChangelistsTree
from test.changelist_data.provider import get_module_src_change_data, get_module_test_change_data
from test.changelist_data.xml.changelists.provider import get_simple_changelist_xml, get_multi_changelist_xml, get_no_changelist_xml


def get_simple_ct_tree():
    return ChangelistsTree(fromstring(get_simple_changelist_xml()))

def get_multi_ct_tree():
    return ChangelistsTree(fromstring(get_multi_changelist_xml()))

def get_no_cl_ct_tree():
    return ChangelistsTree(fromstring(get_no_changelist_xml()))


def test_extract_list_elements_simple_returns_list():
    result = get_simple_ct_tree().get_changelists()
    assert len(result) == 1
    cl = result[0]
    assert cl.name == 'Simple'
    assert len(cl.changes) == 1
    file_change = cl.changes[0]
    assert file_change.before_path == '/main.py'
    assert not file_change.before_dir
    assert file_change.after_path == '/main.py'
    assert not file_change.after_dir


def test_extract_list_elements_multi_returns_list():
    result = get_multi_ct_tree().get_changelists()
    assert len(result) == 2
    # First Changelist
    cl_0 = result[0]
    assert cl_0.name == 'Main'
    assert len(cl_0.changes) == 2
    # Second Changelist
    cl_1 = result[1]
    assert cl_1.name == 'Test'
    assert len(cl_1.changes) == 1


def test_extract_list_elements_no_cl_returns_empty_list():
    ct_tree = get_no_cl_ct_tree()
    result = ct_tree.get_changelists()
    assert len(result) == 0


def test_update_changelists_simple_with_empty():
    ct_tree = get_simple_ct_tree()
    ct_tree.update_changelists([])
    # Get Elements
    result = ct_tree.get_changelists()
    assert len(result) == 0


def test_update_changelists_simple_with_multi():
    ct_tree = get_simple_ct_tree()
    ct_tree.update_changelists([
        Changelist(
            id='af84ea1b',
            name='Main',
            changes=[get_module_src_change_data()],
        ),
        Changelist(
            id='9f60fda2',
            name='Test',
            changes=[get_module_test_change_data()],
        )
    ])
    result = ct_tree.get_changelists()
    assert len(result) == 2


def test_changelists_tree_no_changelists_tag_returns_empty_list():
    tree = changelists.load_xml(get_no_changelist_xml())
    result = tree.get_changelists()
    assert len(result) == 0

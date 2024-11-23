""" Testing the ChangelistsTree Class.
"""
from xml.etree.ElementTree import fromstring

import pytest

from changelist_data.xml import changelists
from changelist_data.xml.changelists.changelists_tree import ChangelistsTree
from test.changelist_data.xml.changelists.provider import get_simple_changelist_xml, get_multi_changelist_xml, \
    get_no_changelist_xml


@pytest.fixture()
def simple_cl_tree():
    return ChangelistsTree(fromstring(get_simple_changelist_xml()))


@pytest.fixture()
def multi_cl_tree():
    return ChangelistsTree(fromstring(get_multi_changelist_xml()))


@pytest.fixture()
def no_cl_tree():
    return ChangelistsTree(fromstring(get_no_changelist_xml()))


def test_extract_list_elements_simple_returns_list(simple_cl_tree):
    result = simple_cl_tree.get_changelists()
    assert len(result) == 1
    cl = result[0]
    assert cl.name == 'Simple'
    assert len(cl.changes) == 1
    file_change = cl.changes[0]
    assert file_change.before_path == '/main.py'
    assert not file_change.before_dir
    assert file_change.after_path == '/main.py'
    assert not file_change.after_dir


def test_extract_list_elements_multi_returns_list(multi_cl_tree):
    result = multi_cl_tree.get_changelists()
    assert len(result) == 2
    # First Changelist
    cl_0 = result[0]
    assert cl_0.name == 'Main'
    assert len(cl_0.changes) == 2
    # Second Changelist
    cl_1 = result[1]
    assert cl_1.name == 'Test'
    assert len(cl_1.changes) == 1


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


def test_changelists_tree_no_changelists_tag_returns_empty_list():
    tree = changelists.load_xml(get_no_changelist_xml())
    result = tree.get_changelists()
    assert len(result) == 0


def test_get_root_no_cl_manager_returns_root(no_cl_tree):
    assert no_cl_tree.get_root().getroot().tag == 'changelists'


def test_get_root_simple_returns_root(simple_cl_tree):
    assert simple_cl_tree.get_root().getroot().tag == 'changelists'


def test_get_root_multi_returns_root(multi_cl_tree):
    assert multi_cl_tree.get_root().getroot().tag == 'changelists'

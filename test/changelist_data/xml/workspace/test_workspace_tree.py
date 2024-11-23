""" Testing the WorkspaceTree Class.
"""

import pytest

from changelist_data.xml import workspace
from test.changelist_data.xml.workspace import provider


@pytest.fixture()
def simple_ws_tree():
    return workspace.load_xml(provider.get_simple_changelist_xml())


@pytest.fixture()
def multi_ws_tree():
    return workspace.load_xml(provider.get_multi_changelist_xml())


@pytest.fixture()
def no_clm_ws_tree():
    return workspace.load_xml(provider.get_no_changelist_xml())


def test_get_changelists_simple_returns_list(simple_ws_tree):
    result = simple_ws_tree.get_changelists()
    assert len(result) == 1
    cl = result[0]
    assert cl.name == 'Simple'
    assert cl.comment == 'Main Program Files'
    assert len(cl.changes) == 1
    file = cl.changes[0]
    assert file.before_path == '/main.py'
    assert not file.before_dir
    assert file.after_path == '/main.py'
    assert not file.after_dir


def test_get_changelists_multi_returns_list(multi_ws_tree):
    result = multi_ws_tree.get_changelists()
    assert len(result) == 2
    # First Changelist
    cl_0 = result[0]
    assert cl_0.name == 'Main'
    assert len(cl_0.changes) == 2
    # Second Changelist
    cl_1 = result[1]
    assert cl_1.name == 'Test'
    assert len(cl_1.changes) == 1


def test_get_changelists_no_cl_returns_empty_list(no_clm_ws_tree):
    try:
        no_clm_ws_tree.get_changelists()
        assert False
    except SystemExit:
        assert True


def test_update_changelists_simple_with_empty_returns_empty(simple_ws_tree):
    simple_ws_tree.update_changelists([])
    assert len(simple_ws_tree.get_changelists()) == 0


def test_update_changelists_multi_with_empty_returns_empty(multi_ws_tree):
    multi_ws_tree.update_changelists([])
    assert len(multi_ws_tree.get_changelists()) == 0


def test_update_changelists_simple_with_multi(simple_ws_tree, multi_ws_tree):
    simple_ws_tree.update_changelists(
        multi_ws_tree.get_changelists()
    )
    result = simple_ws_tree.get_changelists()
    assert len(result) == 2
    assert result == multi_ws_tree.get_changelists()


def test_update_changelists_multi_with_simple(multi_ws_tree, simple_ws_tree):
    multi_ws_tree.update_changelists(
        simple_ws_tree.get_changelists()
    )
    result = multi_ws_tree.get_changelists()
    assert len(result) == 1
    assert result == simple_ws_tree.get_changelists()


def test_update_changelists_no_cl_manager_raises_exit(no_clm_ws_tree):
    try:
        no_clm_ws_tree.update_changelists([])
        raised_exit = False
    except SystemExit:
        raised_exit = True
    assert raised_exit


def test_get_root_no_cl_manager_returns_root(no_clm_ws_tree):
    assert no_clm_ws_tree.get_root().getroot().tag == 'project'


def test_get_root_simple_returns_root(simple_ws_tree):
    assert simple_ws_tree.get_root().getroot().tag == 'project'


def test_get_root_multi_returns_root(multi_ws_tree):
    assert multi_ws_tree.get_root().getroot().tag == 'project'

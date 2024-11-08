""" Testing the WorkspaceTree Class.
"""
from xml.etree.ElementTree import fromstring
from changelist_data.changelist import Changelist
from changelist_data.xml import workspace
from changelist_data.xml.workspace.workspace_tree import WorkspaceTree
from test.changelist_data.provider import get_module_test_change_data, get_module_src_change_data
from test.changelist_data.xml.workspace import provider


def get_simple_ws_tree():
    return workspace.load_xml(provider.get_simple_changelist_xml())

def get_multi_ws_tree():
    return workspace.load_xml(provider.get_multi_changelist_xml())

def get_no_cl_ws_tree():
    return workspace.load_xml(provider.get_no_changelist_xml())


def test_extract_list_elements_simple_returns_list():
    result = get_simple_ws_tree().get_changelists()
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


def test_extract_list_elements_multi_returns_list():
    result = get_multi_ws_tree().get_changelists()
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
    ws_tree = get_no_cl_ws_tree()
    try:
        ws_tree.get_changelists()
        assert False
    except SystemExit:
        assert True


def test_replace_changelists_simple_with_empty():
    ws_tree = get_simple_ws_tree()
    ws_tree.update_changelists([])
    # Get Elements
    result = ws_tree.get_changelists()
    assert len(result) == 0


def test_replace_changelists_simple_with_multi():
    ws_tree = get_simple_ws_tree()
    ws_tree.update_changelists([
        Changelist(
            id='af84ea1b',
            name='Main',
            changes=[get_module_src_change_data()],
        ),
        Changelist(
            id='9f60fda2',
            name='Test',
            changes=[get_module_test_change_data()],
        ),
    ])
    # Get Elements
    result = ws_tree.get_changelists()
    assert len(result) == 2


def test_replace_changelists_no_cl_manager_raises_exit():
    ws_tree = WorkspaceTree(fromstring(provider.get_no_changelist_xml()))
    try:
        ws_tree.update_changelists([])
        raised_exit = False
    except SystemExit:
        raised_exit = True
    assert raised_exit


def test_get_root_no_cl_manager_returns_root():
    ws_tree = WorkspaceTree(fromstring(provider.get_no_changelist_xml()))
    xml_root = ws_tree.get_root()
    assert xml_root.getroot().tag == 'project'

""" Testing Workspace XML Package Methods.
"""
from changelist_data.xml.workspace import load_xml


def test_load_xml_empty_str_raises_exit():
    try:
        load_xml("")
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_load_xml_no_cl_returns_new_tree(no_clm_workspace_xml):
    try:
        result = load_xml(no_clm_workspace_xml)
        result.get_changelists()
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_load_xml_simple_cl(simple_workspace_xml, simple_ws_tree):
    assert simple_ws_tree.get_changelists() == load_xml(simple_workspace_xml).get_changelists()


def test_load_xml_multi_cl(multi_workspace_xml, multi_ws_tree):
    assert multi_ws_tree.get_changelists() == load_xml(multi_workspace_xml).get_changelists()

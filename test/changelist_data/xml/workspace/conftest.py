""" XML Workspace Trees
"""
import pytest

from changelist_data.xml import workspace


@pytest.fixture()
def simple_ws_tree(simple_workspace_xml):
    return workspace.load_xml(simple_workspace_xml)


@pytest.fixture()
def multi_ws_tree(multi_workspace_xml):
    return workspace.load_xml(multi_workspace_xml)


@pytest.fixture()
def no_clm_ws_tree(no_clm_workspace_xml):
    return workspace.load_xml(no_clm_workspace_xml)

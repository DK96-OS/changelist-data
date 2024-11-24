""" Testing Workspace XML Package Methods.
"""
from changelist_data.xml.workspace import read_xml


def test_read_xml_empty_str_raises_exit():
    try:
        read_xml("")
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_read_xml_no_cl_raises_exit(no_clm_workspace_xml):
    try:
        read_xml(no_clm_workspace_xml)
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_read_xml_simple_cl(simple_workspace_xml, simple_cl_list):
    assert simple_cl_list == read_xml(simple_workspace_xml)


def test_read_xml_multi_cl(multi_workspace_xml, multi_cl_list):
    assert multi_cl_list == read_xml(multi_workspace_xml)

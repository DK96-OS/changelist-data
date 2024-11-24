""" Testing Workspace XML Package Methods.
"""
from changelist_data.xml.workspace import read_xml
from test.changelist_data.conftest import simple_cl


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


def test_read_xml_multi_cl(multi_workspace_xml):
    result = read_xml(multi_workspace_xml)
    assert len(result) == 2
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

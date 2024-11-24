""" Testing Changelists Reader.
"""
from changelist_data.xml.changelists import read_xml


def test_read_xml_empty_string_raises_exit():
    try:
        read_xml("")
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_read_xml_no_cl_returns_empty_list(empty_changelists_xml):
    result = read_xml(empty_changelists_xml)
    assert len(result) == 0

    
def test_read_xml_simple_xml_returns_simple_cl(simple_changelists_xml, simple_cl):
    assert [simple_cl] == read_xml(simple_changelists_xml)


def test_read_xml_multi_xml_returns_multi_cl_list(multi_changelists_xml, multi_cl_list):
    assert multi_cl_list == read_xml(multi_changelists_xml)

""" Testing Changelists XML read_xml Method.
"""
from changelist_data.xml.changelists import read_xml


def test_read_xml_empty_str_raises_exit():
    try:
        read_xml("")
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_read_xml_no_cl(empty_changelists_xml):
    result = read_xml(empty_changelists_xml)
    assert len(result) == 0


def test_read_xml_simple_cl(simple_changelists_xml, simple_cl_list):
    result = read_xml(simple_changelists_xml)
    assert len(result) == 1
    assert simple_cl_list == result


def test_read_xml_multi_cl(multi_changelists_xml, multi_cl_list):
    result = read_xml(multi_changelists_xml)
    assert len(result) == 2
    assert multi_cl_list == result

""" Testing Changelists XML load_xml Method.
"""
from changelist_data.xml.changelists import load_xml


def test_load_xml_empty_str_raises_exit():
    try:
        load_xml("")
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_load_xml_empty_returns_empty(empty_changelists_xml):
    result = load_xml(empty_changelists_xml).get_changelists()
    assert len(result) == 0


def test_load_xml_simple_cl(simple_changelists_xml, simple_cl_tree):
    result = load_xml(simple_changelists_xml).get_changelists()
    assert len(result) == 1
    assert simple_cl_tree.get_changelists() == result


def test_load_xml_multi_cl(multi_changelists_xml, multi_cl_tree):
    result = load_xml(multi_changelists_xml).get_changelists()
    assert len(result) == 2
    assert multi_cl_tree.get_changelists() == result
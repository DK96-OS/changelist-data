""" Testing Changelists XML Package Methods.
"""
from changelist_data.xml.changelists import read_xml, load_xml, new_tree
from test.changelist_data.xml.changelists import provider


def test_read_xml_empty_str_raises_exit():
    try:
        read_xml("")
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_read_xml_no_cl():
    xml_input = provider.get_no_changelist_xml()
    result = read_xml(xml_input)
    assert len(result) == 0


def test_read_xml_simple_cl():
    xml_input = provider.get_simple_changelist_xml()
    result = read_xml(xml_input)
    assert len(result) == 1


def test_read_xml_multi_cl():
    xml_input = provider.get_multi_changelist_xml()
    result = read_xml(xml_input)
    assert len(result) == 2


def test_load_xml_empty_str_raises_exit():
    try:
        load_xml("")
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_load_xml_no_cl():
    xml_input = provider.get_no_changelist_xml()
    result = load_xml(xml_input).get_changelists()
    assert len(result) == 0


def test_load_xml_simple_cl():
    xml_input = provider.get_simple_changelist_xml()
    result = load_xml(xml_input).get_changelists()
    assert len(result) == 1


def test_load_xml_multi_cl():
    xml_input = provider.get_multi_changelist_xml()
    result = load_xml(xml_input).get_changelists()
    assert len(result) == 2


def test_new_tree_has_zero_cl():
    result = new_tree()
    assert len(result.get_changelists()) == 0

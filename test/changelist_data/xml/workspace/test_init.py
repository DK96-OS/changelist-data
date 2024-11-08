""" Testing Workspace XML Package Methods.
"""
from changelist_data.xml.workspace import read_xml, load_xml
from test.changelist_data.xml.workspace import provider


def test_read_xml_empty_str_raises_exit():
    try:
        read_xml("")
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_read_xml_no_cl_raises_exit():
    try:
        read_xml(provider.get_no_changelist_xml())
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_read_xml_simple_cl():
    xml_input = provider.get_simple_changelist_xml()
    result = read_xml(xml_input)
    assert len(result) == 1
    # Check the First and only Changelist
    result_cl = result[0]
    assert result_cl.name == "Simple"
    assert result_cl.comment == "Main Program Files"
    assert result_cl.id == "9f60fda2-421e-4a4b-bd0f-4c8f83a47c88"
    assert not result_cl.is_default
    # Check Length of Changes
    change_length = len(result_cl.changes)
    assert 1 == change_length


def test_read_xml_multi_cl():
    xml_input = provider.get_multi_changelist_xml()
    result = read_xml(xml_input)
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


def test_load_xml_empty_str_raises_exit():
    try:
        load_xml("")
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_load_xml_no_cl_returns_new_tree():
    try:
        result = load_xml(provider.get_no_changelist_xml())
        result.get_changelists()
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_load_xml_simple_cl():
    result = load_xml(provider.get_simple_changelist_xml()).get_changelists()
    assert len(result) == 1


def test_load_xml_multi_cl():
    result = load_xml(provider.get_multi_changelist_xml()).get_changelists()
    assert len(result) == 2

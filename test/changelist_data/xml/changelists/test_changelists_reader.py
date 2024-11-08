""" Testing Changelists Reader.
"""
from changelist_data.xml.changelists import read_xml
from test.changelist_data.xml.changelists.provider import get_simple_changelist_xml, get_no_changelist_xml, \
    get_multi_changelist_xml


def test_read_xml_empty_string_raises_exit():
    try:
        read_xml("")
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_read_xml_no_cl_returns_empty_list():
    result = read_xml(get_no_changelist_xml())
    assert len(result) == 0

    
def test_read_xml_simple_cl():
    result = read_xml(get_simple_changelist_xml())
    assert len(result) == 1


def test_read_xml_multi_cl():
    result = read_xml(get_multi_changelist_xml())
    assert len(result) == 2
    cl = result[0]
    assert cl.name == "Main"
    assert cl.comment == "Main Program Files"
    assert len(cl.changes) == 2
    #
    cl = result[1]
    assert cl.name == "Test"
    assert cl.comment == "Test Files"
    assert len(cl.changes) == 1

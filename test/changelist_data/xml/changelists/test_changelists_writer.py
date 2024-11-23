""" Testing Changelists Writer
"""
from changelist_data.file_change import FileChange
from changelist_data.xml.changelists.changelists_writer import _write_change_data

from test.changelist_data.provider import fc_all, fc_before, fc_after, MODULE_SRC_PATH


def test_write_change_data_with_no_fields():
    data = FileChange()
    element = _write_change_data(data, 1)
    assert element.tag == 'change'
    assert element.attrib == {}


def test_write_change_data_with_all_fields(fc_all):
    element = _write_change_data(fc_all, 1)
    assert element.tag == 'change'
    assert element.get('beforePath') == MODULE_SRC_PATH
    assert element.get('afterPath') == MODULE_SRC_PATH
    assert element.get('beforeDir') == 'false'
    assert element.get('afterDir') == 'false'


def test_write_change_data_with_before_fields(fc_before):
    element = _write_change_data(fc_before, 1)
    assert element.tag == 'change'
    assert element.get('beforePath') == MODULE_SRC_PATH
    assert element.get('beforeDir') == 'false'
    assert element.get('afterDir') is None
    assert element.get('afterPath') is None


def test_write_change_data_with_after_fields(fc_after):
    element = _write_change_data(fc_after, 1)
    assert element.tag == 'change'
    assert element.get('beforePath') is None
    assert element.get('afterPath') == MODULE_SRC_PATH
    assert element.get('afterDir') == 'false'
    assert element.get('beforeDir') is None

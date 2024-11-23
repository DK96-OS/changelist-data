""" Testing Workspace Writer
"""
from changelist_data.file_change import FileChange
from changelist_data.xml.workspace import workspace_reader
from changelist_data.xml.workspace.workspace_writer import _write_change_data

from test.changelist_data.provider import fc_all, fc_before, fc_after


def test_write_change_data_with_no_fields():
    element = _write_change_data(FileChange(), 1)
    assert element.tag == 'change'
    assert element.attrib == {}


def test_write_change_data_with_all_fields(fc_all):
    element = _write_change_data(fc_all, 1)
    assert element.tag == 'change'
    assert element.get('beforePath') == f'{workspace_reader._PROJECT_DIR_VAR}{fc_all.before_path}'
    assert element.get('afterPath') == f'{workspace_reader._PROJECT_DIR_VAR}{fc_all.after_path}'
    assert element.get('beforeDir') == 'false'
    assert element.get('afterDir') == 'false'


def test_write_change_data_with_before_fields(fc_before):
    element = _write_change_data(fc_before, 1)
    assert element.tag == 'change'
    assert element.get('beforePath') == f'{workspace_reader._PROJECT_DIR_VAR}{fc_before.before_path}'
    assert element.get('beforeDir') == 'false'
    assert element.get('afterDir') is None
    assert element.get('afterPath') is None


def test_write_change_data_with_after_fields(fc_after):
    element = _write_change_data(fc_after, 1)
    assert element.tag == 'change'
    assert element.get('beforePath') is None
    assert element.get('afterPath') == f'{workspace_reader._PROJECT_DIR_VAR}{fc_after.after_path}'
    assert element.get('afterDir') == 'false'
    assert element.get('beforeDir') is None

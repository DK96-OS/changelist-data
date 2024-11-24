""" Testing Workspace Writer
"""
from changelist_data.file_change import FileChange
from changelist_data.xml.workspace import workspace_reader
from changelist_data.xml.workspace.workspace_writer import _write_change_data, write_list_element


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


def test_write_list_element_simple_returns(simple_cl):
    result = write_list_element(simple_cl, 2)
    assert result.tag == 'list'


def test_write_list_element_multi_returns(multi_cl_list):
    result0 = write_list_element(multi_cl_list[0], 2)
    result1 = write_list_element(multi_cl_list[1], 2)
    assert result0.tag == 'list'
    assert result1.tag == 'list'
    assert len(list(result0.iter('change'))) == 2
    assert len(list(result1.iter('change'))) == 1

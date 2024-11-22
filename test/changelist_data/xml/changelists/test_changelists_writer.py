""" Testing Changelists Writer
"""
from changelist_data.file_change import FileChange
from changelist_data.xml.changelists.changelists_writer import _write_change_data


def test_write_change_data_with_no_fields():
    data = FileChange()
    element = _write_change_data(data, 1)
    assert element.tag == 'change'
    assert element.attrib == {}


def test_write_change_data_with_all_fields():
    data = FileChange(
        before_path='old_file',
        after_path='new_file',
        before_dir=False,
        after_dir=False
    )
    element = _write_change_data(data, 1)
    assert element.tag == 'change'
    assert element.get('beforePath') == 'old_file'
    assert element.get('afterPath') == 'new_file'
    assert element.get('beforeDir') == 'false'
    assert element.get('afterDir') == 'false'


def test_write_change_data_with_before_fields():
    data = FileChange(
        before_dir=False,
        before_path='old_file',
    )
    element = _write_change_data(data, 1)
    assert element.tag == 'change'
    assert element.get('beforePath') == 'old_file'
    assert element.get('beforeDir') == 'false'
    assert element.get('afterDir') is None
    assert element.get('afterPath') is None


def test_write_change_data_with_after_fields():
    data = FileChange(
        after_dir=False,
        after_path='path/new_file.txt',
    )
    element = _write_change_data(data, 1)
    assert element.tag == 'change'
    assert element.get('beforePath') is None
    assert element.get('afterPath') == 'path/new_file.txt'
    assert element.get('afterDir') == 'false'
    assert element.get('beforeDir') is None

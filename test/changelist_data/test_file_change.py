"""Testing Module Methods.
"""
from changelist_data import file_change
from test.changelist_data.conftest import MODULE_SRC_PATH


def test_properties_module_src_after(fc_after):
    data = fc_after
    assert not data.before_dir 
    assert data.before_path is None
    assert not data.after_dir
    assert data.after_path == MODULE_SRC_PATH


def test_properties_module_src_before(fc_before):
    data = fc_before
    assert not data.before_dir
    assert data.before_path == MODULE_SRC_PATH
    assert not data.after_dir
    assert data.after_path is None


def test_properties_module_src_all(fc_all):
    data = fc_all
    assert not data.before_dir
    assert data.before_path == MODULE_SRC_PATH
    assert not data.after_dir
    assert data.after_path == MODULE_SRC_PATH


def test_create_fc_empty_str_returns_fc_empty_after_path():
    result = file_change.create_fc('')
    assert result.after_path == ''
    assert not result.after_dir
    # The other properties are None
    assert result.before_path is None
    assert result.before_dir is None


def test_update_fc_empty_str_returns_fc_empty_str_paths():
    result = file_change.update_fc('')
    assert result.after_path == ''
    assert not result.after_dir
    assert result.before_path == ''
    assert not result.before_dir


def test_delete_fc_empty_str_returns_fc_empty_str_paths():
    result = file_change.delete_fc('')
    assert result.before_path == ''
    assert not result.before_dir
    # The other properties are None
    assert result.after_path is None
    assert result.after_dir is None
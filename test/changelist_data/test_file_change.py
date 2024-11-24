"""Testing Module Methods.
"""
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

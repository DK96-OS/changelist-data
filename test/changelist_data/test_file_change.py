"""Testing Module Methods
"""
from test.changelist_data import provider


def test_properties_module_src():
    data = provider.get_module_src_change_data()
    assert not data.before_dir 
    assert data.before_path is None
    assert not data.after_dir
    assert data.after_path == provider.MODULE_SRC_PATH

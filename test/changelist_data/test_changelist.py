"""Testing ChangeList Data
"""
from test.changelist_data import provider


def test_properties_cl0():
    instance = provider.get_cl0()
    assert instance.id == '0'
    assert instance.name == ''
    assert len(instance.changes) == 0
    assert len(instance.comment) == 0
    assert not instance.is_default


def test_properties_cl1():
    instance = provider.get_cl1()
    assert instance.id == '1212434'
    assert instance.name == 'ChangeList'
    assert len(instance.changes) == 1
    assert len(instance.comment) == 0
    assert not instance.is_default

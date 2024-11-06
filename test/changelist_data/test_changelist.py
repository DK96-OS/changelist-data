"""Testing ChangeList Data
"""
from changelist_data.file_change import FileChange
from changelist_data.changelist import Changelist


def get_cl0():
    return Changelist(
        id="0",
        name="",
        changes=list(),
    )

def get_cl1():
    return Changelist(
        id="1212434",
        name="ChangeList",
        changes=[
            FileChange(
                after_path="/module/file.txt",
                after_dir=False,
            )
        ],
    )


def test_properties_cl0():
    instance = get_cl0()
    assert instance.id == '0'
    assert instance.name == ''
    assert len(instance.changes) == 0
    assert len(instance.comment) == 0
    assert not instance.is_default


def test_properties_cl1():
    instance = get_cl1()
    assert instance.id == '1212434'
    assert instance.name == 'ChangeList'
    assert len(instance.changes) == 1
    assert len(instance.comment) == 0
    assert not instance.is_default

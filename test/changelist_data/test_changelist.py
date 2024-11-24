"""Testing ChangeList Data
"""
import pytest

from changelist_data.changelist import Changelist
from changelist_data.file_change import FileChange


@pytest.fixture()
def sample_cl0():
    return Changelist(
        id="0",
        name="",
        changes=list(),
    )


@pytest.fixture()
def sample_cl1():
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


def test_properties_cl0(sample_cl0):
    assert sample_cl0.id == '0'
    assert sample_cl0.name == ''
    assert len(sample_cl0.changes) == 0
    assert len(sample_cl0.comment) == 0
    assert not sample_cl0.is_default


def test_properties_cl1(sample_cl1):
    assert sample_cl1.id == '1212434'
    assert sample_cl1.name == 'ChangeList'
    assert len(sample_cl1.changes) == 1
    assert len(sample_cl1.comment) == 0
    assert not sample_cl1.is_default

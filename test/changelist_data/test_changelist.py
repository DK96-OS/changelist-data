"""Testing ChangeList Data
"""
import pytest

from changelist_data import changelist
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


def test_get_default_cl_empty_list_returns_none():
    assert changelist.get_default_cl([]) is None


def test_get_default_cl_sample_cl0_list_returns_cl0(sample_cl0):
    assert changelist.get_default_cl([sample_cl0]) == sample_cl0


def test_get_default_cl_sample_cls_list_returns_first0(sample_cl0, sample_cl1):
    assert changelist.get_default_cl([sample_cl0, sample_cl1]) == sample_cl0


def test_get_default_cl_sample_cls_list_returns_first1(sample_cl0, sample_cl1):
    assert changelist.get_default_cl([sample_cl1, sample_cl0]) == sample_cl1


def test_get_default_cl_sample_cls_generator_returns_first1(sample_cl0, sample_cl1):
    def sample_cl_generator():
        yield from [sample_cl1, sample_cl0]
    assert changelist.get_default_cl(sample_cl_generator()) == sample_cl1


def test_get_default_cl_multi_cl_list_returns_default(multi_cl_list):
    assert changelist.get_default_cl(multi_cl_list) == multi_cl_list[0]


def test_get_default_cl_multi_cl_list_generator_returns_default(multi_cl_list):
    def multi_cl_generator():
        yield from multi_cl_list
    assert changelist.get_default_cl(multi_cl_generator()) == multi_cl_list[0]


def test_get_default_cl_empty_generator_returns_default():
    def multi_cl_generator():
        yield from []
    assert changelist.get_default_cl(multi_cl_generator()) is None


def test_get_default_cl_tuple_returns_first(sample_cl0, sample_cl1):
    assert changelist.get_default_cl((sample_cl0, sample_cl1)) == sample_cl0


def test_compute_key_empty_str_returns_empty_str():
    assert changelist.compute_key('') == ''


def test_compute_key_build_updates():
    assert changelist.compute_key('Build Updates') == 'buildupdates'


def test_compute_key_project_root():
    assert changelist.compute_key('Project Root') == 'projectroot'
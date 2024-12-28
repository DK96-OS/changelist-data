""" Testing Collections.
"""
from changelist_data.validation.collections import is_collection, divide_collection


def test_is_collection_list_returns_true():
    assert is_collection([])


def test_is_collection_tuple_returns_true():
    assert is_collection(tuple())


def test_is_collection_none_returns_false():
    assert not is_collection(None)


def test_is_collection_int_returns_false():
    assert not is_collection(4)


def test_is_collection_str_returns_false():
    assert not is_collection("apples")


def test_divide_collection_empty_returns_empty():
    result = list(divide_collection([]))
    assert len(result) == 0


def test_divide_collection_single_char_3_returns_3():
    result = list(divide_collection(['a', 'b', 'c'], 3))
    assert len(result) == 3
    assert result[0] == ['a']
    assert result[1] == ['b']
    assert result[2] == ['c']


def test_divide_collection_single_char_4_groups_2_returns_2_groups():
    result = list(divide_collection(['a', 'b', 'c', 'd'], 2))
    assert len(result) == 2
    assert result[0] == ['a', 'b']
    assert result[1] == ['c', 'd']


def test_divide_collection_single_char_4_groups_4_returns_4_groups():
    result = list(divide_collection(['a', 'b', 'c', 'd'], 4))
    assert len(result) == 4
    assert result[0] == ['a']
    assert result[1] == ['b']
    assert result[2] == ['c']
    assert result[3] == ['d']


def test_divide_collection_single_char_4_groups_3_returns_3_groups():
    result = list(divide_collection(['a', 'b', 'c', 'd'], 3))
    assert len(result) == 3
    assert result[0] == ['a']
    assert result[1] == ['b']
    assert result[2] == ['c', 'd']


def test_divide_collection_single_char_5_groups_3_returns_3_groups():
    result = list(divide_collection(['a', 'b', 'c', 'd', 'e'], 3))
    assert len(result) == 3
    assert result[0] == ['a']
    assert result[1] == ['b']
    assert result[2] == ['c', 'd', 'e']


def test_divide_collection_single_char_6_groups_3_returns_3_groups():
    result = list(divide_collection(['a', 'b', 'c', 'd', 'e', 'f'], 3))
    assert len(result) == 3
    assert result[0] == ['a', 'b']
    assert result[1] == ['c', 'd']
    assert result[2] == ['e', 'f']


def test_divide_collection_single_char_7_groups_3_returns_3_groups():
    result = list(divide_collection(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 3))
    assert len(result) == 3
    assert result[0] == ['a', 'b']
    assert result[1] == ['c', 'd']
    assert result[2] == ['e', 'f', 'g']

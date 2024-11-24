from changelist_data.xml.changelists import new_tree


def test_new_tree_has_zero_cl():
    result = new_tree()
    assert len(result.get_changelists()) == 0

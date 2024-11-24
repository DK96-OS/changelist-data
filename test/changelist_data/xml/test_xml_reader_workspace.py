"""Testing XML Reader Methods.
"""
from xml.etree.ElementTree import fromstring

from changelist_data.xml.xml_reader import filter_by_tag


def test_filter_by_tag_no_changelist_returns_empty(no_clm_workspace_xml):
    root_elem = fromstring(no_clm_workspace_xml)
    # There are no List Elements
    assert len(list(filter_by_tag(root_elem, 'list'))) == 0
    # There are no Change Elements
    assert len(list(filter_by_tag(root_elem, 'change'))) == 0


def test_filter_by_tag_simple_returns_1_list_1_change(simple_workspace_xml):
    root_elem = fromstring(simple_workspace_xml)
    # There is 1 List Element
    assert len(list(filter_by_tag(root_elem, 'list'))) == 1
    # There is 1 Change Element
    assert len(list(filter_by_tag(root_elem, 'change'))) == 1


def test_filter_by_tag_multi_returns_2_list_3_changes(multi_workspace_xml):
    root_elem = fromstring(multi_workspace_xml)
    # There are 2 List Elements
    assert len(list(filter_by_tag(root_elem, 'list'))) == 2
    # There are 3 Change Elements
    assert len(list(filter_by_tag(root_elem, 'change'))) == 3

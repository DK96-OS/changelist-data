"""
"""
from xml.etree.ElementTree import fromstring

import pytest

from changelist_data.xml.changelists import ChangelistsTree


@pytest.fixture()
def simple_cl_tree(simple_changelists_xml):
    return ChangelistsTree(fromstring(simple_changelists_xml))


@pytest.fixture()
def multi_cl_tree(multi_changelists_xml):
    return ChangelistsTree(fromstring(multi_changelists_xml))


@pytest.fixture()
def no_cl_tree(empty_changelists_xml):
    return ChangelistsTree(fromstring(empty_changelists_xml))


@pytest.fixture()
def invalid_cl_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<changelists>
<lisat id="af84ea1b9f3a2835e933" name="Main" comment="Main Files">
  <change beforePath="/main.py" beforeDir="false" />
</lisat>
</changelists>"""

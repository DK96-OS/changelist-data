""" Testing BaseXML Tree
"""
import tempfile
from pathlib import Path

import pytest

from changelist_data.xml import changelists, workspace
from changelist_data.xml.base_xml_tree import BaseXMLTree


@pytest.fixture
def temp_dir():
    tdir = tempfile.TemporaryDirectory()
    yield tdir
    tdir.cleanup()


@pytest.fixture
def temp_file(temp_dir):
    file = temp_dir.name + "/test_xml.xml"
    yield Path(file)


def test_write_file_changelists_new_tree_empty(temp_file):
    tree = changelists.new_tree()
    tree.write_tree(temp_file)
    # Read from File
    result = changelists.read_xml(temp_file.read_text())
    assert len(result) == 0


def test_write_file_workspace_simple_cl(temp_file, simple_workspace_xml):
    tree = workspace.load_xml(simple_workspace_xml)
    tree.write_tree(temp_file)
    # Read from File
    result = workspace.read_xml(temp_file.read_text())
    assert len(result) == 1


def test_write_file_changelists_simple_cl(temp_file, simple_changelists_xml):
    tree = changelists.load_xml(simple_changelists_xml)
    tree.write_tree(temp_file)
    # Read from File
    result = changelists.read_xml(temp_file.read_text())
    assert len(result) == 1


def test_get_root_raises_not_implemented_error():
    try:
        base_xml_tree = BaseXMLTree()
        base_xml_tree.get_root()
        raised_error = False
    except NotImplementedError:
        raised_error = True
    except TypeError:
        raised_error = True
    assert raised_error


def test_get_changelists_raises_not_implemented_error():
    try:
        base_xml_tree = BaseXMLTree()
        base_xml_tree.get_changelists()
        raised_error = False
    except NotImplementedError:
        raised_error = True
    except TypeError:
        raised_error = True
    assert raised_error


def test_update_changelists_raises_not_implemented_error():
    try:
        base_xml_tree = BaseXMLTree()
        base_xml_tree.update_changelists([])
        raised_error = False
    except NotImplementedError:
        raised_error = True
    except TypeError:
        raised_error = True
    assert raised_error

""" Testing BaseXML Tree
"""
import tempfile
from pathlib import Path

import pytest

from changelist_data.xml import changelists, workspace


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

""" Testing Storage of Workspace XML Files.
"""
from changelist_data.storage import workspace_storage


def test_read_file_no_cl_raises_exit(temp_file, no_clm_workspace_xml):
    temp_file.write_text(no_clm_workspace_xml)
    try:
        result = workspace_storage.read_file(temp_file)
        assert len(result) == 0
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_read_file_empty_cl(temp_file, empty_workspace_xml):
    temp_file.write_text(empty_workspace_xml)
    result = workspace_storage.read_file(temp_file)
    assert len(result) == 0


def test_read_file_simple_cl(temp_file, simple_workspace_xml):
    temp_file.write_text(simple_workspace_xml)
    result = workspace_storage.read_file(temp_file)
    assert len(result) == 1


def test_read_file_multi_cl(temp_file, multi_workspace_xml):
    temp_file.write_text(multi_workspace_xml)
    result = workspace_storage.read_file(temp_file)
    assert len(result) == 2


def test_load_file_no_cl(temp_file, no_clm_workspace_xml):
    temp_file.write_text(no_clm_workspace_xml)
    try:
        result = workspace_storage.load_file(temp_file)
        result.get_changelists()
        raises_exit = False
    except SystemExit:
        raises_exit = True
    assert raises_exit


def test_load_file_empty_cl(temp_file, empty_workspace_xml):
    temp_file.write_text(empty_workspace_xml)
    result = workspace_storage.load_file(temp_file)
    assert len(result.get_changelists()) == 0


def test_load_file_simple_cl(temp_file, simple_workspace_xml, simple_cl_list):
    temp_file.write_text(simple_workspace_xml)
    assert simple_cl_list == workspace_storage.load_file(temp_file).get_changelists()


def test_load_file_multi_cl(temp_file, multi_workspace_xml, multi_cl_list):
    temp_file.write_text(multi_workspace_xml)
    assert multi_cl_list == workspace_storage.load_file(temp_file).get_changelists()


def test_write_file_empty_cl(temp_file, empty_workspace_xml):
    temp_file.write_text(empty_workspace_xml)
    tree = workspace_storage.load_file(temp_file)
    workspace_storage.write_file(tree, temp_file)
    # Read from Temp
    result = workspace_storage.read_file(temp_file)
    assert len(result) == 0


def test_write_file_simple_cl(temp_file, simple_workspace_xml, simple_cl_list):
    temp_file.write_text(simple_workspace_xml)
    tree = workspace_storage.load_file(temp_file)
    workspace_storage.write_file(tree, temp_file)
    # Read from Temp
    assert simple_cl_list == workspace_storage.read_file(temp_file)


def test_write_file_multi_cl(temp_file, multi_workspace_xml, multi_cl_list):
    temp_file.write_text(multi_workspace_xml)
    tree = workspace_storage.load_file(temp_file)
    workspace_storage.write_file(tree, temp_file)
    # Read from Temp
    assert multi_cl_list == workspace_storage.read_file(temp_file)

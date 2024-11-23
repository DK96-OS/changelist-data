""" Methods for Writing XML.
"""
from xml.etree.ElementTree import Element, indent

from changelist_data.file_change import FileChange
from changelist_data.changelist import Changelist
from changelist_data.xml.workspace import workspace_reader


def write_list_element(
    changelist: Changelist,
    indent_level: int = 2,
) -> Element:
    """
    Convert a Changelist to XML Element format.

    Parameters:
    - changelist (Changelist): The Changelist data to format.

    Returns:
    str - A String containing the xml formatted contents of the Changelist. 
    """
    clist = Element('list')
    if changelist.is_default:
        clist.set('default', 'true')
    clist.set('id', changelist.id)
    clist.set('name', changelist.name)
    clist.set('comment', changelist.comment)
    for change in changelist.changes:
        clist.append(
            _write_change_data(
                data=change,
                indent_level=indent_level + 1,
            )
        )
    indent(clist, level=indent_level)
    return clist


def _write_change_data(
    data: FileChange,
    indent_level: int,
) -> Element:
    """
    Write the FileChange Data to XML format.

    Parameters:
    - data (FileChange): The FileChange Data for a specific File.

    Returns:
    str - A String containing the XML tag for this FileChange Data.
    """
    change = Element('change')
    if data.before_path is not None:
        change.set('beforePath', workspace_reader._PROJECT_DIR_VAR + data.before_path)
    if data.before_dir is not None:
        change.set('beforeDir', str(data.before_dir).lower())
    if data.after_path is not None:
        change.set('afterPath',workspace_reader._PROJECT_DIR_VAR + data.after_path)
    if data.after_dir is not None:
        change.set('afterDir', str(data.after_dir).lower())
    #
    indent(change, level=indent_level)
    return change

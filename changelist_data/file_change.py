""" Data container for File Change information.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class FileChange:
    """ The Change Information on a single file.

**Properties:**
 - before_path (str?): The initial path of the file.
 - before_dir (bool?): Whether the initial file is a directory.
 - after_path (str?): The final path of the file.
 - after_dir (bool?): Whether the final path is a directory.
    """
    before_path: str | None = None
    before_dir: bool | None = None
    after_path: str | None = None
    after_dir: bool | None = None


def create_fc(file_path_str: str) -> FileChange:
    """ Build a FC for a created file.
 - Created File Path is stored in the after_path attribute.
 - The after_dir attribute is set to false.

**Parameters:**
 - file_path_str (str): To be stored in FileChange.

**Returns:**
 FileChange - The dataclass object containing a Created FileChange.
    """
    return FileChange(after_path=file_path_str, after_dir=False)


def update_fc(file_path_str: str) -> FileChange:
    """ Build a FC for an updated file.
 - Updated Files contain a before and after path. If they don't match, it's a move-update.
 - Both before_dir and after_dir attribute are set to false.

**Parameters:**
 - file_path_str (str): To be stored in FileChange.

**Returns:**
 FileChange - The dataclass object containing an Update FileChange.
    """
    return FileChange(before_path=file_path_str, before_dir=False, after_path=file_path_str, after_dir=False)


def delete_fc(file_path_str: str) -> FileChange:
    """ Build a FC for a deleted file.
 - Deleted File Path is stored in the before_path attribute.
 - The before_dir attribute is set to false.

**Parameters:**
 - file_path_str (str): To be stored in FileChange.

**Returns:**
 FileChange - The dataclass object containing a Delete FileChange.
    """
    return FileChange(before_path=file_path_str, before_dir=False)
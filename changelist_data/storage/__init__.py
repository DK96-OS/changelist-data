""" Storage Access Methods.
"""
from pathlib import Path
from typing import Generator

from changelist_data.changelist import Changelist
from changelist_data.storage import file_validation, changelists_storage, workspace_storage
from changelist_data.storage.changelist_data_storage import ChangelistDataStorage
from changelist_data.storage.storage_type import StorageType, get_default_path
from changelist_data.xml.changelists import new_tree


def read_storage(
    option: StorageType | None = None,
    file_path: Path | None = None,
) -> list[Changelist]:
    """ Read Changelist Data from Storage into a List of Changelist data.
        - None values indicate that the storage file should be searched for using default values.

**Parameters:**
 - option (StorageType | None): The Storage Type describing the XML format. Search all StorageTypes in order by default.
 - file_path (Path | None): The file path to read from. Use None to look in default storage locations.

**Returns:**
 list[Changelist] - The List of Changelist data.
    """
    if file_path is not None:
        if option is None:
            exit("When File Path is Provided, The Storage Type must be Provided as well.")
        return list(_generate_option(option, file_path))
    # Find and Read from Default File Paths
    if option is None:
        if (storage_result := read_any_storage_option()) is not None:
            return storage_result
    elif (storage_path := file_validation.check_if_default_file_exists(option)) is not None:
        return list(_generate_option(option, storage_path))
    return []


def read_any_storage_option() -> list[Changelist] | None:
    """ Check the default locations for all storage options.
 - First checks Changelists, then Workspace locations.

**Returns:**
 list[Changelist]? - The list of Changelist data objects read from the file, or None.
    """
    if len(result := list(_generate_changelists_from_any_storage_option())) > 0:
        return result
    return None


def _generate_changelists_from_any_storage_option() -> Generator[Changelist, None, None]:
    for opts in StorageType:
        if (storage_path := file_validation.check_if_default_file_exists(StorageType(opts))) is not None:
            yield from _generate_option(StorageType(opts), storage_path)
            return None
    return None


def generate_changelists_from_storage(
    option: StorageType | None = None,
    file_path: Path | None = None,
) -> Generator[Changelist, None, None]:
    """ Read Changelist Data from Storage into a List of Changelist data.
- None values indicate that the storage file should be searched for using default values.

**Parameters:**
 - option (StorageType | None): The Storage Type describing the XML format. Search all StorageTypes in order by default.
 - file_path (Path | None): The file path to read from. Use None to look in default storage locations.

**Returns:**
 list[Changelist] - The List of Changelist data.
    """
    if file_path is not None:
        if option is None:
            exit("When File Path is Provided, The Storage Type must be Provided as well.")
        yield from _generate_option(option, file_path)
    # Find and Read from Default File Paths
    if option is None:
        if (storage_result := _generate_changelists_from_any_storage_option()) is not None:
            yield from storage_result
            return None
    elif (storage_path := file_validation.check_if_default_file_exists(option)) is not None:
        yield from _generate_option(option, storage_path)
    return None


def load_storage(
    option: StorageType | None = None,
    file_path: Path | None = None,
) -> ChangelistDataStorage:
    """ Load Changelist Data into a managed Storage object.
- None values indicate that the storage file should be searched for using default values.

**Parameters:**
 - option (StorageType | None): The Storage Type describing the XML format. Use None to search all StorageTypes in order.
 - file_path (Path | None): The file path to read from. Use None to look in default storage locations.

**Returns:**
 ChangelistDataStorage - A managed Storage object containing Changelist data.
    """
    if file_path is not None:
        if option is None:
            exit("When File Path is Provided, The Storage Type must be Provided as well.")
        return _load_option(option, file_path)
    # Find and Read from Default File Paths
    if option is None:
        if (storage_result := load_any_storage_option()) is not None:
            return storage_result
    elif (storage_path := file_validation.check_if_default_file_exists(option)) is not None:
        return _load_option(option, storage_path)
    # Create an empty Changelists Storage Tree with a default path
    return ChangelistDataStorage(
        new_tree(),
        StorageType.CHANGELISTS,
        get_default_path(StorageType.CHANGELISTS)
    )


def load_any_storage_option() -> ChangelistDataStorage | None:
    """ Check the default locations for all storage options.
 - First checks Changelists, then Workspace locations.
 - Returns None if no file is found.

**Returns:**
 ChangelistDataStorage? - The data object providing a read and write interface for the storage file.
    """
    for opts in StorageType:
        if (storage_path := file_validation.check_if_default_file_exists(StorageType(opts))) is not None:
            return _load_option(StorageType(opts), storage_path)
    return None


def _generate_option(
    option: StorageType,
    path: Path
) -> Generator[Changelist, None, None]:
    if option == StorageType.CHANGELISTS:
        yield from changelists_storage.generate_changelists_from_file(path)
    elif option == StorageType.WORKSPACE:
        yield from workspace_storage._generate_changelists_from_file(path)
    return None

def _load_option(
    option: StorageType,
    path: Path
) -> ChangelistDataStorage:
    if option == StorageType.CHANGELISTS:
        return ChangelistDataStorage(
            changelists_storage.load_file(path),
            option,
            path
        )
    if option == StorageType.WORKSPACE:
        return ChangelistDataStorage(
            workspace_storage.load_file(path),
            option,
            path
        )
    raise ValueError("Invalid Storage Option")
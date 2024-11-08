""" File Validation Methods
"""
from pathlib import Path

from changelist_data.storage import storage_type
from changelist_data.storage.storage_type import StorageType


CHANGELISTS_FILE_PATH_STR = '.changelists/data.xml'
WORKSPACE_FILE_PATH_STR = '.idea/workspace.xml'


def file_exists(path: Path) -> bool:
    """ Determines if Path exists and is_file.
    """
    return path.exists() and path.is_file()


def check_if_default_file_exists(
    option: StorageType,
) -> Path | None:
    """ Return the Path to the default file for this storage option iff it exists.

    Parameters:
    - option (StorageType): The StorageType option to check.

    Returns:
    Path | None - The Path to the Default Storage File, or None if the path is not a file that exists.
    """
    if file_exists(file_path := storage_type.get_default_path(option)):
        return file_path
    return None


def validate_file_input_text(file_path: Path) -> str:
    """
    Ensure that the File Exists, and is within reasonable size parameters.
        Read the File and return its string contents.

    Parameters:
    - file_path (Path): The Path to the Input File.

    Returns:
    str - The Text Contents of the Input File.

    Raises:
    SystemExit - When any of the validation conditions fails, or the file operation fails.
    """
    if not file_path.exists():
        exit("File did not exist")
    if not file_path.is_file():
        exit("Given Path was not a file")
    file_stats = file_path.stat()
    if (file_size := file_stats.st_size / 1024) > 32 * 1024:
        exit("Input File was larger than 32 MB. Refusing to read it.")
    try:
        return file_path.read_text()
    except FileNotFoundError:
        exit("Couldn't find the file, after checking that it exists.")
    except IOError:
        exit("IOError occurred while reading Input File")
    except Exception as e:
        exit(f"Unexpected Exception while reading InputFile(name={file_path.name}, fileSize={file_size} kb) Exception=({e})")

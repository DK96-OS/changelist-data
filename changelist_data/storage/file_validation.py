""" File Validation Methods
"""
from pathlib import Path


CHANGELISTS_FILE_PATH_STR = '.changelists/data.xml'
WORKSPACE_FILE_PATH_STR = '.idea/workspace.xml'


def _determine_if_file_exists(
    path: Path | None,
    default_path: Path,
) -> Path | None:
    """ Returns Path only if Storage File Exists.
    """
    if path is None:
        if default_path.exists() and default_path.is_file():
            return default_path
    elif path.exists() and path.is_file():
        return path
    return None


def find_changelists_storage(cl_path: Path | None = None) -> Path | None:
    """ Returns Path only if Changelists Storage File Exists.
    """
    return _determine_if_file_exists(cl_path, Path(CHANGELISTS_FILE_PATH_STR))


def find_workspace_storage(workspace_path: Path | None = None) -> Path | None:
    """ Returns Path only if Workspace Storage File Exists.
    """
    return _determine_if_file_exists(workspace_path, Path(WORKSPACE_FILE_PATH_STR))


def get_default_file_path() -> Path:
    """ Searches for Changelists, then Workspace.
        If neither is found, returns path to Changelists Data, but does not create the file.
    """
    if (cl_path := find_changelists_storage(None)) is not None:
        return cl_path
    if (ws_path := find_workspace_storage(None)) is not None:
        return ws_path
    return Path(CHANGELISTS_FILE_PATH_STR)


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
    except:
        exit(f"Unexpected Error occurred while reading Input File (name={file_path.name}, fileSize={file_size} kb)")

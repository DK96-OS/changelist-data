"""Data describing a File Change.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class FileChange:
    """The Change Information that is associated with a single file.

    Properties:
    - before_path (str | None): The initial path of the file.
    - before_dir (bool | None): Whether the initial file is a directory.
    - after_path (str | None): The final path of the file.
    - after_dir (bool | None): Whether the final path is a directory.
    """
    before_path: str | None = None
    before_dir: bool | None = None
    after_path: str | None = None
    after_dir: bool | None = None

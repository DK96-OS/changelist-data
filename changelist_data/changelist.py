"""The Data Class for a ChangeList.
"""
from dataclasses import dataclass

from changelist_data.file_change import FileChange


@dataclass(frozen=True)
class Changelist:
    """
    The Data class representing a ChangeList.
    
    Properties:
    - id (str): The unique id of the changelist.
    - name (str): The name of the changelist.
    - changes (list[ChangeData]): The list of file changes in the changelist.
    - comment (str): The comment associated with the changelist.
    - is_default (bool): Whether this is the active changelist.
    """
    id: str
    name: str
    changes: list[FileChange]
    comment: str = ""
    is_default: bool = False

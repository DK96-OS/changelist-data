"""The Data Class for a ChangeList.
"""
from dataclasses import dataclass
from typing import Iterable

from changelist_data.file_change import FileChange


@dataclass(frozen=True)
class Changelist:
    """ The Data class representing a ChangeList.
    
    Properties:
    - id (str): The unique id of the changelist.
    - name (str): The name of the changelist.
    - changes (list[ChangeData]): The list of file changes in the changelist.
    - comment (str): The comment associated with the changelist. Default: Empty String.
    - is_default (bool): Whether this is the active changelist. Default: False.
    """
    id: str
    name: str
    changes: list[FileChange]
    comment: str = ""
    is_default: bool = False


def get_default_cl(
    changelists: Iterable[Changelist],
) -> Changelist | None:
    """ Find the Default Changelist, or set the first Changelist to default.
        Returns None if lists is empty.
    """
    for cl in lists:
        if cl.is_default:
            return cl
    if len(lists) > 0: # First if no default attribute found
        return lists[0]
    return None

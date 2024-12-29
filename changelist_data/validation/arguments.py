""" String Validation Methods.
"""
from changelist_data.validation.collections import execute_boolean_operation_concurrently


_ILLEGAL_FILESYSTEM_CHARS: tuple[str,...] = ('&', ';', '\0', '<', '>', '*', '?', '|', '\n', '\r', ',', '^', '#', '@', '$',)


def validate_string_argument(
    argument: str | None,
    check_illegal_fs_chars: bool = True,
) -> bool:
    """ Determine whether an argument is a non-empty string.
        - Does not count whitespace.
        - Uses the strip method to remove empty space.

    Parameters:
    - argument (str): The given argument to validate.
    - check_illegal_fs_chars (bool): Whether to apply the Illegal Character filter. Default is True.

    Returns:
    bool - True if the argument qualifies as valid.
    """
    if argument is None or not isinstance(argument, str):
        return False
    elif len(simplified_arg := argument.strip()) < 1:
        return False
    elif check_illegal_fs_chars:
        return not has_illegal_filesystem_chars(simplified_arg)
    return True


def has_illegal_filesystem_chars(
    filesystem_argument: str,
) -> bool:
    """ Determines whether this argument contains illegal filesystem characters.

    Parameters:
    - filesystem_argument (str): The argument to be validated.

    Returns:
    bool - True if an illegal character was found in the sequence. The argument must be filtered or rejected.
    """
    for char in _ILLEGAL_FILESYSTEM_CHARS:
        if char in filesystem_argument:
            return True
    return False


def has_illegal_filesystem_chars_concurrent(
    filesystem_argument: str,
) -> bool:
    """ Determines whether this argument contains illegal filesystem characters.

    Parameters:
    - filesystem_argument (str): The argument to be validated.

    Returns:
    bool - True if an illegal character was found in the sequence. The argument must be filtered or rejected.
    """
    def check_chars(characters):
        for c in characters:
            if c in filesystem_argument:
                return True
        return False
    return execute_boolean_operation_concurrently(
        _ILLEGAL_FILESYSTEM_CHARS, check_chars, 4
    )

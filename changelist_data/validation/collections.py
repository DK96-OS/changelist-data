""" Validation Module Methods for Collections.
"""
from typing import Generator, Callable


def is_collection(input_argument) -> bool:
    """ Determines whether the input argument is a collection.
        - Valid collections are either a list or a tuple.

    Parameters:
    - input_argument (list | tuple): The argument to check.

    Returns:
    bool - True when the argument is a list or a tuple.
    """
    return isinstance(input_argument, list) or isinstance(input_argument, tuple)


def divide_collection(
    input_collection: list | tuple,
    num_groups: int = 2,
) -> Generator[list, None, None]:
    """ Divides a collection into smaller lists, yielding the results one by one.

    Parameters:
    - input_list (list | tuple[...]): The collection that will be divided.
    - num_groups (int): The number of groups to divide the collection into. Must be non-zero positive integer.

    Yields:
    list - Only yields lists of elements, even if a tuple was provided.
    """
    # Validate Arguments
    if not is_collection(input_collection):
        raise ValueError("Input must be a collection (list or tuple), was " + str(type(input_collection)))
    if not isinstance(num_groups, int) or num_groups <= 0:
        raise ValueError("Number of groups must be a positive integer")
    # Calculate the size of each group
    if num_groups > (collection_size := len(input_collection)):
        num_groups = collection_size
    group_size = 0 if 0 == num_groups else collection_size // num_groups
    # Generate smaller lists
    for i in range(num_groups):
        start_index = i * group_size
        end_index = (i + 1) * group_size if i < num_groups - 1 else None
        if 0 == len(new_group := input_collection[start_index:end_index]):
            break    # Prevent Empty lists from being generated
        yield new_group


def execute_boolean_operation_concurrently(
    input_collection: list | tuple,
    collection_operation: Callable[[list | tuple], bool],
    num_concurrent_groups: int = 4,
) -> bool:
    """ Execute a boolean operation on a collection of elements, concurrently.
        - Returns True as soon as possible.

    Parameters:
    - input_collection (list | tuple): The collection to be split and operated on concurrently.
    - collection_operation (Callable): A callable that executes on a list, and returns the first True result.
    - num_concurrent_groups (int): The number of groups to split the collection into.

    Returns:
    bool - True if any element in the collection causes the operation to return true.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed
    #
    with ThreadPoolExecutor() as executor:
        futures = [ # Submit tasks for groups of illegal characters
            executor.submit(collection_operation, char_groups)
            for char_groups in divide_collection(input_collection, num_concurrent_groups)
        ]
        for future in as_completed(futures): # As each task completes check for true result
            if future.result():
                return True
    return False

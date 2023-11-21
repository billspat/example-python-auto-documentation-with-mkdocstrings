"""(this documentation was automatically extracted from the module docstring at the top of /main_code_goes_here/combinatorics.py)

Defines basic combinatoric operations

- `permutations(values)` - Returns all permutations of a given list of values.
- `combinations(values)` - Returns all combinations of a given list of values.

Examples:
    >>> from main_code_goes_here import combinatorics
    >>> combinatorics.permutations(["a","b","c"])
    [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
    >>> combinatorics.combinations([1,2,3,4], 3)
    [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
"""

import itertools
from typing import TypeVar

T = TypeVar("T")


def permutations(values: list[T]) -> list[tuple[T, ...]]:
    """Return all possible permutations of values in given list

    Examples:
        >>> permutations(["sock",False])
        [('sock', False), (False, 'sock')]

    Args:
        values (list[Any]): A list of values (of any type)

    Returns:
        list[tuple]: A list of tuples (matching the types in the original input)
    """

    return list(itertools.permutations(values))


def combinations(values: list[T], r: int) -> list[tuple[T, ...]]:
    """Return all possible combinations containing r elements from the values in provided list

    Examples:
        >>> combinations([1,"dog",True], r=2)
        [(1, 'dog'), (1, True), ('dog', True)]

    Args:
        values (list[Any]): A list of values (of any type)
        r (int): Number of elements in each returned group

    Returns:
        list[tuple] : A list of tuples (matching the types in the original input)
    """

    return list(itertools.combinations(values, r))

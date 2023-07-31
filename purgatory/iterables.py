from itertools import chain, repeat
from typing import Iterable, TypeVar

T = TypeVar("T")


def repeat_values(it: Iterable[T], n: int) -> Iterable[T]:
    """[1, 2, 3] and n is 2, the function will return the iterable [1, 1, 2, 2, 3, 3]."""
    return chain.from_iterable(repeat(i, n) for i in it)

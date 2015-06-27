"""Actual sorting algorithms and associated logic.

Exports:
    SortAlg: Object containing various sort algorithms and source.
    parse_source: Returns source parsed into a list of sortable integers.
    remap: Returns a list with each value mapped to within a specified range.
"""
from config import DEFAULT_SOURCE, AVAILABLE_ALGS


def parse_source(source):
    """Return source as a list of sortable integers.

    Arguments:
        source (str): A whitespace-separated list of numbers.

    Returns:
        List[int]: A sortable list of integers.
        If provided source was empty or none, then return the default source.
    """
    try:
        if source.strip() == "":
            return DEFAULT_SOURCE
        else:
            # convert to a list of integers
            return list(map(int, source.strip().split()))
    except AttributeError:
        return DEFAULT_SOURCE


def remap(l, min_val=0, max_val=200):
    """Return a list with values mapped to a specified range.

    If the old range's minimum and maximum are the same value then use the
    midpoint.

    Arguments:
        l (List[int]): List of numbers to be mapped.
        min_val (Optional[int]): Minimum value of new range.
        max_val (Optional[int]): Maximum value of new range.

    Return:
        List[float]: The numbers mapped to their new ranges.
    """

    old_min = min(l)
    for i in l:
        try:
            i = ((i - old_min) * (max_val - min_val) / (max(l) - old_min)
                 + min_val)
        except ZeroDivisionError:
            i = (min_val + max_val) / 2
    return l


class SortAlg:
    """Main class for sort algorithms and implementation.

    Args:
        alg_name (str): A string representation of the name of the requested
            algorithm, prefixed with `sort_`.
        source (Optional[str]): A whitespace-separated list of numbers to pass
            to `parse_source()`. If omitted, then a default source will be used
            as per `parse_source()`.

    Attributes:
        alg: A sort method to use.
        name (str): A display name for the algorithm.
        source (List[int]): A list to sort.
        steps (List[List [int]]): A list containing the state of the list after
            every step in the sort.
    """

    def __init__(self, alg_name, source=DEFAULT_SOURCE):
        self.alg = getattr(self, alg_name)
        self.name = {i[0]: i[1] for i in AVAILABLE_ALGS}[alg_name]
        self.source = parse_source(source)
        self.steps = [self.source]

    def get_step(self, num):
        """Return the state of the list at the specified step of the sort.

        If the list has not yet been generated up to that point, then do so.

        Args:
            num (int): Zero-based step of the list to return.

        Returns:
            List[int]: State of the list at specified stage of sort.
        """
        try:
            if num < 0:
                return "Number too small."
            return self.steps[num]
        except IndexError:
            self.alg(len(self.source) + num - 1)
            return self.steps[num]

    def selection(self, duration=None):
        """Implement selection sort for specified number of steps."""
        from itertools import islice

        def _add_step(l, i):
            """Add a step of the sort to `self.steps`.

            Args:
                l (List[int]): List to perform step of sort on.
                i (int): Current position in list.
            """
            l = list(l)
            # Generator expression to yeild (value, i). Use itertools.islice
            # to look at sublist without creating new list.
            genexp = ((n, i) for i, n in enumerate(islice(l, i, len(l))))
            min_i = min(genexp)[0] + i  # minimum index adjusted for whole list
            if l[i] != l[min_i]:
                l[i], l[min_i] = l[min_i], l[i]  # swap minimum & current items
                self.steps.append(l)

        for i in range(len(self.steps[-1]) if duration is None else duration):
            _add_step(self.steps[-1], i)

    def bogo(self, duration=None):
        """Implement bogosort for specified number of steps."""
        from random import shuffle

        def _add_step(l):
            l = list(l)
            shuffle(l)
            self.steps.append(l)

        try:
            for _ in range(duration):
                _add_step(self.steps[-1])
        except TypeError:
            while sorted(self.steps[-1]) != self.steps[-1]:
                _add_step(self.steps[-1])

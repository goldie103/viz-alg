DEFAULT_SOURCE = [42, 0, 106, 10, 184]


def format_alg_name(alg):
    """Return a name formatted as a capitalized string."""
    UNSPACED_NAMES = ["bogo", "bogobogo", "quick"]
    return i.capitalize() + " Sort" if i not in UNSPACED_NAMES else "sort"


def remap(l, min_val=0, max_val=200):
    """Return a list with values mapped to a specified range."""
    old_min = min(l)
    for i in l:
        try:
            i = ((i - old_min) * (max_val - min_val) / (max(l) - old_min)
                 + min_val)
        except ZeroDivisionError:
            # for case where list contains all of one value
            # i.e. max(l) == min(l). In this case,
            # map to half of total range.
            i = (min_val + max_val) / 2
    return l


def parse_source(source, default=None):
    """Turn source to a list of integers. Use default if undefined."""

    if default is None:
        default = DEFAULT_SOURCE

    try:
        source = source.strip().split()
        return default if len(source) == 0 else list(map(int, source))
    except AttributeError:
        return default


class SortAlg:
    def __init__(self, alg_name, source=None):
        """
        Setup sorting algorithm object with specified alg and source. Alg must
        be a string containing the name of a sort function (e.g.
        "sort_selection"). Source can be ommitted, in which case a default
        source from config is used, a list of integers, or a
        whitespace-separated string of integers.
        """
        self.alg = getattr(self, alg_name)
        self.name = format_alg_name(alg_name)
        self.parse_source()
        self.steps = [self.source]

    def get_step(self, num):
        """Return the specified step of the sort process as a list"""
        try:
            if num < 0:
                return "Number too small."
            return self.steps[num]
        except IndexError:
            self.alg(len(self.source) + num - 1)
            return self.steps[num]

    def sort_selection(self, duration=None):
        """Build list with state of list after each stage of sort."""
        from itertools import islice

        def _add_step(l, i):
            """Return list after one step of selection sort."""
            l = list(l)
            # generator expression to return (value, i)
            # use itertools.islice to look at sublist without creating new list
            genexp = ((n, i) for i, n in enumerate(islice(l, i, len(l))))
            min_i = min(genexp)[0] + i
            if l[i] != l[min_i]:
                l[i], l[min_i] = l[min_i], l[i]
                self.steps.append(l)

        for i in range(len(self.steps[-1]) if duration is None else duration):
            _add_step(self.steps[-1], i)

    def sort_bogo(self, duration=None):
        """ Build list containing state of list after each stage of sort. """
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

algs = [i for i in dir(SortAlg) if i.startswith("sort_")]

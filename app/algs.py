from config import DEFAULT_SOURCE, AVAILABLE_ALGS


def parse_source(source):
    """Return source as a list of integers, using default if necessary."""
    try:
        if source.strip() == "":
            return DEFAULT_SOURCE
        else:
            # convert to a list of integers
            return list(map(int, source.strip().split()))
    except AttributeError:
        return DEFAULT_SOURCE


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


class SortAlg:
    def __init__(self, alg_name, source=DEFAULT_SOURCE):
        """
        Setup sorting algorithm object with specified alg and source. Alg must
        be a string containing the name of a sort function (e.g.
        "sort_selection"). Source can be ommitted, in which case a default
        source from config is used, a list of integers, or a
        whitespace-separated string of integers.
        """
        self.alg = getattr(self, alg_name)
        # props for displaying in page
        self.props = {
            "name": {i[0]: i[1] for i in AVAILABLE_ALGS}[alg_name],
            "source": parse_source(source)
        }
        self.props["steps"] = [self.props["source"]]

    def next_step(self):
        """Apply the next step of the sort."""
        self.alg(1)

    def selection(self, duration=None):
        """Build list with state of list after each stage of sort."""
        steps = self.props["steps"]

        def _add_step(l, i):
            """Return list after one step of selection sort."""
            l = list(l)
            cur_min = min(enumerate(l[i:]), key=lambda p: p[1])[0]
            if l[i] != l[cur_min + i]:
                l[i], l[cur_min + i] = l[cur_min + i], l[i]
                steps.append(l)

        for i in range(len(steps[-1]) if duration is None else duration):
            _add_step(steps[-1], i)

    def bogo(self, duration=None):
        """ Build list containing state of list after each stage of sort. """
        from random import shuffle
        steps = self.props["steps"]

        def _add_step(l):
            l = list(l)
            shuffle(l)
            steps.append(l)

        try:
            for _ in range(duration):
                _add_step(steps[-1])
        except TypeError:
            while sorted(steps[-1]) != steps[-1]:
                _add_step(steps[-1])

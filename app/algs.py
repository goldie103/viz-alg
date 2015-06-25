from config import DEFAULT_SOURCE, AVAILABLE_ALGS


class SortAlg:
    def __init__(self, alg, source=DEFAULT_SOURCE):
        """
        Setup sorting algorithm object with specified alg and source. Alg must
        be a string containing the name of a sort function (e.g.
        "sort_selection"). Source can be ommitted, in which case a default
        source from config is used, a list of integers, or a
        whitespace-separated string of integers.
        """
        self.alg = getattr(self, alg)
        # props for displaying in page
        self.props = {
            "name": {i[0]: i[1] for i in AVAILABLE_ALGS}[alg],
            "source": self.parse_source(source)
        }
        self.props["steps"] = [self.props["source"]]
        self.alg(self.props["steps"])

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
                i = ((i - old_min) * (max_val - min_val) /
                     (max(l) - old_min) + min_val)
            except ZeroDivisionError:
                # for case where list contains all of one value
                # i.e. max(l) == min(l). In this case,
                # map to half of total range.
                i = (min_val + max_val) / 2
        return l

    def sort_selection(self, steps):
        """ Build list with state of list after each stage of sort. """
        for i in range(len(steps[-1])):
            # loop through unsorted remainder of list
            for j in range(i, len(steps[-1])):
                if steps[-1][i] > steps[-1][j]:
                    steps.append(list(steps[-1]))
                    # swap first unsorted value with smaller unsorted value
                    steps[-1][i], steps[-1][j] = steps[-1][j], steps[-1][i]

    def sort_bogo(self, steps):
        """ Build list containing state of list after each stage of sort. """
        from random import shuffle
        while sorted(steps[-1]) != steps[-1]:
            steps.append(list(steps[-1]))
            shuffle(steps[-1])   # shuffle until sorted

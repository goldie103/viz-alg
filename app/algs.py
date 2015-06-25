from config import DEFAULT_SOURCE, AVAILABLE_ALGS


class SortAlg:
    def __init__(self, alg, source=DEFAULT_SOURCE):
        """ Setup sorting algorithm object with specified alg and source. """
        self.alg = getattr(self, alg)
        # props for displaying in page
        self.props = {
            "name": {i[0]: i[1] for i in AVAILABLE_ALGS}[alg],
            "source": source if source is not None else DEFAULT_SOURCE}
        self.props["steps"] = [self.props["source"]]
        self.alg(self.props["steps"])

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


class SortAlg:
    AVAILABLE_ALGS = [("sort_selection", "Selection Sort"),
                      ("sort_bogo", "Bogosort")]
    DEFAULT_LIST = [0, 42, 10, 11, 24]

    def __init__(self, alg, size=10):
        from random import sample
        self.alg = getattr(self, alg)
        # props for displaying in page
        self.props = {"name": {i[0]: i[1] for i in self.AVAILABLE_ALGS}[alg],
                      "source": sample(range(50), size)}
        self.props["steps"] = [self.props["source"]]
        self.alg(self.props["steps"])

    def sort_selection(self, steps):
        """
        Build list containing state of list after each stage in sorting with a
        selection sort algorithm implementation.
        """
        for i in range(len(steps[-1])):
            # loop through unsorted remainder of list
            for j in range(i, len(steps[-1])):
                if steps[-1][i] > steps[-1][j]:
                    steps.append(list(steps[-1]))
                    # swap first unsorted value with smaller unsorted value
                    steps[-1][i], steps[-1][j] = steps[-1][j], steps[-1][i]


    def sort_bogo(self, steps):
        """
        Build list containing state of list after each stage in sorting with a
        bogosort algorithm implementation.
        """
        from random import shuffle
        while sorted(steps[-1]) != steps[-1]:
            steps.append(list(steps[-1]))
            shuffle(steps[-1])   # shuffle until sorted


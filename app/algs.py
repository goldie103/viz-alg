
class SortAlg:
    AVAILABLE_ALGS = [("sort_selection", "Selection Sort"),
                      ("sort_bogo", "Bogosort")]
    DEFAULT_LIST = [0, 42, 10, 11, 24]

    def __init__(self, alg, size=10):
        from random import sample
        self.alg = getattr(self, alg)
        # props for displaying in page
        self.props = {"name": {i[0]: i[1] for i in self.AVAILABLE_ALGS}[alg],
                      "source": sample(range(50), size)
        }
        self.props["sorted_list"] = self.alg(self.props["source"])

    def sort_selection(self, l):
        """
        Return a list sorted with a selection sort implementation.
        """
        new = [i for i in l]    # temporary fix to weird assignment carryover

        for i in range(len(new)):
            # loop through unsorted remainder of list
            for j in range(i, len(new)):
                if new[i] > new[j]:
                    # swap first unsorted value with smaller unsorted value
                    new[i], new[j] = new[j], new[i]

        return new

    def sort_bogo(self, l):
        """
        Return a list sorted with a bogosort implementation
        """
        from random import shuffle
        new = [i for i in l]    # temporary fix to weird assignment carryover

        while sorted(new) != new:
            # shuffle until sorted
            shuffle(new)

        return new




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
        self.props["sorted_list"] = list(self.props["source"])
        self.sort_selection(self.props["sorted_list"])

    def sort_selection(self, l):
        """
        Return a list sorted with a selection sort implementation.
        """
        for i in range(len(l)):
            # loop through unsorted remainder of list
            for j in range(i, len(l)):
                if l[i] > l[j]:
                    # swap first unsorted value with smaller unsorted value
                    l[i], l[j] = l[j], l[i]

    def sort_bogo(self, l):
        """
        Return a list sorted with a bogosort implementation
        """
        from random import shuffle
        while sorted(l) != l: shuffle(l)   # shuffle until sorted




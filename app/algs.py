

class SortAlg:
    AVAILABLE_ALGS = [("sort_selection", "Selection Sort"),
                      ("sort_bogo", "Bogosort")]
    DEFAULT_LIST = [27, 12, 22, 49, 29]

    def __init__(self, alg):
        algs = {i[0]: i[1] for i in self.AVAILABLE_ALGS}
        self.alg = getattr(self, alg)
        self.name = algs[alg]

    def sort_selection(self, l):
        new = l

        for i in range(len(new)):
            # loop through unsorted remainder of list
            for j in range(i, len(new)):
                if new[i] > new[j]:
                    # swap first unsorted value with smaller unsorted value
                    new[i], new[j] = new[j], new[i]

        return new

    def sort_bogo(self, l):
        from random import shuffle
        new = l

        while sorted(new) != new:
            # shuffle until sorted
            shuffle(new)

        return new



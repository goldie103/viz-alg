#!flask/bin/python
"""
Basic testing framework, currently only testing a single default list.
"""

import unittest

from config import DEFAULT_SOURCE, AVAILABLE_ALGS
from app import app
from app.algs import SortAlg


class TestCase(unittest.TestCase):
    """ Basic testing framework """

    def setUp(self):
        """ Basic setup for testing, run before testing. """
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()

    def test_sorting(self):
        """ Check if each algorithm functions correctly """
        expected = {"sort_selection": [[0, 42, 10, 11, 25],
                                       [0, 10, 42, 11, 25],
                                       [0, 10, 11, 42, 25],
                                       [0, 10, 11, 25, 42]]}
        for alg, _ in AVAILABLE_ALGS:
            output = SortAlg(alg, DEFAULT_SOURCE).props["steps"]
            if alg != "sort_bogo":
                assert output == expected[alg]
            else:
                # bogosort is random and thus only final result can be tested
                assert output[-1] == sorted(DEFAULT_SOURCE)

if __name__ == "__main__":
    unittest.main()

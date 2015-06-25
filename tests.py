#!flask/bin/python
"""
Basic testing framework with coverage reports to determine what lines of code
are being executed during testing.
"""

import unittest
# coverage testing at top of file to have coverage logging begin immediately
from coverage import coverage
cov = coverage(branch=True, omit=["flask/*", "tests.py"])
cov.start()

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
    try:
        unittest.main()
    except:
        pass

    # observe what lines of code are executed in testing and which are not
    cov.stop()
    cov.save()
    print("\n\nCoverage Report:\n")
    cov.report()
    print("HTML version: {}".format("tmp/coverage/index.html"))
    cov.html_report(directory="tmp/coverage")
    cov.erase()

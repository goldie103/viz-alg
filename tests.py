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
        expected = {"sort_selection": [[42, 0, 106, 10, 184],
                                       [0, 42, 106, 10, 184],
                                       [0, 10, 106, 42, 184],
                                       [0, 10, 42, 106, 184]]}
        for alg, _ in AVAILABLE_ALGS:
            output = SortAlg(alg, DEFAULT_SOURCE).props["steps"]
            assert output[-1] == sorted(DEFAULT_SOURCE)
            if alg != "sort_bogo":
                assert output == expected[alg]

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

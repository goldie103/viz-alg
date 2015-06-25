#!flask/bin/python
"""
Basic testing framework with coverage reports to determine what lines of code
are being executed during testing.
"""

import unittest
import sys
from getopt import getopt, GetoptError

use_coverage = True

try:
    opts, args = getopt(sys.argv[1:], "q", ["quick"])
except GetoptError:
    print("usage: tests.py [-q] [--quick]")
    sys.exit()

for opt, arg in opts:
    if opt == "-q":
        use_coverage = False

if use_coverage:
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
        expected = {"selection": [[42, 0, 106, 10, 184],
                                  [0, 42, 106, 10, 184],
                                  [0, 10, 106, 42, 184],
                                  [0, 10, 42, 106, 184]]}
        for alg_name, _ in AVAILABLE_ALGS:
            alg = SortAlg(alg_name, DEFAULT_SOURCE)
            alg.alg()
            output = alg.props["steps"]
            assert output[-1] == sorted(DEFAULT_SOURCE), \
                "{} sort yeilded {}".format(alg_name, output[-1])
            if alg_name != "bogo":
                assert output == expected[alg_name], output

if __name__ == "__main__":
    try:
        unittest.main()
    except:
        pass

    if use_coverage:
        # observe what lines of code are executed in testing and which are not
        cov.stop()
        cov.save()
        print("\n\nCoverage Report:\n")
        cov.report()
        print("HTML version: {}".format("tmp/coverage/index.html"))
        cov.html_report(directory="tmp/coverage")
        cov.erase()

#!flask/bin/python
"""Basic testing framework with coverage reports.

Run simple unit tests on existing code and optionally generate a coverage
report detailing what hasn't been tested.

-q, --quick     Run without coverage reports.
"""

import sys
from os.path import join as pathjoin

import unittest
from getopt import getopt, GetoptError

from app import app
from app.algs import SortAlg, algs, DEFAULT_SOURCE


class TestCase(unittest.TestCase):
    """Basic testing framework."""

    def setUp(self):
        """Basic setup for testing, run before testing."""

        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()

    def test_sorting(self):
        """Check if each algorithm functions correctly

        Checks that the end result is as expected and, if possible, that it
        takes appropriate steps to get there.
        """

        expected = {"selection": [[42, 0, 106, 10, 184],
                                  [0, 42, 106, 10, 184],
                                  [0, 10, 106, 42, 184],
                                  [0, 10, 42, 106, 184]]}
        for alg_name in algs:
            alg = SortAlg(alg_name)
            alg_name = alg_name[len("sort_"):]
            alg.alg()
            output = alg.steps
            assert output[-1] == sorted(DEFAULT_SOURCE), \
                "{} sort yeilded {}".format(alg_name, output[-1])
            if alg_name != "bogo":
                assert output == expected[alg_name], output


def main(argv):
    # Parse command line options
    use_coverage = True

    try:
        opts, args = getopt(argv, "q", ["quick"])
    except GetoptError:
        print("usage: tests.py [-q] [--quick]")
        sys.exit()

    for opt, arg in opts:
        if opt == "-q":
            use_coverage = False

    if use_coverage:
        # Start coverage checking
        from coverage import coverage
        cov = coverage(branch=True, omit=app.config["COVERAGE_OMMITTED"])
        cov.start()

    # start testing
    try:
        unittest.main()
    except:
        pass

    if use_coverage:
        # Stop coverage checking and generate report
        cov.stop()
        cov.save()
        print("\n\nCoverage Report:\n")
        cov.report()
        print("HTML version: {}".format(pathjoin(app.config["COVERAGE_DIR"],
                                                 "index.html")))
        cov.html_report(directory=app.config["COVERAGE_DIR"])
        cov.erase()


if __name__ == "__main__":
    main(sys.argv[1:])

#!flask/bin/python
"""
Start webapp server on port 5000.
"""

import sys
from app import app


def main(argv):
    """
    Attempt to read command line options to begin server.
    Only option at present is -d to enable debug mode.
    """

    from getopt import getopt, GetoptError

    try:
        opts, args = getopt(argv, "d", ["debug"])
    except GetoptError:
        print("usage: run.py [-d]")
        sys.exit()

    for opt, arg in opts:
        if opt == "-d":
            debug = True

    try:
        app.run(debug=debug)
    except NameError:
        app.run()

if __name__ == "__main__":
    main(sys.argv[1:])

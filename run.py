#!flask/bin/python
"""Start a viz-alg webapp server on port 5000.

usage: run.py [-d] [--debug]
-d, --debug    Start with debug enabled, providing detailed error messages and
               stack traces on errors. If disabled then messages will be logged
               to tmp/viz-alg.log.
"""

import sys
from app import app


def main(argv):
    """Read command line options and run app accordingly.

    Reads arguments from argv and applies relevant options.
    Args:
        argv (list): Output from sys.argv excluding first item.
    """

    from getopt import getopt, GetoptError

    # Get options and arguments from argv
    try:
        opts, args = getopt(argv, "d", ["debug"])
    except GetoptError:
        print("usage: run.py [-d] [--debug]")
        sys.exit()

    # Set options
    for opt, arg in opts:
        if opt == "-d":
            debug = True

    # Run the script
    try:
        app.run(debug=debug)
    except NameError:
        app.run()

if __name__ == "__main__":
    main(sys.argv[1:])

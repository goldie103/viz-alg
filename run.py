#!flask/bin/python
import getopt
import sys
from app import app

def main(argv):
    """
    Attempt to read command line options to begin server.
    """
    try:
        opts, args = getopt.getopt(argv, "d", ["debug"])
    except getopt.GetoptError:
        print("usage: run.py [-d]")
        sys.exit()

    use_debug = False
    for opt, arg in opts:
        if opt == "-d":
            use_debug = True

    app.run(debug=use_debug)

if __name__ == "__main__":
    main(sys.argv[1:])

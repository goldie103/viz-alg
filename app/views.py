"""
Handles page display and routing for each page on the webapp.
"""
# library imports
from flask import render_template
# local code imports
from app import app
from .forms import InputForm
from .algs import SortAlg


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    """
    Main page of webapp.
    Briefly describe purpose and usage, show input form, and display output.
    """

    form = InputForm()

    if form.validate_on_submit():
        alg = SortAlg(form.alg.data, source=form.source.data).props

        # show output and hide input
        return render_template("index.html", title=alg["name"],
                               form=False, alg=alg)

    # show input and hide output
    return render_template("index.html", title="Home",
                           form=form, alg=False)


# Error Handling
def display_error(errnum, error):
    """ Return an error template with message depending on error number. """

    ERR_MSG = {404: "Sorry, the page you're looking for couldn't be found.",
               500: "Sorry, something went wrong. Try again?"}

    return render_template("err.html", title=error,
                           error=error, message=ERR_MSG[errnum])


# pass error number and types to function that does actual error processing
@app.errorhandler(404)
def not_found_error(error):
    return display_error(404, error), 404


@app.errorhandler(500)
def internal_error(error):
    return display_error(500, error), 500

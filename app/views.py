"""Handle page display and routing."""

from flask import render_template

from app import app
from .forms import InputForm
from .algs import SortAlg


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    """Handle display of main page of webapp.

    Returns:
        str: HTML of index.html with either a chosen algorithm or a form.
    """

    form = InputForm()

    if form.validate_on_submit():
        alg = SortAlg(form.alg.data, form.source.data)
        alg.alg()
        return render_template("index.html", title="Home", alg=alg)

    return render_template("index.html", title="Home", form=form)


# Error Handling
def display_error(errnum, error):
    """Return an error template with friendly message depending on error number.
    Args:
        errnum (int): Error number to render.
        error (str): Specific error message.

    Returns:
        str: Rendered error page with messages passed in.

    """

    ERR_MSG = {404: "Sorry, the page you're looking for couldn't be found.",
               500: "Sorry, something went wrong. Try again?",
               302: "Something went wrong; this one's on us."}

    return render_template("err.html", title=error,
                           error=error, message=ERR_MSG[errnum])


# pass error number and types to function that does actual error processing
@app.errorhandler(404)
def not_found_error(error):
    return display_error(404, error), 404


@app.errorhandler(500)
def internal_error(error):
    return display_error(500, error), 500


@app.errorhandler(302)
def request_error(error):
    return display_error(302, error), 302

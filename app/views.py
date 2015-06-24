from flask import render_template, flash, redirect
from app import app
from .forms import InputForm
from .algs import SortAlg

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    """
    Info and input page.
    """
    form = InputForm()
    if form.validate_on_submit():
        alg = SortAlg(form.alg.data, size=form.source_size.data).props

        return render_template("index.html", title=alg["name"],
                               form=False, alg=alg)

    return render_template("index.html", title="Home",
                           form=form, alg=False)



def display_error(errnum, error):
    ERR_MSG = {404: "Sorry, the page you're looking for couldn't be found.",
               500: "Sorry, something went wrong. Try again?"}
    return render_template("err.html", title=error,
                           error=error, message=ERR_MSG[errnum])

@app.errorhandler(404)
def not_found_error(error):
    return display_error(404, error), 404

@app.errorhandler(500)
def internal_error(error):
    return display_error(500, error), 500

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

        # show progress messages
        flash("Sorting {}".format(alg["source"]))
        flash("Sorted list: {}".format(alg["steps"]))

        # return render_template("view.html", title=alg["name"], alg=alg)

    return render_template("index.html",
                           title="Home",
                           form=form)

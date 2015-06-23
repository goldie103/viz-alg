from flask import render_template, flash, redirect
from app import app
from .forms import InputForm
from .algs import SortAlg

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    """Home page of webapp with associated info."""
    form = InputForm()
    if form.validate_on_submit():
        alg=SortAlg(form.alg.data, size=form.source_size.data)

        # Build class attributes that will be displayed in page
        alg={"name": alg.name,
             "list": alg.source,
             "sorted": alg.alg(alg.source)}

        # show progress messages
        flash("Sorting in progress")
        flash("Sorted list: {}".format(alg["sorted"]))

        return render_template("view.html",
                               title=alg["name"],
                               alg=alg)

    return render_template("index.html",
                           title="Home",
                           form=form)

@app.route("/view")
def view():
    """Return view of visualisations"""
    alg = {"name": "Selection Sort"}
    return render_template("view.html",
                           title="Home",
                           alg=alg)

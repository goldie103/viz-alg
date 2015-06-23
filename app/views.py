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
        alg=SortAlg(form.alg.data)
        alg={"name": alg.name,
             "list": alg.DEFAULT_LIST,
             "sorted": alg.alg(alg.DEFAULT_LIST)}
        flash("Sorting {alg} with list:\nsorted".format(alg=str(form.alg.data)))
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

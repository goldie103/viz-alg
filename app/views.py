from flask import render_template
from app import app

def selection_sort(l):
    for i in range(len(l)+1):
        if l[i] > l[0]:
            l[0], l[i] = l[i], l[0]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",
                           title="Home")

@app.route("/view")
def view():
    alg = {"name": "Selection Sort"}
    return render_template("views.html",
                           title="Home",
                           alg=alg)



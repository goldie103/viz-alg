from flask.ext.wtf import Form
from wtforms import BooleanField, SelectField
from wtforms.validators import DataRequired
from .algs import SortAlg

class InputForm(Form):
    alg = SelectField("alg", choices=SortAlg.AVAILABLE_ALGS)
    is_descending = BooleanField("is_descending", default=False)

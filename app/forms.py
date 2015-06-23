from flask.ext.wtf import Form
from wtforms import BooleanField, SelectField, IntegerField
from wtforms.validators import NumberRange
from .algs import SortAlg

class InputForm(Form):
    alg = SelectField("alg", choices=SortAlg.AVAILABLE_ALGS)
    source_size = IntegerField("source_size",
                               validators=[NumberRange(min=0, max=20)])
    is_descending = BooleanField("is_descending", default=False)


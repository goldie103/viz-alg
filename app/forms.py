"""
Form definition and validation for each part of webapp.
"""

# library imports
from flask.ext.wtf import Form
from wtforms import SelectField, StringField
from wtforms.validators import ValidationError
# local project imports
from config import AVAILABLE_ALGS, DEFAULT_SOURCE
from .alg import parse_source


def valid_source(form, field):
    """
    Check if field contains entry valid for a source list.

    Validity of entry is determined essentially by whether any exceptions are
    thrown when attempting to process the output into a list.

    Empty, whitespace and None entries are considered valid.
    """
    try:
        parse_source(field.data)
    except:
        raise ValidationError("Not a valid custom list.")


class InputForm(Form):
    """ Main input form for entering desired algorithm and settings. """

    default_formatted = ' '.join([str(i) for i in DEFAULT_SOURCE])

    alg = SelectField(
        label="Algorithm",
        description="A sorting algorithm you'd like to see visualized.",
        choices=AVAILABLE_ALGS)

    source = StringField(
        label="List to sort",
        description="A list to sort. If you don't enter anything the default"
        " {} will be used.".format(default_formatted),
        default=default_formatted,
        validators=[valid_source])

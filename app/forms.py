"""
Form definition and validation for each part of webapp.
"""

# library imports
from flask.ext.wtf import Form
from wtforms import SelectField, StringField
from wtforms.validators import ValidationError
# local project imports
from config import AVAILABLE_ALGS


def convert_source(s):
    """
    Return a string split into a list of integers.
    Returns None if an empty or whitespace string.
    """
    return None if s.strip() == "" else [int(i) for i in s.strip().split()]


def valid_source(form, field):
    """
    Check if field contains entry valid for a source list.

    Validity of entry is determined essentially by whether any exceptions are
    thrown when attempting to process the output into a list.

    Empty, whitespace and None entries are considered valid.
    """
    if field.data is not None and field.data.strip() != "":
        try:
            convert_source(field.data)
        except:
            raise ValidationError("Not a valid custom list.")


class InputForm(Form):
    """ Main input form for entering desired algorithm and settings. """
    alg = SelectField("alg", choices=AVAILABLE_ALGS)
    source = StringField("source", [valid_source])

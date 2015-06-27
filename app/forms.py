"""Form definition and validation.

Exports:
    InputForm: Algorithm request form.
"""

# library imports
from flask.ext.wtf import Form
from wtforms import SelectField, StringField
from wtforms.validators import ValidationError
# local project imports
from .algs import parse_source, DEFAULT_SOURCE, algs, format_alg_name


def valid_source(form, field):
    """Validator for source input field.

    Attempt to parse the source, and if it fails assume the list isn't valid.

    Args:
        form: Automatically-passed in containing form.
        field (Field): A completed field to validate.

    Raises:
        ValidationError: If parsing fails.

    """
    try:
        parse_source(field.data)
    except:
        raise ValidationError("Not a valid custom list.")


class InputForm(Form):
    """Main input form for entering desired algorithm.

    Attributes:
        alg (SelectField): Chosen algorithm to display.
        source (StringField): List of numbers to sort.
    """

    default_formatted = ' '.join([str(i) for i in DEFAULT_SOURCE])

    alg = SelectField(
        label="Algorithm",
        description="A sorting algorithm you'd like to see visualized.",
        choices=[(i, format_alg_name(i)) for i in algs])

    source = StringField(
        label="List to sort",
        description=("A list to sort. If you don't enter anything the default"
                     " will be used."),
        default=default_formatted,
        validators=[valid_source])

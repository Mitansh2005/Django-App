from django.core.exceptions import ValidationError
import re

def validate_no_special_characters(value):
    print(f"Validating: {value}")  # Debug print
    # Define a regular expression pattern to check for special characters
    if not re.match("^[A-Za-z0-9]*$", value):
        raise ValidationError('This field cannot contain special characters.')

def validate_phone_number(value):
    print(f"Validating: {value}")  # Debug print
    """Validator to check that phone number contains only digits."""
    if not re.match("^[0-9]*$", value):
        raise ValidationError('The phone number must contain only digits.')
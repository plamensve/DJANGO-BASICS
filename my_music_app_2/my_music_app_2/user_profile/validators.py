import re

from django.core.exceptions import ValidationError


def username_symbols_validator(value):
    if not re.match(r'^\w+$', value):
        raise ValidationError(
            'Ensure this value contains only letters, numbers, and underscore.',
            code='invalid_username'
        )
import re

from django.core.exceptions import ValidationError


def profile_user_name_symbol_validator(value):
    if not re.match(r'^\w+$', value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
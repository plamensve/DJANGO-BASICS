from django.core.exceptions import ValidationError


def validate_username_length(username):
    if len(username) < 3:
        raise ValidationError('Username must be at least 3 chars long!')


def validate_username_symbols(username):
    for x in username:
        if not (x.isalnum() or x == '_'):
            raise ValidationError('"Username must contain only letters, digits, and underscores!"')

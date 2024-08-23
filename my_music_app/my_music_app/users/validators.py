from django.core.exceptions import ValidationError


def username_chars_check(username):
    if not all(c.isalnum() or c == '_' for c in username):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
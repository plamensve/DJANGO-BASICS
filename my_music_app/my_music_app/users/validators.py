from django.core.exceptions import ValidationError


def username_chars_check(username):
    if not all(c.isalnum() or c == '_' for c in username):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def min_age_validations(age):
    if age < 0:
        raise ValidationError("Age cannot be below 0")

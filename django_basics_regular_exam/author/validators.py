from django.core.exceptions import ValidationError


def author_letters_validator(author):
    if not author.isalpha():
        raise ValidationError("Your name must contain letters only!")


def six_digit_validator(value):
    if len(value) != 6 or not value.isdigit():
        raise ValidationError("Your passcode must be a combination of exactly 6 digits!")


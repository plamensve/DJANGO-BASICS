from django.core.exceptions import ValidationError


def author_letters_validator(author):
    if not author.isalpha():
        raise ValidationError("Your name must contain letters only!")


def six_digit_validator(value):
    if not len(value) == 6:
        raise ValidationError("Your passcode must be exactly 6 digits!")

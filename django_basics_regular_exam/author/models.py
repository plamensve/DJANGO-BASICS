from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from author.validators import author_letters_validator, six_digit_validator


class Author(models.Model):
    AUTHOR_FIRST_NAME_MAX_LENGTH = 40
    AUTHOR_FIRST_NAME_MIN_LENGTH = 4
    AUTHOR_LAST_NAME_MAX_LENGTH = 50
    AUTHOR_LAST_NAME_MIN_LENGTH = 2

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=AUTHOR_FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(AUTHOR_FIRST_NAME_MIN_LENGTH),
            author_letters_validator
        ]
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=AUTHOR_LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(AUTHOR_LAST_NAME_MIN_LENGTH),
            author_letters_validator
        ]
    )

    passcode = models.CharField(
        null=False,
        blank=False,
        help_text="Your passcode must be a combination of 6 digits",
        validators=[
            six_digit_validator
        ]
    )

    pets_number = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
    )

    info = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

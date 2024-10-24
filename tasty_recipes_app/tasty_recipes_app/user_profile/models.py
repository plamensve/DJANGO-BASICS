from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from tasty_recipes_app.user_profile.validators import name_start_with_capital_letter_validator


class Profile(models.Model):
    MIN_LENGTH_NICK_NAME = 2
    MAX_LENGTH_NICK_NAME = 15
    MAX_LENGTH_FIRST_NAME = 30
    MAX_LENGTH_LAST_NAME = 30

    nick_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        validators=[
            MinLengthValidator(MIN_LENGTH_NICK_NAME, message='Nickname must be at least 2 chars long!'),
            MaxLengthValidator(MAX_LENGTH_NICK_NAME),
        ]
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        validators=[
            MaxLengthValidator(MAX_LENGTH_FIRST_NAME),
            name_start_with_capital_letter_validator,
        ]
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        validators=[
            MaxLengthValidator(MAX_LENGTH_LAST_NAME),
            name_start_with_capital_letter_validator,
        ]
    )

    chef = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )























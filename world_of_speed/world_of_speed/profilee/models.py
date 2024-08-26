from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.profilee.validators import validate_username_length, validate_username_symbols


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 3
    MIN_VALUE_AGE = 21
    MAX_LENGTH_PASSWORD = 20
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MAX_LENGTH = 25

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH_USERNAME,
        validators=[
            MinLengthValidator(MIN_LENGTH_USERNAME),
            validate_username_length,
            validate_username_symbols
        ],

    )

    email = models.CharField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(
                MIN_VALUE_AGE,
                message='Age requirement: 21 years and above.')
        ]
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH_PASSWORD
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_MAX_LENGTH
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=LAST_NAME_MAX_LENGTH
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )






















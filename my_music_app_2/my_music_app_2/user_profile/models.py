from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models

from my_music_app_2.user_profile.validators import username_symbols_validator


class Profile(models.Model):
    MIN_LENGTH_USER_NAME = 2
    MAX_LENGTH_USER_NAME = 15
    MIN_AGE_VALUE = 0

    username = models.CharField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_LENGTH_USER_NAME),
            MaxLengthValidator(MAX_LENGTH_USER_NAME),
            username_symbols_validator,
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_AGE_VALUE),
        )
    )
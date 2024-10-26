from django.core.validators import MinLengthValidator
from django.db import models

from my_music_app_3.profilee.validators import profile_user_name_symbol_validator


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 2

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[
            MinLengthValidator(MIN_LENGTH_USERNAME),
            profile_user_name_symbol_validator
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )









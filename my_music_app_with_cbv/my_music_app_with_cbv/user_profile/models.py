from django.core.validators import MinLengthValidator
from django.db import models

from my_music_app_with_cbv.user_profile.validators import username_validator_symbols


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 15

    username = models.CharField(
        null=False,
        blank=False,
        max_length=USERNAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(USERNAME_MIN_LENGTH),
            username_validator_symbols
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



















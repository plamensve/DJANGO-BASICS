from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.users.validators import username_chars_check


class Profile(models.Model):
    MIN_AGE = 0
    USER_NAME_MIN_LENGTH = 0
    USER_NAME_MAX_LENGTH = 15

    username = models.CharField(
        max_length=USER_NAME_MAX_LENGTH,
        validators=[MinLengthValidator(USER_NAME_MIN_LENGTH), username_chars_check]
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        validators=[MinValueValidator(MIN_AGE)]
    )
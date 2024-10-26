from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models

from world_of_speed_app_2.user_profile.validators import username_validator


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 3
    USERNAME_MAX_LENGTH = 15
    AGE_MIN_VALUE = 21
    PASSWORD_MAX_LENGTH = 20
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MAX_LENGTH = 25

    username = models.CharField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(USERNAME_MIN_LENGTH),
            MaxLengthValidator(USERNAME_MAX_LENGTH),
            username_validator
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(AGE_MIN_VALUE)
        ],
        help_text="Age requirement: 21 years and above."
    )

    password = models.CharField(
        null=False,
        blank=False,
        validators=[
            MaxLengthValidator(PASSWORD_MAX_LENGTH)
        ]
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        validators=[
            MaxLengthValidator(FIRST_NAME_MAX_LENGTH)
        ]
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        validators=[
            MaxLengthValidator(LAST_NAME_MAX_LENGTH)
        ]
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )



























































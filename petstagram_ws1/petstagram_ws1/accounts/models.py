from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class UserProfile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'
        DO_NOT_SHOW = 'DO NOT SHOW', 'DO NOT SHOW'

    username = models.CharField(
        null=False,
        blank=False,
        max_length=30
    ),

    password = models.CharField(
        null=False,
        blank=False,
        max_length=30
    ),

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=50
    )

    first_name = models.CharField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex='^[a-zA-Z]+$',
                message='First name should contain only letters.'
            )
        ],
        max_length=30
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex='^[a-zA-Z]+$',
                message='First name should contain only letters.'
            )
        ],
        max_length=30
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        choices=GenderChoices.choices,
        default=GenderChoices.DO_NOT_SHOW,
    )

    # TODO: •	When the user has been deleted,
    #  all their photos, pets, comments, and likes should be deleted too

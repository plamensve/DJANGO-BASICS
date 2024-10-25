from django.core.validators import MaxLengthValidator, MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed_app_2.car.validators import car_year_validator
from world_of_speed_app_2.user_profile.models import Profile


class Car(models.Model):
    CAR_TYPE_MAX_LENGTH = 10
    CAR_MODEL_MIN_LENGTH = 1
    CAR_MODEL_MAX_LENGTH = 15

    class TypeChoices(models.TextChoices):
        RALLY = 'Rally', 'Rally'
        OPEN_WHEEL = 'Open-Wheel', 'Open-Wheel'
        KART = 'Kart', 'Kart'
        DRAG = 'Drag', 'Drag'
        OTHER = 'Other', 'Other'

    type = models.CharField(
        null=False,
        blank=False,
        validators=[
            MaxLengthValidator(CAR_TYPE_MAX_LENGTH),
        ],
        choices=TypeChoices.choices,
    )

    model = models.CharField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(CAR_MODEL_MIN_LENGTH),
            MaxLengthValidator(CAR_MODEL_MAX_LENGTH),
        ],
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            car_year_validator
        ],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        }
    )

    price = models.DecimalField(
        null=False,
        blank=False,
        decimal_places=3,
        max_digits=10,
        validators=(
            MinValueValidator(1.000),
        ),
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='owner',
    )






































































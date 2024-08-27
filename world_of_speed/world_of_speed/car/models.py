from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.car.validators import validate_car_year
from world_of_speed.profilee.models import Profile


class Car(models.Model):
    CAR_TYPE_MAX_LENGTH = 10
    CAR_MODEL_MAX_LENGTH = 15
    CAR_MODEL_MIN_LENGTH = 1
    MIN_VALUE_PRICE = 1.0

    class CarTypeChoices(models.TextChoices):
        RALLY = 'Rally', 'Rally'
        OPEN_WHEEL = 'Open-wheel', 'Open-wheel'
        KART = 'Kart', 'Kart'
        DRAG = 'Drag', 'Drag'
        OTHER = 'Other', 'Other'

    type = models.CharField(
        null=False,
        blank=False,
        max_length=CAR_TYPE_MAX_LENGTH,
        choices=CarTypeChoices.choices
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=CAR_MODEL_MAX_LENGTH,
        validators=[
            MinLengthValidator(CAR_MODEL_MIN_LENGTH)
        ]
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            validate_car_year
        ]
    )

    image_url = models.URLField(
        unique=True,
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        }

    )

    price = models.FloatField(
        validators=[
            MinValueValidator(MIN_VALUE_PRICE)
        ]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )





































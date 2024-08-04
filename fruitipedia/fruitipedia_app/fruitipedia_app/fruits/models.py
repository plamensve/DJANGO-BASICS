from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.fruits.validators import check_name_letters


class Category(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False
    )

class Fruit(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=[
            MinLengthValidator(2),
            check_name_letters
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    nutrition = models.TextField(
        null=True,
        blank=True
    )
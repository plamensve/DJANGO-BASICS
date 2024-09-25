from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_ws1.pets.models import Pet
from petstagram_ws1.photos.validators import validate_file_size


class Photo(models.Model):
    photo = models.ImageField(
        validators=(validate_file_size,)
    )

    description = models.TextField(
        validators=[MinLengthValidator(10)],
        max_length=300
    )

    location = models.CharField(
        max_length=30
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
        related_name='tagged_pet_photo'
    )

    date_of_publication = models.DateField(
        auto_now=True
    )
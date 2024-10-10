from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from petstagram_2.pets.models import Pet
from petstagram_2.photos.validators import photo_size_validator


class Photo(models.Model):
    MIN_LENGTH_DESCRIPTION = 10
    MAX_LENGTH_DESCRIPTION = 300
    MAX_LENGTH_LOCATION = 30

    photo = models.ImageField(
        upload_to='images',
        validators=[
            photo_size_validator,
        ]
    )

    description = models.TextField(
        validators=[
            MinLengthValidator(MIN_LENGTH_DESCRIPTION),
            MaxLengthValidator(MAX_LENGTH_DESCRIPTION)
        ],
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=MAX_LENGTH_LOCATION,
        null=True,
        blank=True
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True
    )

    date_of_publication = models.DateField(
        auto_now=True
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        related_name='like_to_photo',
        on_delete=models.CASCADE
    )


class Comment(models.Model):
    TEXT_MAX_LENGTH = 300

    text = models.TextField(
        max_length=TEXT_MAX_LENGTH
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True
    )

    to_photo = models.ForeignKey(
        Photo,
        related_name='comment_to_photo',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-date_time_of_publication']

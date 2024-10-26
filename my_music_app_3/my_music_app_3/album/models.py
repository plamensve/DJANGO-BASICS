from django.core.validators import MinValueValidator
from django.db import models

from my_music_app_3.profilee.models import Profile


class Album(models.Model):
    MAX_LENGTH_ALBUM_NAME = 30
    MAX_LENGTH_ARTIST_NAME = 30
    MAX_LENGTH_GENRE_CHOICES = 30
    MIN_VALUE_PRICE = 0.0

    class GenreChoices(models.TextChoices):
        POP_MUSIC = "Pop Music", "Pop Music"
        JAZZ_MUSIC = "Jazz Music", "Jazz Music"
        RNB_MUSIC = "R&B Music", "R&B Music"
        ROCK_MUSIC = "Rock Music", "Rock Music"
        COUNTRY_MUSIC = "Country Music", "Country Music"
        DANCE_MUSIC = "Dance Music", "Dance Music"
        HIP_HOP_MUSIC = "Hip Hop Music", "Hip Hop Music"
        OTHER = "Other", "Other"

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=MAX_LENGTH_ALBUM_NAME
    )

    artist_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH_ARTIST_NAME
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH_GENRE_CHOICES,
        choices=GenreChoices.choices
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(MIN_VALUE_PRICE)
        ]
    )

    # TODO: Should be hidden from user
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
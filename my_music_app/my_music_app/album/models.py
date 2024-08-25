from django.core.validators import MinValueValidator
from django.db import models

from my_music_app.users.models import Profile


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    PRICE_MIN_VALUE = 0.0
    class GenreChoices(models.TextChoices):
        POP_MUSIC = 'Pop Music', 'Pop Music'
        JAZZ_MUSIC = 'Jazz Music', 'Jazz Music'
        RNB_MUSIC = 'R&B Music', 'R&B Music'
        ROCK_MUSIC = 'Rock Music', 'Rock Music'
        COUNTRY_MUSIC = 'Country Music', 'Country Music'
        DANCE_MUSIC = 'Dance Music', 'Dance Music'
        HIP_HOP_MUSIC = 'Hip Hop Music', 'Hip Hop Music'
        OTHER = 'Other', 'Other'

    album_name = models.CharField(
        unique=True,
        max_length=ALBUM_NAME_MAX_LENGTH
    )

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=ARTIST_MAX_LENGTH
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=GenreChoices.choices
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        validators=[MinValueValidator(PRICE_MIN_VALUE)]
    )

    # TODO: check ON_DELETE constraint
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )













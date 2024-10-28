from django.core.validators import MinValueValidator
from django.db import models

from my_music_app_with_cbv.user_profile.models import Profile


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH =30
    MIN_VALUE_PRICE = 0.0

    class GenreChoices(models.TextChoices):
        POP_MUSIC = ("Pop Music", "Pop Music")
        JAZZ_MUSIC = ("Jazz Music", "Jazz Music")
        RNB_MUSIC = ("R&B Music", "R&B Music")
        ROCK_MUSIC = ("Rock Music", "Rock Music")
        COUNTRY_MUSIC = ("Country Music", "Country Music")
        DANCE_MUSIC = ("Dance Music", "Dance Music")
        HIPHOP_MUSIC = ("Hip Hop Music", "Hip Hop Music")
        OTHER = ("Other", "Other")

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=ALBUM_NAME_MAX_LENGTH
    )

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=ARTIST_MAX_LENGTH
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=GENRE_MAX_LENGTH,
        choices=GenreChoices.choices
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_VALUE_PRICE)
        ]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )






















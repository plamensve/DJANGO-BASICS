from django.core.validators import MaxLengthValidator, MinValueValidator
from django.db import models

from my_music_app_2.user_profile.models import Profile


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    MIN_VALUE_PRICE = 0.0

    GENRE_CHOICES = [
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),]

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        validators=[
            MaxLengthValidator(ALBUM_NAME_MAX_LENGTH)
        ]
    )

    artist = models.CharField(
        null=False,
        blank=False,
        validators=[
            MaxLengthValidator(ARTIST_NAME_MAX_LENGTH)
        ]
    )

    genre = models.CharField(
        null=False,
        blank=False,
        validators=[
            MaxLengthValidator(GENRE_MAX_LENGTH)
        ],
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image_field = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_VALUE_PRICE)
        ],
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )















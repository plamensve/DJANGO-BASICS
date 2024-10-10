from django.db import models

from petstagram_2.photos.models import Photo


class Comment(models.Model):
    MAX_LENGTH_TEX_FIELD = 300

    text = models.TextField(
        max_length=MAX_LENGTH_TEX_FIELD
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-date_time_of_publication']

class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )
from django.db import models

from petstagram_ws1.photos.models import Photo


class Comment(models.Model):
    comment_text = models.TextField(
        max_length=300
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )

#test
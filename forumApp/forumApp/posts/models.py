from django.db import models

from forumApp.posts.validators import BadLanguageValidator


class Posts(models.Model):
    TOPIC_CHOICES = (
        ('PY', 'Python'),
        ('JS', 'Java Script'),
        ('C#', 'C Sharp'),
        ('OTHER', 'Other')
    )

    topic = models.CharField(
        choices=TOPIC_CHOICES,
        default='Other'
    )

    author = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    content = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        validators=[
            BadLanguageValidator()
        ]
    )

    image = models.ImageField(
        upload_to='post_images/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

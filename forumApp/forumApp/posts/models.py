from django.db import models


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
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class PersonInfor(models.Model):
    first_name = models.CharField(
        max_length=100,  # добавено max_length
        null=True,
        blank=True
    )
    second_name = models.CharField(
        max_length=100,  # добавено max_length
        null=True,
        blank=True
    )
    age = models.IntegerField(
        null=True,
        blank=True
    )

from django.db import models


from django.db import models

class Posts(models.Model):
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
    stats = models.CharField(
        max_length=100,  # добавено max_length
        null=True,
        blank=True,
        default=1
    )

class StudentWithChoices(models.Model):
    STATUS_CHOICES = (
        (1, 'DRAFT'),
        (2, 'PUBLISHED'),
        (3, 'ARCHIVED')
    )

    f_name = models.CharField(
        max_length=100,  # добавено max_length
        null=True,
        blank=True
    )

    status = models.IntegerField(
        max_length=20,  # добавено max_length
        choices=STATUS_CHOICES
    )

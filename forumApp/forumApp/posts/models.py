from django.db import models


class users_posts(models.Model):
    name = models.CharField(
        max_length=100
    )

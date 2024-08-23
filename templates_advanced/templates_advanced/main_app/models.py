from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    photo_1 = models.URLField(null=True, blank=True)
    photo_2 = models.URLField(null=True, blank=True)
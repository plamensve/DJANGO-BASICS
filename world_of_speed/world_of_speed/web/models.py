from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)

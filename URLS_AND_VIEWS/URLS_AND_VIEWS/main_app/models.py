from django.db import models


class employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)


#test
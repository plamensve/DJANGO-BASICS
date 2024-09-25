from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    name = models.CharField(
        max_length=30
    )

    photo = models.URLField(

    )

    date_of_birth = models.DateField(

    )

    #TODO : pet's day, month, and year of birth

    pet_slug = models.SlugField(
        auto_created=True,
        unique=True,
        null=False,
        blank=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.pet_slug:
            self.pet_slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


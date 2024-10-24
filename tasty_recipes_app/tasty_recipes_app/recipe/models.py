from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models
from tasty_recipes_app.user_profile.models import Profile


class Recipe(models.Model):
    TITLE_MIN_LENGTH = 10
    TITLE_MAX_LENGTH = 100
    MAX_CUISINE_TYPE = 7
    MIN_VALUE_COOKING_TIME = 1

    class CuisineTypeChoices(models.TextChoices):
        FRENCH = 'French', 'French'
        CHINESE = 'Chinese', 'Chinese'
        ITALIAN = 'Italian', 'Italian'
        BALKAN = 'Balkan', 'Balkan'
        OTHER = 'Other', 'Other'

    title = models.CharField(
        null=False,
        blank=False,
        unique=True,
        validators=[
            MinLengthValidator(TITLE_MIN_LENGTH),
            MaxLengthValidator(TITLE_MAX_LENGTH),
        ]
    )

    cuisine_type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_CUISINE_TYPE,
        choices=CuisineTypeChoices.choices,
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Ingredients must be separated by a comma and space."
    )

    cooking_time = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_VALUE_COOKING_TIME)
        ],
        help_text='Provide the cooking time in minutes.'
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='author'
    )

    def clean(self):
        if Recipe.objects.filter(title=self.title).exclude(pk=self.pk).exists():
            raise ValidationError({
                'title': "We already have a recipe with the same title!",
            })

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
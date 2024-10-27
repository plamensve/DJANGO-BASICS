from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from django_basics_regular_exam.author.models import Author


class Post(models.Model):
    TITLE_MAX_LENGTH = 50
    TITLE_MIN_LENGTH = 5
    IMAGE_URL_HELP_TEXT = "Share your funniest furry photo URL!"

    title = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=TITLE_MAX_LENGTH,
        validators=[
            MinLengthValidator(TITLE_MIN_LENGTH),
        ]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        help_text=IMAGE_URL_HELP_TEXT
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )

    # TODO: Трябва да тествам тази валидация
    def clean(self):
        if Post.objects.filter(title=self.title).exclude(id=self.id).exists():
            raise ValidationError("Oops! That title is already taken. How about something fresh and fun?")

    def validate_unique(self, *args, **kwargs):
        try:
            super().validate_unique(*args, **kwargs)
        except ValidationError as e:
            if 'title' in e.error_dict:
                del e.error_dict['title']
            if e.error_dict:
                raise e





















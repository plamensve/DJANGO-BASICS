from django.core.exceptions import ValidationError


def photo_size_validator(photo):
    limit = 5 * 1024 * 1024
    if photo.size > limit:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')

    #test
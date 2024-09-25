from django.core.exceptions import ValidationError


def validate_file_size(file_object):
    if file_object.size > 5 * 1024 * 1024:
        raise ValidationError('The maximum size that can be upload is 5MB')

# TODO - прегледай лекцията за да провериш как се прави class валидатор
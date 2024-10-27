from django import template

from django_basics_regular_exam.author.models import Author

register = template.Library()


@register.inclusion_tag('nav.html', takes_context=True)
def show_menu(context):
    request = context['request']

    profile_exists = Author.objects.first()

    return {
        'profile_exists': profile_exists,
    }
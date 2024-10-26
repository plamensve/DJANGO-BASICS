from django import template

from my_music_app_3.profilee.models import Profile

register = template.Library()


@register.inclusion_tag('nav.html', takes_context=True)
def show_menu(context):
    request = context['request']

    profile_exists = Profile.objects.first()

    return {
        'profile_exists': profile_exists,
    }

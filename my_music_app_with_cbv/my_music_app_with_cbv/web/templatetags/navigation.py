from django import template

from my_music_app_with_cbv.user_profile.models import Profile

register = template.Library()


@register.inclusion_tag('nav.html', takes_context=True)
def show_menu(context):

    profile_exists = Profile.objects.first()

    return {
        'profile_exists': profile_exists,
    }

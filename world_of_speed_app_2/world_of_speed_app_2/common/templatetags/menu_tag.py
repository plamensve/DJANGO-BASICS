from django import template
from django.shortcuts import render

from world_of_speed_app_2.user_profile.models import Profile

register = template.Library()


@register.inclusion_tag('nav.html', takes_context=True)
def render_menu(context):
    profile = Profile.objects.first()

    if profile:
        return {'profile': profile}
    else:
        return {'profile': None}
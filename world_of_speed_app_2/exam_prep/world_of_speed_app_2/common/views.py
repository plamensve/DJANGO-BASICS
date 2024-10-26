from django.shortcuts import render

from world_of_speed_app_2.user_profile.models import Profile


def home_page(request):
    return render(request, 'index.html')

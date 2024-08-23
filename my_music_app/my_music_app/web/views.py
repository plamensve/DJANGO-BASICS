from django.shortcuts import render

from my_music_app.users.models import Profile


def index(request):
    profile = Profile.objects.first()

    if profile:
        return render(request, 'home-with-profile.html')
    else:
        return render(request, 'home-no-profile.html')

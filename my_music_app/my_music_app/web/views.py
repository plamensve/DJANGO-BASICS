import form
from django import forms
from django.shortcuts import render, redirect

from my_music_app.album.models import Album
from my_music_app.users.models import Profile
from my_music_app.web.forms import ProfileForm


def create_profile(request):
    form = ProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            profile = form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def index(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()

    context = {
        'profile': profile,
        'albums': albums
    }

    if profile is None:
        return create_profile(request)

    return render(request, 'home-with-profile.html', context)



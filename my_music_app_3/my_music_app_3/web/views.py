from django.shortcuts import render, redirect

from my_music_app_3.album.models import Album
from my_music_app_3.profilee.models import Profile
from my_music_app_3.web.forms import CreateProfileForm


def index(request):
    profile = Profile.objects.first()
    all_albums = Album.objects.all()
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'all_albums': all_albums,
        'form': form
    }

    if profile:
        return render(request, 'profile/home-with-profile.html', context=context)

    return render(request, 'profile/home-no-profile.html', context=context)
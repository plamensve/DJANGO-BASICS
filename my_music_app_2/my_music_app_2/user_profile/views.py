from django.shortcuts import render, redirect
from my_music_app_2.album.models import Album
from my_music_app_2.user_profile.models import Profile


def profile_details(request):
    profile = Profile.objects.first()
    all_albums = Album.objects.all().count()

    context = {
        'profile': profile,
        'all_albums': all_albums,
    }

    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        profile.delete()
        return redirect('home-page')

    context = {
        'profile': profile,
    }

    return render(request, 'profile/profile-delete.html', context)


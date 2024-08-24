from django.shortcuts import render
from my_music_app.users.models import Profile


def profile_details(request):
    profile = Profile.objects.first()
    albums_count = profile.album_set.count()

    context = {
        'profile': profile,
        'albums_count': albums_count
    }

    return render(request, 'profile-details.html', context)


def profile_delete(request):
    return render(request, 'profile-delete.html')

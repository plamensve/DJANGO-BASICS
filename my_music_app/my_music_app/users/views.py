from django.shortcuts import render, redirect
from django.urls import reverse_lazy

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
    profile = Profile.objects.first()

    if request.method == 'POST':
        profile.delete()

        return redirect('index')

    return render(request, 'profile-delete.html')



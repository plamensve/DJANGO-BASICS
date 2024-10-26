from django.shortcuts import render, redirect

from my_music_app_3.profilee.models import Profile


def profile_details(request):
    profile = Profile.objects.first()
    album_count = profile.album_set.count()

    context = {
        'profile': profile,
        'album_count': album_count,
    }
    return render(request, 'profile/profile-details.html', context=context)


def profile_delete(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    return render(request, 'profile/profile-delete.html')

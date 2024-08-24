from django.shortcuts import render, redirect, get_object_or_404

from my_music_app.album.forms import CreateAlbum
from my_music_app.album.models import Album
from my_music_app.users.models import Profile


def add_album(request):
    form = CreateAlbum(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = Profile.objects.first()
            album = form.save()
            return redirect('index')
    context = {
        'form': form
    }

    return render(request, 'album-add.html', context)


def details_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    context = {
        'album': album
    }
    return render(request, 'album-details.html', context)


def edit_album(request):
    return render(request, 'album-edit.html')


def delete_album(request):
    return render(request, 'album-delete.html')

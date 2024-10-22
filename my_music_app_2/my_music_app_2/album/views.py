from django.shortcuts import render

from my_music_app_2.album.models import Album


def add_album_page(request):
    return render(request, 'album/album-add.html')


def details_page(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context=context)


def edit_album_page(request, pk):
    return render(request, 'album/album-edit.html')


def delete_album(request, pk):
    return render(request, 'album/album-delete.html')

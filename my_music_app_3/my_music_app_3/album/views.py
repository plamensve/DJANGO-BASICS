from django.shortcuts import render, redirect, get_object_or_404

from my_music_app_3.album.models import Album
from my_music_app_3.forms import CreateAlbumForm
from my_music_app_3.profilee.models import Profile


def add_album(request):
    form = CreateAlbumForm(request.POST or None)

    if form.is_valid():
        form.save(commit=False)
        form.instance.owner = Profile.objects.first()
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'album/album-add.html', context=context)


def details_album(request, pk):
    album = get_object_or_404(Album, pk=pk)

    context = {
        'album': album
    }

    return render(request, 'album/album-details.html', context=context)


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = CreateAlbumForm(request.POST or None, instance=album)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'album': album,
        'form': form,
    }

    return render(request, 'album/album-edit.html', context)


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = CreateAlbumForm(request.POST or None, instance=album)

    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'

    if request.method == 'POST':
        album.delete()
        return redirect('index')

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'album/album-delete.html', context)

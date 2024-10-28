from django.shortcuts import render


def album_add(request):
    return render(request, 'album/album-add.html')


def album_details(request, pk):
    return render(request, 'album/album-details.html')


def album_edit(request, pk):
    return render(request, 'album/album-edit.html')


def album_delete(request, pk):
    return render(request, 'album/album-delete.html')

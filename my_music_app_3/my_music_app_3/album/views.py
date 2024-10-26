from django.shortcuts import render


def add_album(request):
    return render(request, 'album/album-add.html')


def details_album(request, pk):
    return render(request, 'album/album-details.html')


def edit_album(request, pk):
    return render(request, 'album/album-edit.html')


def delete_album(request, pk):
    return render(request, 'album/album-delete.html')

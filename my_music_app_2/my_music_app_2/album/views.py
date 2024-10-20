from django.shortcuts import render


def add_album_page(request):
    return render(request, 'album-add.html')


def details_page(request, pk):
    return render(request, 'album-details.html')


def edit_album_page(request, pk):
    return render(request, 'album-edit.html')


def delete_album(request, pk):
    return render(request, 'album-delete.html')

from django.shortcuts import render


def add_album(request):
    return render(request, 'album-add.html')


def details_album(request):
    return render(request, 'album-details.html')


def edit_album(request):
    return render(request, 'album-edit.html')


def delete_album(request):
    return render(request, 'album-delete.html')

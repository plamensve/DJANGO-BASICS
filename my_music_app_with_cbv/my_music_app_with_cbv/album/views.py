from django.shortcuts import render


def album_add(request):
    return render(request, 'album/album-add.html')
